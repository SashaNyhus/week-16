import dogData
import random


class Dog:

    def __init__(self, manualInput=False):
        if manualInput:
            print("leave any field blank to randomize")
        self.name = self.getTrait("name", manualInput)
        self.surname = self.getTrait("surname", manualInput)
        self.fullName = f"{self.name} {self.surname}"
        self.weight = self.getTrait("weight", manualInput)
        self.breed = self.getTrait("breed", manualInput)
        self.age = self.getTrait("age", manualInput)
        self.color = self.getTrait("color", manualInput)
        self.condition = self.getTrait("condition", manualInput)

    def getTrait(self, traitName, manualInput):
        newTrait = ""
        if manualInput:
            newTrait = self.inputTrait(traitName)
        if newTrait == "":
            if traitName == "weight":
                newTrait = random.randrange(3, 100)
            elif traitName == "age":
                newTrait = random.randrange(1, 17)
            else:
                newTrait = self.getRandomTrait(traitName)
        return newTrait

    def inputTrait(self, trait):
        trait = input(f"Enter the {trait} of the dog: ")
        return trait
        
    def getRandomTrait(self, traitName):
        if traitName == "name":
            traitName = random.choice(["maleName", "femaleName"])
        randomTrait = random.choice(getattr(dogData, traitName))
        return randomTrait

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
    random = input("random dog? y/n")
    if random == "y":
        newDog = Dog()
    else:
        newDog = Dog(True)
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
        print(f"{index + 1}. " + dogEntry.fullName)
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
