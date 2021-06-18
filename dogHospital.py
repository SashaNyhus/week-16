import dogData
import random

class Dog:

    def __init__(self, firstName="", lastName="", weight="", breed="", age="", color="", condition=""):
        self.firstName = firstName or self.getRandomTrait("firstName")
        self.lastName = lastName or self.getRandomTrait("lastName")
        self.fullname = f"{self.firstName} {self.lastName}"
        self.weight = weight or random.randrange(3, 100)
        self.breed = breed or self.getRandomTrait("breed")
        self.age = age or random.randrange(1, 17)
        self.color = color or self.getRandomTrait("color")
        self.condition = condition or self.getRandomTrait("condition")

    def getRandomTrait(self, traitName):
        if traitName == "firstName":
            traitName = random.choice(["maleFirstName", "femaleFirstName"])
        randomTrait = random.choice(getattr(dogData, traitName))
        return randomTrait

    def printInfo(self):
        print(
            "PATIENT INFORMATION"
            f"Name: {self.fullname} \n"
            f"Weight: {self.weight} \n"
            f"Breed: {self.breed} \n"
            f"Age: {self.age} \n"
            f"Color: {self.color} \n"
            f"Condition: {self.condition}"
        )


def createRandomClass(className, sources):
    randomlySelected = []
    for array in sources:
        if array[0] == "range":
            randomProperty = random.randrange(*array[1:])
        else:
            randomProperty = random.choice(array)
        print(array)
        randomlySelected.append(randomProperty)
    newClass = className(*randomlySelected)
    return newClass


def createRandomDog():
    firstNames = random.choice([dogData.maleFirstNames, dogData.femaleFirstNames])
    data = [
        firstNames,
        dogData.lastNames,
        ["range", 3, 100],
        dogData.breeds,
        ["range", 1, 20],
        dogData.colors,
        dogData.conditions
    ]
    newDog = createRandomClass(Dog, data)
    return newDog


# def createRandomDog():
#     firstNames = random.choice([dogData.maleFirstNames, dogData.femaleFirstNames])
#     data = {
#         "firstNames": firstNames,
#         "lastNames": dogData.lastNames,
#         "weights": ["range", 3, 100],
#         "breeds": dogData.breeds,
#         "ages": ["range", .5, 20, .5],
#         "colors": dogData.colors,
#         "conditions": dogData.conditions
#     }
#     newDog = createRandomClass(Dog, data)
#     return newDog


def test():
    testDog = Dog()
    testDog.printInfo()
    return


test()