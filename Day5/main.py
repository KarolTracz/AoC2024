import random
import re

with open('input.txt', 'r') as f:
# with open('input_test.txt', 'r') as f:
    raw_input = f.read()

rules_raw = re.findall("[0-9]{2}\|[0-9]{2}", raw_input)
updates_raw = re.findall("(([0-9]{2},)+[0-9]{2})", raw_input)

rules=[]
updates=[]
valid = []
not_valid = []
not_valid_changed = []

for match in rules_raw:
    x, y = match.split("|")
    rules.append([int(x), int(y)])
for match in updates_raw:
    updates.append([int(i) for i in match[0].split(',')])

# print(f'{updates_raw=}')
def first_star():
    result = 0

    for update in updates:
        if is_valid(update):
            valid.append(update)
        else:
            not_valid.append(update)

    for i in valid:
        result += i[len(i)//2]

    print(f'{result=}')
    return result

def is_valid(input: list[int]) -> bool:
    for i in input:
        for rule in rules:
            if i == rule[0]:
                try:
                    if input.index(rule[1]) < input.index(i):
                        return False
                except ValueError:
                    pass
    return True


def is_valid_with_rules(input: list[int]) -> list[bool, [int]]:
    for i in input:
        for rule in rules:
            if i == rule[0]:
                try:
                    if input.index(rule[1]) < input.index(i):
                        return [False, rule]
                except ValueError:
                    pass
    return [True, []]
def second_star():
    result = 0

    while True:
        for update in not_valid:
            if not is_valid_with_rules(update)[0]:
                a, b = is_valid_with_rules(update)[1]
                idx_a, idx_b = update.index(b), update.index(a)
                update[idx_a], update[idx_b] = update[idx_b], update[idx_a]
                if is_valid(update):
                    not_valid_changed.append(update)
                    not_valid.pop(not_valid.index(update))
        if not_valid == []:
            break

    for i in not_valid_changed:
        result += i[len(i)//2]

    print(f'{result=}')
    return result

if __name__ == '__main__':
    first_star()
    print(f'{rules=}')
    print(f'{updates=}')
    second_star()
