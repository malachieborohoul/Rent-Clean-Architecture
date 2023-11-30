import json
import uuid

from rent.serializers.room import RoomJsonEncoder
from rent.domain.room import Room


def test_serialize_domain_room():
    code = uuid.uuid4()
    init_dict = Room(
        code,
        size=200,
        price=10,
        longitude=0.233443,
        latitude=0.233443,
    )