import heapq
from functools import cache

def path_count(start, end, map):
    if start not in map:
        return 0
    if end in map[start]:
        return 1
    counts = 0
    middles = map[start]
    for middle in middles:
        counts += path_count(start, middle, map) * path_count(middle, end, map)
    return counts

def path_count_cache(start, end, pcache):
    devices = pcache.get(start, None)
    if devices is None:
        return 0
    if end in devices:
        return devices[end]
    counts = 0
    for device, value in devices.items():
        if value > 0:
            counts += value * path_count_cache(device, end, pcache)    
    pcache[start][end] = counts
    return counts

def solution1(data):
    path_map = {}
    for line in data:
        start, ends = line.split(":")
        ends = ends.split()
        path_map[start] = ends
    return path_count("you", "out", path_map)

def solution2(data):
    num_paths = 0
    pcache = {}
    for line in data:
        start, ends = line.split(":")
        ends = ends.split()
        pcache[start] = {end: 1 for end in ends}

    svr_to_dac = path_count_cache("svr", "dac", pcache)
    dac_to_fft = path_count_cache("dac", "fft", pcache)
    fft_to_out = path_count_cache("fft", "out", pcache)

    svr_to_fft = path_count_cache("svr", "fft", pcache)
    fft_to_dac = path_count_cache("fft", "dac", pcache)
    dac_to_out = path_count_cache("dac", "out", pcache)

    return (
        svr_to_dac * dac_to_fft * fft_to_out + 
        svr_to_fft * fft_to_dac * dac_to_out
    )

test_data = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""".splitlines()
data = open("day11.txt").read().splitlines()
assert solution1(test_data) == 5
print(f"Solution 1: {solution1(data)}")
test_data = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out""".splitlines()
assert solution2(test_data) == 2
print(f"Solution 2: {solution2(data)}")