
class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def display(self):
        print("max speed :", self.max_speed)

modelX = Vehicle(240, 18)
modelX.display()

print("Model Max Speed:", modelX.max_speed)
print("Model Mileage:", modelX.mileage)