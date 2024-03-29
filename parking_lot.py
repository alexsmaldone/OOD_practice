#parking lot
class ParkingLot:
  def __init__(self, parking_spaces):
    self.total_slots = parking_spaces
    self.available_slots = parking_spaces

  def park(self):
    if not self.is_full():
      self.available_slots -= 1
    else:
      return f"Cannot park car in full lot."

  def remove_car(self):
    if not self.is_empty():
      self.available_slots += 1
    else:
      return f"Cannot remove car from empty parking lot."

  def get_slots(self):
    return self.available_slots

  def is_full(self):
    return self.available_slots == 0

  def is_empty(self):
    return self.available_slots == self.total_slots


newLot = ParkingLot(5)


print(newLot.park())
print(newLot.park())
print(newLot.park())
print(newLot.park())
print(newLot.park())
print(newLot.park())
print(newLot.remove_car())
print(newLot.remove_car())
print(newLot.remove_car())
print(newLot.remove_car())
print(newLot.remove_car())
print(newLot.remove_car())
print(newLot.get_slots())
