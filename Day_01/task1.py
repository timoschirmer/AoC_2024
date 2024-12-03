file = open('input', 'r')

list = [str(line).rstrip('\n') for line in file]

listLeft = []
listRight = []
distance = []

for line in list:
    line = line.split()
    listLeft.append(int(line[0]))
    listRight.append(int(line[-1]))

listLeft.sort()
listRight.sort()

for index, id in enumerate(listLeft):
    distance.append(abs(id - listRight[index]))

totalDistance = sum(distance)

print(totalDistance)