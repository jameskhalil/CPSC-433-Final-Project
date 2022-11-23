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

# def file_Parser(fileName):
#     myfile = open(fileName, 'r')    # Open input file

#     while(True):

#         temp = []

#         line = myfile.readline()

#         if "Game slots:" in line:
#             line = myfile.readline()
#             while(line.strip() != ""):
#                 temp = [x for x in line.strip().split(', ')]
#                 gameSlots.append(temp)
#                 line = myfile.readline()
        
#         if "Practice slots:" in line:
#             line = myfile.readline()
#             while(line.strip() != ""):
#                 temp = [x for x in line.strip().split(', ')]
#                 practiceSlots.append(temp)
#                 line = myfile.readline()
            
#         if "Games:" in line:
#             line = myfile.readline()
#             while(line.strip() != ""):
#                 temp = [x for x in line.strip().split(', ')]
#                 games.append(temp)
#                 line = myfile.readline()
            
#         if "Practices:" in line:
#             line = myfile.readline()
#             while(line.strip() != ""):
#                 temp = [x for x in line.strip().split(', ')]
#                 practices.append(temp)
#                 line = myfile.readline()

#         if "Not compatible:" in line:
#             line = myfile.readline()
#             while(line.strip() != ""):
#                 temp = [x for x in line.strip().split(', ')]
#                 notCompatible.append(temp)
#                 line = myfile.readline()

#         if "Unwanted:" in line:
#             line = myfile.readline()
#             while(line.strip() != ""):
#                 temp = [x for x in line.strip().split(', ')]
#                 unwanted.append(temp)
#                 line = myfile.readline()
        
#         if "Preferences:" in line:
#             line = myfile.readline()
#             while(line.strip() != ""):
#                 temp = [x for x in line.strip().split(', ')]
#                 preferences.append(temp)
#                 line = myfile.readline()

#         if "Pair:" in line:
#             line = myfile.readline()
#             while(line.strip() != ""):
#                 temp = [x for x in line.strip().split(', ')]
#                 pair.append(temp)
#                 line = myfile.readline()
        
#         if "Partial assignments:" in line:
#             line = myfile.readline()
#             while(line.strip() != ""):
#                 temp = [x for x in line.strip().split(', ')]
#                 partialAssign.append(temp)
#                 line = myfile.readline()
#             break

#     myfile.close()


def readInputFile(fileName):
    myfile = open(fileName, 'r')    # Open input file

    while(True):

        line = myfile.readline()

        if "Game slots:" in line:
            headerData(line, myfile, "Game slots:", gameSlots)

        if "Practice slots:" in line:
            headerData(line, myfile, "Practice slots:", practiceSlots)

        if "Games:" in line:
            headerData(line, myfile, "Games:", games)

        if "Practices:" in line:
            headerData(line, myfile, "Pratices:", practices)

        if "Not compatible:" in line:
            headerData(line, myfile, "Not compatible:", notCompatible)

        if "Unwanted:" in line:
            headerData(line, myfile, "Unwanted:", unwanted)

        if "Preferences:" in line:
            headerData(line, myfile, "Preferences:", preferences)

        if "Pair:" in line:
            headerData(line, myfile, "Pair", pair)

        if "Partial assignments:" in line:
            headerData(line, myfile, "Partial assignments", partialAssign)
            break

    myfile.close()
    

def headerData (line, myfile, keyWord, arr):

    if keyWord in line:
        line = myfile.readline()
        while(line.strip() != ""):
            temp = [x for x in line.strip().split(', ')]
            arr.append(temp)
            line = myfile.readline()


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