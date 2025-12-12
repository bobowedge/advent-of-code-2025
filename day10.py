from collections import Counter
from itertools import combinations, combinations_with_replacement as cwr, permutations, product
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import hermite_normal_form

def min_presses1(indicators, schematics):
    presses = 1
    while True:
        for combo in cwr(schematics, presses):
            counts = [0 for _ in range(len(indicators))]
            for buttons in combo:
                for button in buttons:
                    counts[button] += 1
            if all((count % 2 == 1) == indicator for count, indicator in zip(counts, indicators)):
                return presses
        presses += 1
    
def solution1(data):
    presses = 0
    for line in data:
        elements = line.split()
        indicators = []
        for indicator in elements[0][1:-1]:
            if indicator == '#':
                indicators.append(True)
            else:
                indicators.append(False)

        schematics = []
        for schematic in elements[1:-1]:
            buttons = [int(button) for button in schematic[1:-1].split(',')]
            schematics.append(buttons)

        
        presses += min_presses1(indicators, schematics)
    return presses


def calc_joltage(presses, schematics):
    jolts = Counter()
    for schematic, press in zip(schematics, presses):
        for button in schematic:
            jolts[button] += press
    return jolts

def min_presses2(schematics, joltages):
    lenj = len(joltages)
    lens = len(schematics)

    matrix = [[0 for _ in range(lens+1)] for _ in range(lenj)]
    for col, schematic in enumerate(schematics):
        for button in schematic:
            matrix[button][col] = 1
    for row, joltage in enumerate(joltages):
        matrix[row][-1] = joltage

    M = Matrix(matrix)
    Mref, pivot_cols = M.rref()

    reduced = [Mref[idx:idx+lens+1] for idx in range(0, (lens+1)*lenj, lens+1)]
    reduced.sort()
    while reduced[0] == [0] * (lens + 1):
        _ = reduced.pop(0)
    
    pivots = list(pivot_cols)
    pivots.sort(reverse=True)
    nonpivots = []
    ranges = []
    for var in list(range(lens)):
        if var in pivot_cols:
            continue        
        nonpivots.append(var)
        schematic = schematics[var]
        max_press = max([joltages[button] for button in schematic])
        ranges.append(range(max_press+1))

    min_presses = 123456789123456789
    for combo in product(*ranges):
        presses = [None for _ in range(lens)]
        for np, val in zip(nonpivots, combo):
            presses[np] = val
        for p, coeffs in zip(pivots, reduced):
            y = sum([coeffs[x] * presses[x] for x in range(p+1, lens)])
            presses[p] = (coeffs[-1] - y) // coeffs[p]
        if any(x < 0 for x in presses):
            continue
        jolts = calc_joltage(presses, schematics)
        test_joltages = tuple([jolts[x] for x in range(lenj)])
        if test_joltages == joltages:
            num_presses = sum(presses)
            min_presses = min(min_presses, num_presses)
    return min_presses

def solution2(data):
    presses = 0
    minp = 0
    for idx, line in enumerate(data):
        elements = line.split()
        schematics = []
        for schematic in elements[1:-1]:
            buttons = tuple(int(button) for button in schematic[1:-1].split(','))
            schematics.append(buttons)
        schematics = sorted(schematics, key=lambda x: len(x))
        joltages = tuple(int(x) for x in elements[-1][1:-1].split(','))        
        minp = min_presses2(schematics, joltages)
        presses += minp
    return presses
        

def solution2_test(data):
    presses = 0
    for idx, line in enumerate(data):
        elements = line.split()
        schematics = []
        for schematic in elements[1:-1]:
            buttons = tuple(int(button) for button in schematic[1:-1].split(','))
            schematics.append(buttons)
        joltages = tuple(int(x) for x in elements[-1][1:-1].split(','))
        idx_presses = min_presses2(joltages, schematics)
        presses += idx_presses
        print(idx, idx_presses)
    return presses


test_data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".splitlines()
data = open("day10.txt").read().splitlines()

assert solution1(test_data) == 7
print(f"Solution 1: {solution1(data)}")
assert solution2(test_data) == 33
print(f"Solution 2: {solution2(data)}")