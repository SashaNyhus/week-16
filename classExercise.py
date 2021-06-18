class SkodaCar:
    make = "Skoda"

    def __init__(self, doors, wd, color, cylinders):
        self.doors = doors
        self.wd = wd
        self.color = color
        self.cylinders = cylinders

    def printInfo(self):
        print(
            f'This {self.color} {self.cylinders}-cylinder {self.make} car'
            f'has {self.wd}WD and {self.doors} doors'
        )


car1 = SkodaCar(4, 4, "blue", 6)
car2 = SkodaCar(2, 2, "black", 4)
car3 = SkodaCar(5, 2, "white", 4)

carArray = [car1, car2, car3]


def printCars(array):
    for car in array:
        car.printInfo()
    return


printCars(carArray)
