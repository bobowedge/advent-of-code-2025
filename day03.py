def joltage(line, digits_left=12):
    if digits_left == 1:
        return max(int(x) for x in line)
    digits_left -= 1
    digit = max(int(x) for x in line[:-digits_left])
    new_start = line.find(str(digit)) + 1
    return digit*10**(digits_left) + joltage(line[new_start:], digits_left)

def solution1(data):
    return sum(joltage(line, digits_left=2) for line in data)

def solution2(data):
    return sum(joltage(line, digits_left=12) for line in data)

test_data = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
data = open("day03.txt").read().splitlines()

assert solution1(test_data) == 357
print(f"Solution 1: {solution1(data)}")
assert solution2(test_data) == 3121910778619
print(f"Solution 2: {solution2(data)}")
