import sys
import re
import pandas as pd
import numpy as np

fileName = str(sys.argv[1])
wMinFilled = int(sys.argv[2])
wPref = int(sys.argv[3])
wPair = int(sys.argv[4])
wSecDiff = int(sys.argv[5])
penPracticeMin = int(sys.argv[6])
penPracticeMax = int(sys.argv[7])
penNotPaired = int(sys.argv[8])
penSection = int(sys.argv[9])

# rx_dict = {
#     'Game slots': re.compile('Game slots\n'),
#     'Practice slots': re.compile(r'Practice slots\n'),
#     'Games': re.compile(r'Games\n'),
#     'Practices': re.compile(r'Practices\n'),
#     'Not Compatible': re.compile(r'Not Compatible\n'),
#     'Unwanted': re.compile(r'Unwanted\n'),
#     'Preferences': re.compile(r'Preferences\n'),
#     'Pair': re.compile(r'Pair\n'),
#     'Partial Assignments': re.compile(r'Partial assignments\n')
# }


gameSlots = np.array([])
practiceSlots = np.array([])
games = []
practices = []
notCompatible = np.array([])
unwanted = np.array([])
preferences = np.array([])
pair = np.array([])
partialAssign = np.array([])


# def _parse_line(line):
#     """
#     Do a regex search against all defined regexes and
#     return the key and match result of the first matching regex

#     """

#     for key, rx in rx_dict.items():
#         match = rx.search(line)
#         print("here")

#         if match:
#             print("match")
#             return key, match
#     # if there are no matches
#     return None, None

def parse_file(filepath):

    with open(filepath, 'r') as file_object:

        for line in file_object.readlines():

        # line = file_object.readline()
        # while line:

            if 'Game slots:' in line:
                print("found")
                line = file_object.readline()
                line = file_object.readline()
                print(line)
                #     for i in line.split(","): 
                #         np.append(gameSlots,i)
            
            # key = _parse_line(line)

            # if key == 'Game slots':
        
            #     while line.strip():
            #         day, time, gameMax, gameMin = line.strip().split(',')
            #         np.append(gameSlots, [day, time, gameMax, gameMin])

            # if key == 'Practice slots':
            #     while line.strip():
            #         day, time, pracMax, pracMin = line.strip().split(',')
            #         np.append(practiceSlots, [day, time, pracMax, pracMin])

            # if key == 'Games':
            #     while line.strip():
            #         games.append(line)

            # if key == 'Practices':
            #     while line.strip():
            #         practices.append(line)

            # if key == 'Not compatible':
            #     while line.strip():
            #         identifier1, identifier2 = line.strip().split(',')
            #         np.append(notCompatible, [identifier1, identifier2])

            # if key == 'Unwanted':
            #     while line.strip():
            #         identifier, slotday, slottime = line.strip().split(',')
            #         np.append(unwanted, [identifier, slotday, slottime])

            # if key == 'Preferences':
            #     while line.strip():
            #         slotday, slottime, identifier, preferenceValue = line.strip().split(',')
            #         np.append(preferences, [slotday, slottime, identifier, preferenceValue])

            # if key == 'Pair':
            #     while line.strip():
            #         identifier1, identifier2 = line.strip().split(',')
            #         np.append(pair, [identifier1, identifier2])

            # if key == 'Partial assignments':
            #     while line.strip():
            #         identifier, slotday, slottime = line.strip().split(',')
            #         np.append(partialAssign, [identifier, slotday, slottime])

            #line = file_object.readline()

# myfile = open(fileName, 'r')    # Open input file

# fullStrData = str(myfile.read())    # Get data from file
 
# myfile.close()

# print(fullStrData)

parse_file(fileName)

print(gameSlots)
