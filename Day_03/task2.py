import re

file = open('input', 'r')

list = [str(line).rstrip('\n') for line in file]

allNumbers = []
filteredList =[]
do = True

for line in list:
    tempList = re.split(r'(do\(\)|don\'t\(\))', line)
    for item in tempList:
        if item == "do()":
            do = True
        elif item == "don't()":
            do = False
        else:
            if do:
                filteredList.append(item)


for line in filteredList:
    mulList = []
    mulList = re.findall(r'mul\(\d{1,3},\d{1,3}\)',line)
    for mul in mulList:
        numbers = re.findall(r'\d+', mul)
        allNumbers.append(int(numbers[0]) * int(numbers[1]))

result = sum(allNumbers)

print(result) 