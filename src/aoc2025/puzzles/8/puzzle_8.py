from pathlib import Path


def puzzle_8() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    boxes = [tuple(map(int, l.split(","))) for l in inp.splitlines()]
    box_to_group = {b:i for i, b in enumerate(boxes)}
    group_to_boxes = {i: [b] for i, b in enumerate(boxes)}
    distances = {}
    for i,b1 in enumerate(boxes):
        for b2 in boxes[i+1:]:
            dist = (sum([(b2[c] - b1[c])**2 for c in range(3)]))**0.5
            distances[(b1, b2)] = dist
            # distances[(b2, b1)] = dist
    sorted_distances = sorted(distances, key=lambda d: distances[d])
    for bbs in sorted_distances[:1000]:  
        group_to_connect = box_to_group[bbs[1]]
        group_to_connect_to = box_to_group[bbs[0]]
        if group_to_connect == group_to_connect_to:
            continue
        group_to_boxes[group_to_connect_to] += group_to_boxes[group_to_connect]
        group_to_boxes[group_to_connect] = []
        for box in group_to_boxes[group_to_connect_to]:
            box_to_group[box] = group_to_connect_to
    sorted_groups = sorted(group_to_boxes, key=lambda k: len(group_to_boxes[k]), reverse=True)
    return len(group_to_boxes[sorted_groups[0]]) * len(group_to_boxes[sorted_groups[1]]) * len(group_to_boxes[sorted_groups[2]])


def puzzle_8_p2() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    boxes = [tuple(map(int, l.split(","))) for l in inp.splitlines()]
    box_to_group = {b:i for i, b in enumerate(boxes)}
    group_to_boxes = {i: [b] for i, b in enumerate(boxes)}
    distances = {}
    for i,b1 in enumerate(boxes):
        for b2 in boxes[i+1:]:
            dist = (sum([(b2[c] - b1[c])**2 for c in range(3)]))**0.5
            distances[(b1, b2)] = dist
            # distances[(b2, b1)] = dist
    sorted_distances = sorted(distances, key=lambda d: distances[d])
    for bbs in sorted_distances:  
        group_to_connect = box_to_group[bbs[1]]
        group_to_connect_to = box_to_group[bbs[0]]
        if group_to_connect == group_to_connect_to:
            continue
        group_to_boxes[group_to_connect_to] += group_to_boxes[group_to_connect]
        group_to_boxes[group_to_connect] = []
        for box in group_to_boxes[group_to_connect_to]:
            box_to_group[box] = group_to_connect_to
        sorted_groups = sorted(group_to_boxes, key=lambda k: len(group_to_boxes[k]), reverse=True)
        if len(group_to_boxes[sorted_groups[0]]) == len(boxes):
            return bbs[0][0] * bbs[1][0]
    return 0

print("Puzzle 8 Part 1:", puzzle_8())
print("Puzzle 8 Part 2:", puzzle_8_p2())
