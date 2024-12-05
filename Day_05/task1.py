import re

file = open('input', 'r')

lines = [str(line).rstrip('\n') for line in file]

rules = lines[:lines.index("")]
updates = lines[lines.index("") + 1:]

rules = [re.findall(r'\d+', rule) for rule in rules]
updates = [re.findall(r'\d+', update) for update in updates]

correctUpdates = []
middlePages = []

for update in updates:
    valid = True
    for rule in rules:
        try:
            before = update.index(rule[0])
            after = update.index(rule[1])
        except:
            pass
        else:
            if before > after:
                valid = False
    if valid:
        correctUpdates.append(update)

for update in correctUpdates:
    middlePages.append(int(update[int((len(update) - 1) / 2)]))

result = sum(middlePages)

print(result)