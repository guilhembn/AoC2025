from pathlib import Path


def puzzle_5() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    fresh_part, ingredients_part = inp.split("\n\n")
    fresh = [tuple(map(int, f.split("-"))) for f in fresh_part.splitlines()]
    ingredients = set(map(int, ingredients_part.splitlines()))
    to_check = ingredients.copy()
    total_fresh = 0
    for lb, ub in fresh:
        to_remove = set()
        for i in to_check:
            if i in to_remove:
                continue
            if lb <= i <= ub:
                to_remove.add(i)
                total_fresh += 1
        to_check.difference_update(to_remove)
    return total_fresh

def union(range1, range2):
    lb1, ub1 = range1
    lb2, ub2 = range2
    if lb2 > ub1 or lb1 > ub2:
        # No intersection:
        return (range1, range2)
    return (min(lb1, lb2), max(ub1, ub2)), None

def update_unions(united: list[tuple[int, int]], new_range: tuple[int, int]):
    to_update = []
    for ran in united:
        uni = union(ran, new_range)
        if uni[1] is not None:
            continue
        else:
            to_update.append((ran, uni[0]))
    assert len(to_update) <= 2
    if len(to_update) == 0:
        united.append(new_range)
    else:
        for to_delete, _ in to_update:
            united.remove(to_delete)
        for _, to_add in to_update:
            united = update_unions(united, to_add)
    return united


def puzzle_5_p2() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    fresh_part, _ = inp.split("\n\n")
    fresh = [tuple(map(int, f.split("-"))) for f in fresh_part.splitlines()]
    united: list[tuple[int, int]] = []
    for range1 in fresh:
        united = update_unions(united, range1)
    total = 0
    for lb, ub in united:
        total += ub - lb + 1
    return total

print("Puzzle 5 Part 1:", puzzle_5())
print("Puzzle 5 Part 2:", puzzle_5_p2())
