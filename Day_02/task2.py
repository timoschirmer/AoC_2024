file = open('input', 'r')

list = [str(line).rstrip('\n') for line in file]

def isIncreasing(list):
    return all(list[index] < list[index + 1] for index in range(len(list) - 1))

def isDecreasing(list):
    return all(list[index] > list[index + 1] for index in range(len(list) - 1))

def check(list):
    for index in range(len(list) - 1):
        if abs(list[index] - list[index + 1]) > 3:
            return False
    if isIncreasing(list) or isDecreasing(list):
        return True
    return False

def wildCheck(list):
    status = check(list)
    if status:
        return True
    else:
        backup = list.copy()
        for index in range(len(list)):
            list = backup.copy()
            list.pop(index)
            if check(list):
                return True
    return False

safeList = []

for report in list:
    report = report.split()
    for index, i in enumerate(report):
        report[index] = int(i)
    safeList.append(wildCheck(report))

print(safeList.count(True))