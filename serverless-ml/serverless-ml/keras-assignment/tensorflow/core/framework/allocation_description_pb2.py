# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/allocation_description.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/framework/allocation_description.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=_b('\n\030org.tensorflow.frameworkB\033AllocationDescriptionProtosP\001Z=github.com/tensorflow/tensorflow/tensorflow/go/core/framework\370\001\001'),
  serialized_pb=_b('\n6tensorflow/core/framework/allocation_description.proto\x12\ntensorflow\"\xa3\x01\n\x15\x41llocationDescription\x12\x17\n\x0frequested_bytes\x18\x01 \x01(\x03\x12\x17\n\x0f\x61llocated_bytes\x18\x02 \x01(\x03\x12\x16\n\x0e\x61llocator_name\x18\x03 \x01(\t\x12\x15\n\rallocation_id\x18\x04 \x01(\x03\x12\x1c\n\x14has_single_reference\x18\x05 \x01(\x08\x12\x0b\n\x03ptr\x18\x06 \x01(\x04\x42{\n\x18org.tensorflow.frameworkB\x1b\x41llocationDescriptionProtosP\x01Z=github.com/tensorflow/tensorflow/tensorflow/go/core/framework\xf8\x01\x01\x62\x06proto3')
)




_ALLOCATIONDESCRIPTION = _descriptor.Descriptor(
  name='AllocationDescription',
  full_name='tensorflow.AllocationDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requested_bytes', full_name='tensorflow.AllocationDescription.requested_bytes', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allocated_bytes', full_name='tensorflow.AllocationDescription.allocated_bytes', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allocator_name', full_name='tensorflow.AllocationDescription.allocator_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allocation_id', full_name='tensorflow.AllocationDescription.allocation_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_single_reference', full_name='tensorflow.AllocationDescription.has_single_reference', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ptr', full_name='tensorflow.AllocationDescription.ptr', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=234,
)

DESCRIPTOR.message_types_by_name['AllocationDescription'] = _ALLOCATIONDESCRIPTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AllocationDescription = _reflection.GeneratedProtocolMessageType('AllocationDescription', (_message.Message,), dict(
  DESCRIPTOR = _ALLOCATIONDESCRIPTION,
  __module__ = 'tensorflow.core.framework.allocation_description_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.AllocationDescription)
  ))
_sym_db.RegisterMessage(AllocationDescription)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
