import pytest
from rent.domain.room import Room
from rent.repository.memrepo import MemRepo
@pytest.fixture 
def room_dicts():
    return [ {
    "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a", "size": 215,
    "price": 39,
    "longitude": -0.09998975,
    "latitude": 51.75436293, },
    {
    "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a", "size": 405,
    "price": 66,
    "longitude": 0.18228006,
    "latitude": 51.74640997,
    }, {
    "latitude": 51.45994069, },
    {
    "code": "eed76e77-55c1-41ce-985d-ca49bf6c0585", "size": 93,
    "price": 48,
    "longitude": 0.33894476,
    "latitude": 51.39916678,
    }, ]

def test_repository_list_without_parameters(room_dicts): 
    repo = MemRepo(room_dicts)
    rooms = [Room.from_dict(i) for i in room_dicts]
    assert repo.list() == rooms
