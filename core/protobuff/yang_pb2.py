# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yang.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nyang.proto\"g\n\rMatchPlayInfo\x12\x10\n\x08gameType\x18\x01 \x01(\x05\x12\r\n\x05mapId\x18\x02 \x01(\x05\x12\x0f\n\x07mapSeed\x18\x03 \x01(\x05\x12$\n\x0cstepInfoList\x18\x04 \x03(\x0b\x32\x0e.MatchStepInfo\"G\n\rMatchStepInfo\x12\x12\n\nchessIndex\x18\x01 \x01(\x05\x12\x0f\n\x07timeTag\x18\x02 \x01(\x05\x12\x11\n\tdeltaTime\x18\x03 \x01(\x05\"\x1f\n\nInviteJoin\x12\x11\n\tinviteUid\x18\x01 \x01(\t\".\n\nAwardState\x12\x11\n\tcondition\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\x05\"j\n\nInviteInfo\x12\x11\n\tinviteUid\x18\x01 \x01(\t\x12\x17\n\x0fjoinedUserIcons\x18\x02 \x03(\t\x12\x1e\n\tawardInfo\x18\x03 \x03(\x0b\x32\x0b.AwardState\x12\x10\n\x08\x65xpiring\x18\x04 \x01(\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yang_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MATCHPLAYINFO._serialized_start=14
  _MATCHPLAYINFO._serialized_end=117
  _MATCHSTEPINFO._serialized_start=119
  _MATCHSTEPINFO._serialized_end=190
  _INVITEJOIN._serialized_start=192
  _INVITEJOIN._serialized_end=223
  _AWARDSTATE._serialized_start=225
  _AWARDSTATE._serialized_end=271
  _INVITEINFO._serialized_start=273
  _INVITEINFO._serialized_end=379
# @@protoc_insertion_point(module_scope)
