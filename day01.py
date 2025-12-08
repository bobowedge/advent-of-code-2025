def solution1(data):
    count = 0
    position = 50
    for line in data:
        if not line:
            continue
        if line[0] == "R":
            position += int(line[1:])
        if line[0] == "L":
            position -= int(line[1:])
        position %= 100
        if position == 0:
            count += 1
    return count

def solution2(data):
    count = 0
    position = 50
    for line in data:
        if not line:
            continue
        value = int(line[1:])
        if line[0] == "R":
            position += value
            while position >= 100:
                position -= 100
                count += 1
        if line[0] == "L":
            if position == 0:
                position += 100
            position -= value
            while position <= 0:
                position += 100
                count += 1
            if position == 100:
                position = 0
        print(line, position, count)
    return count

test_data = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".splitlines()
assert solution1(test_data) == 3
assert solution2(test_data) == 6
data = open("day01.txt").read().splitlines()
print(f"Solution 1: {solution1(data)}")
print(f"Solution 2: {solution2(data)}")