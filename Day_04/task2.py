import re

file = open('input', 'r')

lines = [str(line).rstrip('\n') for line in file]

array = []

for line in lines:
    lineList = []
    for char in line:
        lineList.append(char)
    array.append(lineList)

# for index, line in enumerate(array):
#     print(index)
#     print(line)

# X-MAS

finds = []

for iLine, line in enumerate(array):
    for iChar, char in enumerate(line):
        match = {"M": 0, "S": 0}
        checkChar = ""
        if iLine <= (len(array) - 3) and iChar <= (len(line) - 3):
            print("---------")
            if char == "M" or char == "S": # Match oben links
                match.update({char: (match.get(char) + 1)})
                print("1. " + char + " --> (" + str(iLine) + ", " + str(iChar)  + ")")
                if array[iLine + 1][iChar + 1] == "A": # Match mitte
                    print("2. " + array[iLine + 1][iChar + 1] + " --> (" + str(iLine + 1) + ", " + str(iChar + 1)  + ")")
                    if array[iLine][iChar + 2] == "M" or array[iLine][iChar + 2] == "S": # Match oben rechts
                        print("3. " + array[iLine][iChar + 2] + " --> (" + str(iLine) + ", " + str(iChar + 2)  + ")")
                        match.update({array[iLine][iChar + 2]: (match.get(array[iLine][iChar + 2]) + 1)})
                        if array[iLine + 2][iChar + 2] == "M" or array[iLine + 2][iChar + 2] == "S": # Match unten rechts
                            print("4. " + array[iLine + 2][iChar + 2] + " --> (" + str(iLine + 2) + ", " + str(iChar + 2)  + ")")
                            match.update({array[iLine + 2][iChar + 2]: (match.get(array[iLine + 2][iChar + 2]) + 1)})
                            if array[iLine + 2][iChar] == "M" or array[iLine + 2][iChar] == "S": # Match unten links
                                print("5. " + array[iLine + 2][iChar] + " --> (" + str(iLine + 2) + ", " + str(iChar)  + ")")
                                match.update({array[iLine + 2][iChar]: (match.get(array[iLine + 2][iChar]) + 1)})
                                if match.get("M") == 2 and match.get("S") == 2 and char != array[iLine + 2][iChar + 2]:
                                    finds.append("Match --> (" + str(iLine) + ", " + str(iChar) + ")")
                        

for find in finds:
    print(find)

print(len(finds))        

# 2032 --> wrong