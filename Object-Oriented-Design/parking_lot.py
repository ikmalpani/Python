# Design a parking lot.

class Vehicle():
  def __init__(self, license_plate):
    self.license_plate = license_plate

  def get_spots_needed():
    return self.spots_needed

  def get_size():
    return self.size

  def can_fit_in_spot():
    return True

class Car(Vehicle):
  def __init__(self, license_plate, spots_needed, size):
    super().__init__(license_plate)
    self.spots_needed= 1
    self.size = "compact"

class MotorCycle(Vehicle):
  def __init__(self, license_plate, spots_needed, size):
    super().__init__(license_plate)
    self.spots_needed = 1
    self.size = "motorcycle"

class Bus(Vehicle):
  def __init__(self, license_plate, spots_needed, size):
    super().__init__(license_plate)
    self.spots_needed = 5
    self.size = "large"

class ParkingLot(object):
  def __init__(self):
    self.compact_available = 0
    self.large_available = 10
    self.motorcycle_available = 10
    self.compact = {}
    self.motorcycle = {}
    self.large = {}

  def park():
    pass

  def unpark():
    pass

  def park_vehicle(self, vehicle):
    if vehicle.size == "compact":
      if self.compact_available > 0:
        self.compact[vehicle] = True 
        self.compact_available -= 1
        print("Car parcked in compact spot")
      elif self.compact_available == 0 and self.large_available > 0:
        self.large[vehicle] = True
        self.large_available -= 1
        print("Car parcked in large spot")
    elif vehicle.size == "motorcycle":
      self.motorcycle[vehicle] = True 
      self.motorcycle_available -= 1
      print("Motorcycle parcked in motorcycle spot")
    elif vehicle.size == "large" and self.large_available > 4:
      self.large[vehicle] = True
      self.large_available -= 5
      print("Bus parcked in 5 large spots.")
    else: print("No spots available.")
    
  
  def unpark_vehicle(self, vehicle):
    if vehicle.size == "compact":
      if vehicle in self.compact:
        del self.compact[vehicle]
      elif vehicle in self.large:
        del self.large[vehicle]
    elif vehicle.size == "motorcycle":
      del self.motorcycle[vehicle]
    elif vehicle.size == "large":
      del self.large[vehicle]

import unittest

class Test(unittest.TestCase):
  def test_parking_lot(self):
    motorcycle1 = MotorCycle("676", 1, "motorcycle")
    car1 = Car("123", 1, "compact")
    bus1 = Bus("122", 5, "large")
    bus2 = Bus("422", 5, "large")
    lot = ParkingLot()
    lot.park_vehicle(car1)
    lot.park_vehicle(bus1)
    lot.park_vehicle(bus2)
    lot.park_vehicle(motorcycle1)
    lot.unpark_vehicle(car1)
    lot.unpark_vehicle(motorcycle1)
    print(lot.compact_available)
    print(lot.motorcycle_available)
    print(lot.large_available)
    self.assertEqual(len(lot.large), 1)

if __name__ == "__main__":
  unittest.main()