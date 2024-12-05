import re

file = open('input', 'r')

lines = [str(line).rstrip('\n') for line in file]

rules = lines[:lines.index("")]
updates = lines[lines.index("") + 1:]

rules = [re.findall(r'\d+', rule) for rule in rules]
updates = [re.findall(r'\d+', update) for update in updates]

incorrectUpdates = []
correctedUpdates = []
middlePages = []


def verifyRule(update, rule):
    try:
        before = update.index(rule[0])
        after = update.index(rule[1])
    except:
        pass
    else:
        if before > after:
            return False
    return True

def verifyRules(update):
    valid = True
    for rule in rules:
        if not verifyRule(update, rule):
            valid = False
    return valid

def switchPages(update, rule):
    update.insert(update.index(rule[0]), rule[1])
    update.pop(update.index(rule[0]))
    update.insert(update.index(rule[1]), rule[0])
    update.pop(update.index(rule[1]))

for update in updates:
    valid = verifyRules(update)
    if not valid:
        incorrectUpdates.append(update)

for update in incorrectUpdates:
    while not verifyRules(update):
        for rule in rules:
            while not verifyRule(update, rule):
                switchPages(update, rule)


for update in incorrectUpdates:
    middlePages.append(int(update[int((len(update) - 1) / 2)]))

result = sum(middlePages)

print(result)