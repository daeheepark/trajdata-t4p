# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vectorized_map.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x14vectorized_map.proto\x12\x08trajdata"\xb0\x01\n\rVectorizedMap\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x08\x65lements\x18\x02 \x03(\x0b\x32\x14.trajdata.MapElement\x12\x1f\n\x06max_pt\x18\x03 \x01(\x0b\x32\x0f.trajdata.Point\x12\x1f\n\x06min_pt\x18\x04 \x01(\x0b\x32\x0f.trajdata.Point\x12\'\n\x0eshifted_origin\x18\x05 \x01(\x0b\x32\x0f.trajdata.Point"\xd8\x01\n\nMapElement\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\'\n\troad_lane\x18\x02 \x01(\x0b\x32\x12.trajdata.RoadLaneH\x00\x12\'\n\troad_area\x18\x03 \x01(\x0b\x32\x12.trajdata.RoadAreaH\x00\x12/\n\rped_crosswalk\x18\x04 \x01(\x0b\x32\x16.trajdata.PedCrosswalkH\x00\x12+\n\x0bped_walkway\x18\x05 \x01(\x0b\x32\x14.trajdata.PedWalkwayH\x00\x42\x0e\n\x0c\x65lement_data"(\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01"F\n\x08Polyline\x12\r\n\x05\x64x_mm\x18\x01 \x03(\x11\x12\r\n\x05\x64y_mm\x18\x02 \x03(\x11\x12\r\n\x05\x64z_mm\x18\x03 \x03(\x11\x12\r\n\x05h_rad\x18\x04 \x03(\x01"\x98\x02\n\x08RoadLane\x12"\n\x06\x63\x65nter\x18\x01 \x01(\x0b\x32\x12.trajdata.Polyline\x12.\n\rleft_boundary\x18\x02 \x01(\x0b\x32\x12.trajdata.PolylineH\x00\x88\x01\x01\x12/\n\x0eright_boundary\x18\x03 \x01(\x0b\x32\x12.trajdata.PolylineH\x01\x88\x01\x01\x12\x13\n\x0b\x65ntry_lanes\x18\x04 \x03(\x0c\x12\x12\n\nexit_lanes\x18\x05 \x03(\x0c\x12\x1b\n\x13\x61\x64jacent_lanes_left\x18\x06 \x03(\x0c\x12\x1c\n\x14\x61\x64jacent_lanes_right\x18\x07 \x03(\x0c\x42\x10\n\x0e_left_boundaryB\x11\n\x0f_right_boundary"d\n\x08RoadArea\x12,\n\x10\x65xterior_polygon\x18\x01 \x01(\x0b\x32\x12.trajdata.Polyline\x12*\n\x0einterior_holes\x18\x02 \x03(\x0b\x32\x12.trajdata.Polyline"3\n\x0cPedCrosswalk\x12#\n\x07polygon\x18\x01 \x01(\x0b\x32\x12.trajdata.Polyline"1\n\nPedWalkway\x12#\n\x07polygon\x18\x01 \x01(\x0b\x32\x12.trajdata.Polylineb\x06proto3'
)


_VECTORIZEDMAP = DESCRIPTOR.message_types_by_name["VectorizedMap"]
_MAPELEMENT = DESCRIPTOR.message_types_by_name["MapElement"]
_POINT = DESCRIPTOR.message_types_by_name["Point"]
_POLYLINE = DESCRIPTOR.message_types_by_name["Polyline"]
_ROADLANE = DESCRIPTOR.message_types_by_name["RoadLane"]
_ROADAREA = DESCRIPTOR.message_types_by_name["RoadArea"]
_PEDCROSSWALK = DESCRIPTOR.message_types_by_name["PedCrosswalk"]
_PEDWALKWAY = DESCRIPTOR.message_types_by_name["PedWalkway"]
VectorizedMap = _reflection.GeneratedProtocolMessageType(
    "VectorizedMap",
    (_message.Message,),
    {
        "DESCRIPTOR": _VECTORIZEDMAP,
        "__module__": "vectorized_map_pb2"
        # @@protoc_insertion_point(class_scope:trajdata.VectorizedMap)
    },
)
_sym_db.RegisterMessage(VectorizedMap)

MapElement = _reflection.GeneratedProtocolMessageType(
    "MapElement",
    (_message.Message,),
    {
        "DESCRIPTOR": _MAPELEMENT,
        "__module__": "vectorized_map_pb2"
        # @@protoc_insertion_point(class_scope:trajdata.MapElement)
    },
)
_sym_db.RegisterMessage(MapElement)

Point = _reflection.GeneratedProtocolMessageType(
    "Point",
    (_message.Message,),
    {
        "DESCRIPTOR": _POINT,
        "__module__": "vectorized_map_pb2"
        # @@protoc_insertion_point(class_scope:trajdata.Point)
    },
)
_sym_db.RegisterMessage(Point)

Polyline = _reflection.GeneratedProtocolMessageType(
    "Polyline",
    (_message.Message,),
    {
        "DESCRIPTOR": _POLYLINE,
        "__module__": "vectorized_map_pb2"
        # @@protoc_insertion_point(class_scope:trajdata.Polyline)
    },
)
_sym_db.RegisterMessage(Polyline)

RoadLane = _reflection.GeneratedProtocolMessageType(
    "RoadLane",
    (_message.Message,),
    {
        "DESCRIPTOR": _ROADLANE,
        "__module__": "vectorized_map_pb2"
        # @@protoc_insertion_point(class_scope:trajdata.RoadLane)
    },
)
_sym_db.RegisterMessage(RoadLane)

RoadArea = _reflection.GeneratedProtocolMessageType(
    "RoadArea",
    (_message.Message,),
    {
        "DESCRIPTOR": _ROADAREA,
        "__module__": "vectorized_map_pb2"
        # @@protoc_insertion_point(class_scope:trajdata.RoadArea)
    },
)
_sym_db.RegisterMessage(RoadArea)

PedCrosswalk = _reflection.GeneratedProtocolMessageType(
    "PedCrosswalk",
    (_message.Message,),
    {
        "DESCRIPTOR": _PEDCROSSWALK,
        "__module__": "vectorized_map_pb2"
        # @@protoc_insertion_point(class_scope:trajdata.PedCrosswalk)
    },
)
_sym_db.RegisterMessage(PedCrosswalk)

PedWalkway = _reflection.GeneratedProtocolMessageType(
    "PedWalkway",
    (_message.Message,),
    {
        "DESCRIPTOR": _PEDWALKWAY,
        "__module__": "vectorized_map_pb2"
        # @@protoc_insertion_point(class_scope:trajdata.PedWalkway)
    },
)
_sym_db.RegisterMessage(PedWalkway)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _VECTORIZEDMAP._serialized_start = 35
    _VECTORIZEDMAP._serialized_end = 211
    _MAPELEMENT._serialized_start = 214
    _MAPELEMENT._serialized_end = 430
    _POINT._serialized_start = 432
    _POINT._serialized_end = 472
    _POLYLINE._serialized_start = 474
    _POLYLINE._serialized_end = 544
    _ROADLANE._serialized_start = 547
    _ROADLANE._serialized_end = 827
    _ROADAREA._serialized_start = 829
    _ROADAREA._serialized_end = 929
    _PEDCROSSWALK._serialized_start = 931
    _PEDCROSSWALK._serialized_end = 982
    _PEDWALKWAY._serialized_start = 984
    _PEDWALKWAY._serialized_end = 1033
# @@protoc_insertion_point(module_scope)
