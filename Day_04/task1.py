import re

file = open('input', 'r')

lines = [str(line).rstrip('\n') for line in file]


# Get horizontal

horizontal = 0

for line in lines:
    XMAS = re.findall(r'XMAS', line)
    SAMX = re.findall(r'SAMX', line)
    horizontal = horizontal + len(XMAS) + len(SAMX)

# print(horizontal)


array = []

for line in lines:
    lineList = []
    for char in line:
        lineList.append(char)
    array.append(lineList)

# for index, line in enumerate(array):
#     print(index)
#     print(line)

# Get diagonal and vertical

finds = []

for iLine, line in enumerate(array):
    for iChar, char in enumerate(line):
        if iLine <= (len(array) - 4):
            # links -> rechts
            if iChar <= (len(line) - 4):
                if char == "X":
                    # Vorwärts
                    if array[(iLine + 1)][iChar + 1] == "M":
                        if array[(iLine + 2)][iChar + 2] == "A":
                            if array[(iLine + 3)][iChar + 3] == "S":
                                finds.append("LRv --> (" + str(iLine) + ", " + str(iChar) + ")")
                elif char == "S":
                    # Rückwärts
                    if array[(iLine + 1)][iChar + 1] == "A":
                        if array[(iLine + 2)][iChar + 2] == "M":
                            if array[(iLine + 3)][iChar + 3] == "X":
                                finds.append("LRr --> (" + str(iLine) + ", " + str(iChar) + ")")
            # rechts -> links
            if iChar >= 3:
                if char == "X":
                    # Vorwärts
                    if array[(iLine + 1)][iChar - 1] == "M":
                        if array[(iLine + 2)][iChar - 2] == "A":
                            if array[(iLine + 3)][iChar - 3] == "S":
                                finds.append("RLv --> (" + str(iLine) + ", " + str(iChar) + ")")
                elif char == "S":
                    # Rückwärts
                    if array[(iLine + 1)][iChar - 1] == "A":
                        if array[(iLine + 2)][iChar - 2] == "M":
                            if array[(iLine + 3)][iChar - 3] == "X":
                                finds.append("RLr --> (" + str(iLine) + ", " + str(iChar) + ")")
            # vertical XMAS
            if char == "X":
                if array[(iLine + 1)][iChar] == "M":
                    if array[(iLine + 2)][iChar] == "A":
                        if array[(iLine + 3)][iChar] == "S":
                            finds.append("Vv --> (" + str(iLine) + ", " + str(iChar) + ")")
            if char == "S":
                if array[(iLine + 1)][iChar] == "A":
                    if array[(iLine + 2)][iChar] == "M":
                        if array[(iLine + 3)][iChar] == "X":
                            finds.append("Vr --> (" + str(iLine) + ", " + str(iChar) + ")")

diagonal = len(finds)

print(horizontal + diagonal)