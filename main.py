import sys

fileName = str(sys.argv[1])
wMinFilled = int(sys.argv[2])
wPref = int(sys.argv[3])
wPair = int(sys.argv[4])
wSecDiff = int(sys.argv[5])
penPracticeMin = int(sys.argv[6])
penPracticeMax = int(sys.argv[7])
penNotPaired = int(sys.argv[8])
penSection = int(sys.argv[9])


gameSlots = []
practiceSlots = []
games = []
practices = []
notCompatible = []
unwanted = []
preferences = []
pair = []
partialAssign = []


def readInputFile(fileName):
    inputFile = open(fileName, 'r')    # Open input file

    while(True):

        line = inputFile.readline()

        if "Game slots:" in line:
            headerData(line, inputFile, gameSlots)

        if "Practice slots:" in line:
            headerData(line, inputFile, practiceSlots)

        if "Games:" in line:
            headerData(line, inputFile, games)

        if "Practices:" in line:
            headerData(line, inputFile, practices)

        if "Not compatible:" in line:
            headerData(line, inputFile, notCompatible)

        if "Unwanted:" in line:
            headerData(line, inputFile, unwanted)

        if "Preferences:" in line:
            headerData(line, inputFile, preferences)

        if "Pair:" in line:
            headerData(line, inputFile, pair)

        if "Partial assignments:" in line:
            headerData(line, inputFile, partialAssign)
            break

    inputFile.close()
    

def headerData (line, inputFile, arr):

        line = inputFile.readline()
        while(line.strip() != ""):
            temp = [x for x in line.strip().split(', ')]
            arr.append(temp)
            line = inputFile.readline()


# Just to check
readInputFile(fileName)

print("Game Slots: ", gameSlots)
print("Practice Slots: ", practiceSlots)
print("Games: ", games)
print("Practices: ", practices)
print("Not Compatible: ", notCompatible)
print("Unwanted: ", unwanted)
print("Preferences:", preferences)
print("Pair: ", pair)
print("Partial Assignments: ", partialAssign)