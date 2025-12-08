def is_fresh(ID, inventory):
    for low, high in inventory:
        if low <= ID <= high:
            return True
    return False


def solution1(data):
    inventory = set()
    fresh = 0
    for line in data:
        line = line.strip()
        if not line:
            continue
        if '-' in line:
            low, high = line.split("-")
            inventory.add((int(low), int(high)))
        else:
            ID = int(line)
            fresh += is_fresh(ID, inventory)
    return fresh

def solution2(data):
    fresh = []
    for line in data:
        line = line.strip()
        if not line:
            continue
        if '-' in line:
            low, high = line.split("-")
            fresh.append((int(low), int(high)))
    fresh.sort()
    idx = 0
    while idx < len(fresh) - 1:
        low1, high1 = fresh[idx]
        low2, high2 = fresh[idx + 1]
        if low1 <= low2 <= high1:
            high1 = max(high1, high2)
            fresh.pop(idx+1)
            fresh[idx] = (low1, high1)
        else:
            idx += 1
    return sum(high - low + 1 for low, high in fresh)

test_data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".splitlines()
data = open("day05.txt").read().splitlines()

assert solution1(test_data) == 3
print(f"Solution 1: {solution1(data)}")
assert solution2(test_data) == 14
print(f"Solution 2: {solution2(data)}")