"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmain.proto\x12\x05visao\x1a\x1bgoogle/protobuf/empty.proto"\x12\n\x04File\x12\n\n\x02id\x18\x01 \x01(\t"\x1a\n\nFileUpload\x12\x0c\n\x04file\x18\x01 \x01(\x0c"\x13\n\x05Image\x12\n\n\x02id\x18\x01 \x01(\t27\n\x05VisAO\x12.\n\nUploadFile\x12\x11.visao.FileUpload\x1a\x0b.visao.File"\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'main_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_FILE']._serialized_start = 50
    _globals['_FILE']._serialized_end = 68
    _globals['_FILEUPLOAD']._serialized_start = 70
    _globals['_FILEUPLOAD']._serialized_end = 96
    _globals['_IMAGE']._serialized_start = 98
    _globals['_IMAGE']._serialized_end = 117
    _globals['_VISAO']._serialized_start = 119
    _globals['_VISAO']._serialized_end = 174