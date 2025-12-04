from functools import reduce
from pathlib import Path


def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def puzzle_2() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    add = 0
    for r in inp.split(","):
        lb, rb = map(int, r.split("-"))
        for i in range(lb, rb + 1):
            si = str(i)
            if len(si) % 2 != 0:
                continue
            half = int(len(si)/2)
            if si[:half] == si[half:]:
                add += i
    return add

def puzzle_2_p2() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    add = 0
    invalids = set()
    for r in inp.split(","):
        lb, rb = map(int, r.split("-"))
        for i in range(lb, rb + 1):
            si = str(i)
            for d in factors(len(si)):
                if d == len(si):
                    continue
                cut = [si[i:i+d] for i in range(0, len(si), d)]
                if len(set(cut)) == 1 and i not in invalids:
                    invalids.add(i)
                    add += i
    return add

print("Puzzle 2 Part 1:", puzzle_2())
print("Puzzle 2 Part 2:", puzzle_2_p2())
