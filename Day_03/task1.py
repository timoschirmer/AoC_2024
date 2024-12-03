import re

file = open('input', 'r')

list = [str(line).rstrip('\n') for line in file]

allNumbers = []

for line in list:
    mulList = []
    mulList = re.findall(r'mul\(\d{1,3},\d{1,3}\)',line)
    for mul in mulList:
        numbers = re.findall(r'\d+', mul)
        allNumbers.append(int(numbers[0]) * int(numbers[1]))

result = sum(allNumbers)

print(result) 