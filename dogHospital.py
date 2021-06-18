import dogData
import random

class Dog:

    def __init__(self, firstName="", lastName="", weight="", breed="", age="", color="", condition=""):
        self.firstName = firstName or self.getRandomTrait("firstName")
        self.lastName = lastName or self.getRandomTrait("lastName")
        self.fullName = f"{self.firstName} {self.lastName}"
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

    def printNameDisplay(self, index):
        print(f"{index}. {self.fullName}")

    def printInfo(self):
        print(
            "PATIENT INFORMATION \n"
            f"Name: {self.fullName} \n"
            f"Weight: {self.weight} \n"
            f"Breed: {self.breed} \n"
            f"Age: {self.age} \n"
            f"Color: {self.color} \n"
            f"Condition: {self.condition}"
        )

def getNewDog():
    newDogInfo = []
    def addTraitInput(trait):
        newDogInfo.append(input(trait))
        return
    random = input("random dog? y/n")
    if random == "y":
        newDog = Dog()
    else:
        print("leave any field blank to randomize")
        addTraitInput("First Name: ")
        addTraitInput("Last Name: ")
        addTraitInput("Weight: ")
        addTraitInput("Breed: ")
        addTraitInput("Age: ")
        addTraitInput("Color: ")
        addTraitInput("Condition: ")
        newDog = Dog(*newDogInfo)
    print("New patient added:")
    newDog.printInfo()
    return newDog
        

        



def initializeDogList():
    dogsList = []
    while(len(dogsList) < 5):
        dogsList.append(Dog())
    return dogsList


def printList(currentList):
    for index, dogEntry in enumerate(currentList):
        print(f"{int(index + 1)}. " + dogEntry.fullName)
    return


def main():
    dogs = initializeDogList()
    running = True
    while(running):
        print("Current Patients:")
        printList(dogs)
        mainChoice = int(input("enter a number to see full information or 0 to view other options"))
        if mainChoice == 0:
            subChoice = int(input("0 to add patient, 1 to return to dog list, 2 to close program"))
            if subChoice == 0:
                dogs.append(getNewDog())
            elif subChoice > 1:
                running = False
            continue
        else:
            dogs[mainChoice - 1].printInfo()
            continue
    return


main()