import random


def getNumbersArray(length):
    array = []
    while(len(array) < length):
        array.append(int(input("Enter a number: ")))
    return array


def printArray(array):
    print(*array, sep=", ")
    return


def getArrayMin(array):
    array.sort()
    return array[0]


def getArrayMax(array):
    array.sort()
    return array[len(array) - 1]


def getArrayAverage(array):
    return sum(array) / len(array)


def getArrayMode(array):
    modeArray = [[0, 0]]
    for numberToTest in array:
        frequency = 0
        for entry in array:
            if int(entry) == int(numberToTest):
                frequency = frequency + 1
        print(f"found {numberToTest} {frequency} times")
        if frequency > modeArray[0][1]:
            modeArray = [[numberToTest, frequency]]
        elif frequency == modeArray[0][1]:
            newNumber = True
            for pair in modeArray:
                if numberToTest == pair[0]:
                    newNumber = False
            if newNumber:
                modeArray.append([numberToTest, frequency])
    modeFrequency = modeArray[0][1]
    if len(modeArray) == 1:
        mode = str(modeArray[0][0]) + " "
    else:
        mode = ""
        for pair in modeArray:
            mode += f"{pair[0]}, "
    return f"{mode}at {modeFrequency} occurances"


def arrayStats():
    numbersArray = getNumbersArray(10)
    print(
        f"You entered the array:"
    )
    printArray(numbersArray)
    print(
        f"The minimum is {getArrayMin(numbersArray)} \n"
        f"The maximum is {getArrayMax(numbersArray)} \n"
        f"The mode is {getArrayMode(numbersArray)} \n"
        f"The average is {getArrayAverage(numbersArray)}"
    )
    return


arrayStats()

