# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TripUpdate.proto

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
  name='TripUpdate.proto',
  package='tutorial',
  syntax='proto2',
  serialized_pb=_b('\n\x10TripUpdate.proto\x12\x08tutorial\"\xdb\x02\n\x07Vehicle\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nvehicle_id\x18\x02 \x01(\x05\x12\x16\n\x0e\x63urrent_status\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x0f\n\x07stop_id\x18\x05 \x01(\t\x12$\n\x04trip\x18\x06 \x03(\x0b\x32\x16.tutorial.Vehicle.Trip\x12,\n\x08position\x18\x07 \x03(\x0b\x32\x1a.tutorial.Vehicle.Position\x1a^\n\x04Trip\x12\x0f\n\x07trip_id\x18\x01 \x01(\t\x12\x1d\n\x15schedule_relationship\x18\x02 \x01(\t\x12\x10\n\x08route_id\x18\x03 \x02(\t\x12\x14\n\x0c\x64irection_id\x18\x04 \x01(\t\x1a@\n\x08Position\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x0f\n\x07\x62\x65\x61ring\x18\x03 \x01(\t\".\n\x08Vehicles\x12\"\n\x07vehicle\x18\x01 \x03(\x0b\x32\x11.tutorial.Vehicle')
)




_VEHICLE_TRIP = _descriptor.Descriptor(
  name='Trip',
  full_name='tutorial.Vehicle.Trip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trip_id', full_name='tutorial.Vehicle.Trip.trip_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='schedule_relationship', full_name='tutorial.Vehicle.Trip.schedule_relationship', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_id', full_name='tutorial.Vehicle.Trip.route_id', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction_id', full_name='tutorial.Vehicle.Trip.direction_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=312,
)

_VEHICLE_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='tutorial.Vehicle.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='tutorial.Vehicle.Position.latitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='tutorial.Vehicle.Position.longitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bearing', full_name='tutorial.Vehicle.Position.bearing', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=378,
)

_VEHICLE = _descriptor.Descriptor(
  name='Vehicle',
  full_name='tutorial.Vehicle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tutorial.Vehicle.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vehicle_id', full_name='tutorial.Vehicle.vehicle_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_status', full_name='tutorial.Vehicle.current_status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='tutorial.Vehicle.timestamp', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop_id', full_name='tutorial.Vehicle.stop_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trip', full_name='tutorial.Vehicle.trip', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='tutorial.Vehicle.position', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VEHICLE_TRIP, _VEHICLE_POSITION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=378,
)


_VEHICLES = _descriptor.Descriptor(
  name='Vehicles',
  full_name='tutorial.Vehicles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vehicle', full_name='tutorial.Vehicles.vehicle', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=426,
)

_VEHICLE_TRIP.containing_type = _VEHICLE
_VEHICLE_POSITION.containing_type = _VEHICLE
_VEHICLE.fields_by_name['trip'].message_type = _VEHICLE_TRIP
_VEHICLE.fields_by_name['position'].message_type = _VEHICLE_POSITION
_VEHICLES.fields_by_name['vehicle'].message_type = _VEHICLE
DESCRIPTOR.message_types_by_name['Vehicle'] = _VEHICLE
DESCRIPTOR.message_types_by_name['Vehicles'] = _VEHICLES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vehicle = _reflection.GeneratedProtocolMessageType('Vehicle', (_message.Message,), dict(

  Trip = _reflection.GeneratedProtocolMessageType('Trip', (_message.Message,), dict(
    DESCRIPTOR = _VEHICLE_TRIP,
    __module__ = 'TripUpdate_pb2'
    # @@protoc_insertion_point(class_scope:tutorial.Vehicle.Trip)
    ))
  ,

  Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), dict(
    DESCRIPTOR = _VEHICLE_POSITION,
    __module__ = 'TripUpdate_pb2'
    # @@protoc_insertion_point(class_scope:tutorial.Vehicle.Position)
    ))
  ,
  DESCRIPTOR = _VEHICLE,
  __module__ = 'TripUpdate_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Vehicle)
  ))
_sym_db.RegisterMessage(Vehicle)
_sym_db.RegisterMessage(Vehicle.Trip)
_sym_db.RegisterMessage(Vehicle.Position)

Vehicles = _reflection.GeneratedProtocolMessageType('Vehicles', (_message.Message,), dict(
  DESCRIPTOR = _VEHICLES,
  __module__ = 'TripUpdate_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Vehicles)
  ))
_sym_db.RegisterMessage(Vehicles)


# @@protoc_insertion_point(module_scope)
