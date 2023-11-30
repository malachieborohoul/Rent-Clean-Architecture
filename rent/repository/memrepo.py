from rent.domain.room import Room

class MemRepo:
    def __init__(self,data):
        self.data= data

    def list(self):
        return [Room.form_dict(i) for i in self.data]