from collections import Counter

def solution1(data):
    beams = set()
    beams.add(data[0].find('S'))
    splittings = 0
    for line in data[1:]:
        new_beams = set()
        for beam in beams:
            if line[beam] == '^':
                new_beams.add(beam-1)
                new_beams.add(beam+1)
                splittings += 1
            else:
                new_beams.add(beam)
        beams = set(new_beams)
    return splittings

def solution2(data):
    beams = Counter()
    beams[data[0].find('S')] += 1
    for line in data[1:]:
        new_beams = Counter()
        for beam, counter in beams.items():
            if line[beam] == '^':
                new_beams[beam-1] += counter
                new_beams[beam+1] += counter
            else:
                new_beams[beam] += counter
        beams = Counter(new_beams)
    return new_beams.total()


test_data = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""".splitlines()
data = open("day07.txt").read().splitlines()

assert solution1(test_data) == 21
print(f"Solution 1: {solution1(data)}")
assert solution2(test_data) == 40
print(f"Solution 2: {solution2(data)}")