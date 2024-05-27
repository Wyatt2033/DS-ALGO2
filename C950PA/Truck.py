# Class for Truck Object
class Truck:

    # Creates truck object,
    def __init__(self, capacity, speed, packages, mileage, address, time, start_time):
        self.capacity = capacity
        self.speed = speed
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.time = time
        self.start_time = start_time

    # Retruns string truck object.
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (
            self.capacity, self.speed, self.packages, self.mileage, self.address, self.time, self.start_time)
