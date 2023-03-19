#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Create Time: 2022/11/30 00:00
# Create User: NB-Dragon
import os
import time
from helper.FileHelper import FileHelper
from helper.RequestHelper import RequestHelper
import base64 # 补充
import json
from core.protobuff import yang_pb2 # 补充
from core.protobuff import world_pb2
from google.protobuf import json_format


class OnlineDataAnalyzer(object):
    def __init__(self, static_map_path, static_map_link):
        self._request_helper = RequestHelper()
        self._static_map_path = static_map_path
        self._static_map_link = static_map_link

    def download_map_struct_data(self, summary_data: dict):
        if summary_data["err_code"] == 0:
            map_hash = self._get_game_map_hash(summary_data)
            self._create_local_struct_data(map_hash)

    def _create_local_struct_data(self, map_hash):
        map_cache_file = self._generate_map_cache_path(map_hash)
        if not self._is_file_up_to_date(map_cache_file):
            map_struct_data = self._request_map_struct_data(map_hash)
            self._save_local_struct_data(map_cache_file, map_struct_data, map_hash)

    def _request_map_struct_data(self, map_hash):
        map_struct_link = self._generate_map_struct_request_link(map_hash)
        return self._request_helper.request_get_method(map_struct_link)

    # @staticmethod
    def _save_local_struct_data(self, map_cache_file, map_struct_data, map_hash):
        if isinstance(map_struct_data, bytes) and len(map_struct_data):
            # map_struct_string = map_struct_data.decode() # 用proto解码
            map_struct_string = self._generate_decry_data(map_struct_data) # 用proto解码
            FileHelper().write_file_content(map_cache_file, map_struct_string)
            print("=====> 地图初始结构缓存成功: {}".format(map_hash))
        else:
            print("=====> 地图初始结构缓存失败: {}".format(map_hash))

    def _generate_map_struct_request_link(self, map_hash):
        return "{}/{}.map".format(self._static_map_link, map_hash) # 生成解码后的数据路径

    def _generate_map_cache_path(self, map_hash):
        map_cache_name = "{}.json".format(map_hash)
        return os.path.join(self._static_map_path, map_cache_name) # 原始地图数据

    def _is_file_up_to_date(self, file_path):
        if os.path.isfile(file_path):
            system_date = self._get_current_date()
            modify_date = self._get_file_modify_date(file_path)
            return system_date == modify_date
        return False

    @staticmethod
    def _get_game_map_hash(summary_data):
        print("=====> 当前游戏的地图结构密钥已更新")
        return summary_data["data"]["map_md5"][1]

    @staticmethod
    def _get_current_date():
        return time.strftime("%Y-%m-%d", time.localtime())

    @staticmethod
    def _get_file_modify_date(file_path):
        modify_time_second = os.path.getmtime(file_path)
        modify_time = time.localtime(modify_time_second)
        return time.strftime("%Y-%m-%d", modify_time)
    
    @staticmethod
    def _generate_decry_data(map_struct_data):
        gameMap_out = world_pb2.GameMap()
        gameMap_out.ParseFromString(map_struct_data[21:])
        map_data = json.loads(json_format.MessageToJson(gameMap_out))
        # print("原始数据：", map_data)

        level_data = map_data["levelData"]
        for level in level_data:
            level_data[level] = level_data[level].pop("llist", []) # 坑人的地方
            for idx, node_item in enumerate(level_data[level]):
                if("type" not in node_item):
                    level_data[level][idx]["type"] = 0
                if("rolNum" not in node_item):
                    level_data[level][idx]["rolNum"] = 0
                if("rowNum" not in node_item):
                    level_data[level][idx]["rowNum"] = 0
                if("layerNum" not in node_item):
                    level_data[level][idx]["layerNum"] = 0
                if("moldType" not in node_item):
                    level_data[level][idx]["moldType"] = 0
                if("blockNode" not in node_item):
                    level_data[level][idx]["blockNode"] = None
        # print("data:\n",map_data)
        return json.dumps(map_data)
