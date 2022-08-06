#parking lot
class ParkingLot:
  def __init__(self, parking_spaces):
    self.total_slots = parking_spaces
    self.available_slots = parking_spaces

  def park(self):
    pass

  def remove_car(self):
    pass

  def get_slots(self):
    return self.available_slots

  def is_full(self):
    return self.available_slots == 0
