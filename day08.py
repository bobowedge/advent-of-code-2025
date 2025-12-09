import heapq

def l2diff(pos1, pos2):
    l2norm = 0
    for i in range(3):
        diff = pos1[i] - pos2[i]
        l2norm += diff * diff
    return l2norm

def get_boxes(data):
    boxes = []
    for line in data:
        box = tuple([int(v) for v in line.split(",")])
        boxes.append(box)
    return boxes

def get_dtuples(boxes):
    dtuples = []
    for idx, box1 in enumerate(boxes):
        for box2 in boxes[idx+1:]:
            dtuple = (l2diff(box1, box2), box1, box2)
            heapq.heappush(dtuples, dtuple)
    return dtuples

def update_circuits(box1, box2, circuits):
    indexes = set()
    for idx, circuit in enumerate(circuits):
        if box1 in circuit or box2 in circuit:
            indexes.add(idx)
    if len(indexes) == 0:
        circuits.append({box1, box2})
    elif len(indexes) == 1:
        idx = indexes.pop()
        circuits[idx].update([box1, box2])
    elif len(indexes) == 2:
        idx1 = indexes.pop()
        idx2 = indexes.pop()
        min_idx = min(idx1, idx2)
        max_idx = max(idx1, idx2)
        circuit2 = circuits.pop(max_idx)
        circuits[min_idx] |= circuit2
    else:
        raise RuntimeError("Bad circuits")
    
def solution1(data, number=1000):

    boxes = get_boxes(data)
    dtuples = get_dtuples(boxes)
    counter = 0
    circuits = []
    while counter < number:
        counter += 1
        _, box1, box2 = heapq.heappop(dtuples)
        update_circuits(box1, box2, circuits)
    lengths = [len(circuit) for circuit in circuits]
    lengths.sort(reverse=True)
    return lengths[0] * lengths[1] * lengths[2]

def solution2(data): 
    boxes = get_boxes(data)
    dtuples = get_dtuples(boxes)
    circuits = []
    while len(dtuples) > 0:
        _, box1, box2 = heapq.heappop(dtuples)
        update_circuits(box1, box2, circuits)
        if len(circuits) == 1 and len(circuits[0]) == len(boxes):
            return box1[0] * box2[0]
    raise RuntimeError("Bad solution")

test_data = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""".splitlines()
data = open("day08.txt").read().splitlines()

assert solution1(test_data, 10) == 40
print(f"Solution 1: {solution1(data)}")
assert solution2(test_data) == 25272
print(f"Solution 2: {solution2(data)}")