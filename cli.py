#!/usr/bin/env python
from rent.repository.memrepo import MemRepo
from rent.use_cases.room_list import room_list_use_cases

rooms = [ {
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
repo = MemRepo(rooms)
result = room_list_use_cases(repo)

print([rooms.to_dict() for room in result])