def find_rolls(data):
    rolls = set()
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "@":
                rolls.add((row, col))
    return rolls

def accessible(roll, rolls):
    count = 0
    for row in range(roll[0]-1, roll[0]+2):
        for col in range(roll[1]-1, roll[1]+2):
            if (row, col) in rolls:
                count += 1
    return count <= 4

def solution1(data):
    rolls = find_rolls(data)
    return sum(1 for roll in rolls if accessible(roll, rolls))

def solution2(data):
    rolls = find_rolls(data)
    total = len(rolls)
    while True:
        new_rolls = set()
        for roll in rolls:
            if not accessible(roll, rolls):
                new_rolls.add(roll)
        if new_rolls == rolls:
            break
        rolls = new_rolls
    return total - len(rolls)

test_data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".splitlines()
data = open("day04.txt").read().splitlines()

assert solution1(test_data) == 13
print(f"Solution 1: {solution1(data)}")
assert solution2(test_data) == 43
print(f"Solution 2: {solution2(data)}")