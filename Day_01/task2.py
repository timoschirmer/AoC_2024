file = open('input', 'r')

list = [str(line).rstrip('\n') for line in file]

listLeft = []
listRight = []
similarity = 0

for line in list:
    line = line.split()
    listLeft.append(int(line[0]))
    listRight.append(int(line[-1]))

for id in listLeft:
    similarity = similarity + (id * listRight.count(id))

print(similarity)