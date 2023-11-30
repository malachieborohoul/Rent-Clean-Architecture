import uuid
import dataclasses

@dataclasses
class Room:
    code = uuid.UUID
    size= int
    price = int
    longitude = float
    latitude = float