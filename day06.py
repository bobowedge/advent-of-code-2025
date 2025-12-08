from math import prod

OPERATORS = {'+': sum,'*': prod}

def solution1(data):
    problems = []
    for line in data:
        problems.append(line.split())
    total = 0
    for problem in zip(*problems):
        oper = OPERATORS[problem[-1]]
        total += oper(map(int, problem[:-1]))
    return total

def solution2(data):
    numbers: list[str] = data[:-1]
    operations = data[-1].split()
    idx = 0
    total = 0
    while idx < len(numbers[0]):
        longest = 0
        num_length = 0
        for line in numbers:
            while idx + num_length < len(line) and line[idx+num_length] != " ":
                num_length += 1
            longest = max(num_length, longest)
        num_col = [tuple(line[idx:idx+longest]) for line in numbers]
        problem = []
        for digit_col in zip(*num_col):
            number = "".join(digit_col).strip()
            problem.append(int(number))
        oper = OPERATORS[operations.pop(0)]
        total += oper(problem)
        idx += longest + 1
    return total

test_data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """.splitlines()
data = open("day06.txt").read().splitlines()

assert solution1(test_data) == 4277556
print(f"Solution 1: {solution1(data)}")
assert solution2(test_data) == 3263827
print(f"Solution 2: {solution2(data)}")