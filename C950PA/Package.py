# Create package class.
class Package:

    # Creates package object.
    def __init__(self, ID, address, city, state, zip_code, deadline_time, weight, notes,  status, delivery_time):
        self.ID = ID
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.state = state
        self.deadline_time = deadline_time
        self.weight = weight
        self.notes = notes
        self.status = status
        self.delivery_time = delivery_time

    # Returns string package object.
    def __str__(self):
        return "%s. %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip_code, self.deadline_time, self.weight, self.notes, self.status, self.delivery_time)

    