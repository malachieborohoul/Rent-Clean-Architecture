import json
import uuid

from rent.serializers.room import RoomJsonEncoder
from rent.domain.room import Room


def test_serialize_domain_room():
    code = uuid.uuid4()
    room = Room(
        code,
        size=200,
        price=10,
        longitude=0.233443,
        latitude=0.233443,
    )


    expected_json= f"""
        {{
            "code":"{code}",
            "size":"200",
            "price":"10",
            "longitude"="0.233443",
            "latitude"="0.233443",
        }}
    """

    json_room = json.dumps(room,cls=RoomJsonEncoder)

    assert json.loads(json_room)== json.loads(expected_json)
