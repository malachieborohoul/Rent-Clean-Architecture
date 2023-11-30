import uuid
import dataclasses

@dataclasses
class Room:
    code = uuid.UUID
    size= int
    price = int
    longitude = float
    latitude = float

    @classmethod
    def from_dict(self, d):
        return self(**d)