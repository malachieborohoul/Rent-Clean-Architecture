#!/usr/bin/env python
from rent.repository.memrepo import MemRepo
from rent.use_cases.room_list import room_list_use_cases

repo = MemRepo([])
result = room_list_use_cases(repo)