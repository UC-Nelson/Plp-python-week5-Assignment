
class Vehicle:
    def move(self):
        print("The vehicle moves")

class Car(Vehicle):
    def move(self):
        print("Driving my BMW")

class Plane(Vehicle):
    def move(self):
        print("Flying to Australia")

class Boat(Vehicle):
    def move(self):
        print("Sailing to Peru")

# Test the polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
