# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Fighting.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Fighting.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x46ighting.proto\"\x19\n\tUserInput\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x05\")\n\rUserInputData\x12\n\n\x02ID\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x05\"I\n\x11\x43ollectUsersInput\x12\x0c\n\x04step\x18\x01 \x01(\x05\x12&\n\x0eusersInputData\x18\x02 \x03(\x0b\x32\x0e.UserInputDataB\x08\xaa\x02\x05Protob\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_USERINPUT = _descriptor.Descriptor(
  name='UserInput',
  full_name='UserInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='UserInput.data', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=43,
)


_USERINPUTDATA = _descriptor.Descriptor(
  name='UserInputData',
  full_name='UserInputData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='UserInputData.ID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='UserInputData.data', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=86,
)


_COLLECTUSERSINPUT = _descriptor.Descriptor(
  name='CollectUsersInput',
  full_name='CollectUsersInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='CollectUsersInput.step', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usersInputData', full_name='CollectUsersInput.usersInputData', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=161,
)

_COLLECTUSERSINPUT.fields_by_name['usersInputData'].message_type = _USERINPUTDATA
DESCRIPTOR.message_types_by_name['UserInput'] = _USERINPUT
DESCRIPTOR.message_types_by_name['UserInputData'] = _USERINPUTDATA
DESCRIPTOR.message_types_by_name['CollectUsersInput'] = _COLLECTUSERSINPUT

UserInput = _reflection.GeneratedProtocolMessageType('UserInput', (_message.Message,), dict(
  DESCRIPTOR = _USERINPUT,
  __module__ = 'Fighting_pb2'
  # @@protoc_insertion_point(class_scope:UserInput)
  ))
_sym_db.RegisterMessage(UserInput)

UserInputData = _reflection.GeneratedProtocolMessageType('UserInputData', (_message.Message,), dict(
  DESCRIPTOR = _USERINPUTDATA,
  __module__ = 'Fighting_pb2'
  # @@protoc_insertion_point(class_scope:UserInputData)
  ))
_sym_db.RegisterMessage(UserInputData)

CollectUsersInput = _reflection.GeneratedProtocolMessageType('CollectUsersInput', (_message.Message,), dict(
  DESCRIPTOR = _COLLECTUSERSINPUT,
  __module__ = 'Fighting_pb2'
  # @@protoc_insertion_point(class_scope:CollectUsersInput)
  ))
_sym_db.RegisterMessage(CollectUsersInput)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\005Proto'))
# @@protoc_insertion_point(module_scope)
