import uuid
from rent.domain.room import Room

def test_room_model_init():
    code = uuid.uuid4()
    init_dict = Room(
        code,
        size=200,
        price=10,
        longitude=0.233443,
        latitude=0.233443,
    )

    room1 = Room.from_dict(init_dict)
    room2 = Room.from_dict(init_dict)

    assert room1==room2
    # assert room.to_dict()==init_dict

    # assert room.code == code
    # assert room.size == 200
    # assert room.price == 10
    # assert room.longitudece == 0.2334430
    # assert room.latitude == 0.2334430