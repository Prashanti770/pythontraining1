class Bus:
    def travel(self):
        print("moves on road")
    def fuel(self):
        print("needs diesel")

class Ship:
    def travel(self):
        print("moves on water")

    def fuel(self):
        print("needs Heavy Fuel Oil")

#common interface

def transport(vehicle):
    vehicle.travel()

indra = Bus()
titanic = Ship()

transport(indra)
transport(titanic)
