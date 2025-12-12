from itertools import combinations

def red_tiles(data):
    tiles = []
    for line in data:
        x, y = line.split(",")
        tile = (int(x), int(y))
        tiles.append(tile)
    return tiles

def area1(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    minx = min(x1, x2)
    maxx = max(x1, x2)
    miny = min(y1, y2)
    maxy = max(y1, y2)
    return (maxx - minx + 1) * (maxy - miny + 1)

def solution1(data):
    tiles = red_tiles(data)
    max_area = 0
    for pt1, pt2 in combinations(tiles, 2):
        max_area = max(max_area, area1(pt1, pt2))
    return max_area

def solution2(data):
    """Look at the data. It's close to a circle with a cutout"""
    tiles = red_tiles(data)
    max_area = 0
    top_pt = (94817, 50191)
    bottom_pt = (94817, 48573)
    for tile1, tile2 in combinations(tiles, 2):
        minx = min(tile1[0], tile2[0])
        maxx = max(tile1[0], tile2[0])
        miny = min(tile1[1], tile2[1])
        maxy = max(tile1[1], tile2[1])
        if minx < top_pt[0] and miny <= bottom_pt[1] < maxy:
            continue
        area = None
        for blockx, blocky in tiles:
            if minx < blockx < maxx and miny < blocky < maxy:
                area = 0
                break
        if area is None:
            area = area1(tile1, tile2)
            max_area = max(max_area, area)
    return max_area
    

test_data = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".splitlines()
data = open("day09.txt").read().splitlines()

assert solution1(test_data) == 50
print(f"Solution 1: {solution1(data)}")

print(f"Solution 2: {solution2(data)}")
