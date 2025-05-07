import re

# with open('input_test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    raw_input = f.read()

regex = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
matches = re.findall(regex, raw_input)


def first_star():
    result = 0
    for match in matches:
        x, y = int(match[0]), int(match[1])
        result += x*y
        print(f"First number: {x}, Second number: {y}")
    print(f'{result=}')
    return result


def second_star():
    result = 0
    in_do_block = True

    for match in matches:
        full_match = match[0]

        if full_match == "do()":
            in_do_block = True
        elif full_match == "don't()":
            in_do_block = False
        elif "mul" in full_match and in_do_block:
            x, y = int(match[1]), int(match[2])
            result += x * y
    print(f'{result=}')
    return result


if __name__ == '__main__':
    first_star()
    regex = r"(do\(\)|don't\(\)|mul\(([0-9]{1,3}),([0-9]{1,3})\))"
    matches = re.findall(regex, raw_input)
    second_star()