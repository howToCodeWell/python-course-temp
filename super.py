# Micro Python only calls one class that is inherited


class Vehicle:
    def __init__(self):
        print("This is a Vehicle")


class Car(Vehicle):
    def __init__(self):
        print("This is a Car")
        super().__init__()


class Boat(Vehicle):
    def __init__(self):
        print("This is a Boat")
        super().__init__()


class Racer(Car, Boat):
    def __init__(self):
        print("This is a Racer")
        super().__init__()


Racer()

