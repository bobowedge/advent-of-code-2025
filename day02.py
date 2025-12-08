def invalid_id_single_length(id_str, length=2):
    if length == 1:
        return len(set(id_str)) == 1
    len_id = len(id_str) 
    if len_id % length != 0:
        return False
    repeat = id_str[:len_id//length] * length
    return id_str == repeat

def invalid_id(id):
    id_str = str(id)
    len_id = len(id_str)
    for length in range(1, len_id//2 + 1):
        if invalid_id_single_length(id_str, length):
            return True
    return False

def solution1(data):
    total = 0
    for ids in data:
        start, end = ids.split("-")
        for id in range(int(start), int(end) + 1):
            if invalid_id_single_length(str(id)):
                total += id
    return total

def solution2(data):
    total = 0
    for ids in data:
        start, end = ids.split("-")
        for id in range(int(start), int(end) + 1):
            if invalid_id(id):
                total += id
    return total

test_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".split(",")
data = open("day02.txt").read().split(",")

assert solution1(test_data) == 1227775554
print(f"Solution 1: {solution1(data)}")
assert solution2(test_data) == 4174379265
print(f"Solution 2: {solution2(data)}")
