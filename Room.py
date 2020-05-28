class Room:
    def __init__(self, room_number, seating_capacity):
        self._room_number = room_number
        self._seating_capacity = seating_capacity

    def get_number(self): return self._room_number

    def get_seating_capacity(self): return self._seating_capacity
