from pathlib import Path


def puzzle_9() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    return 0


def puzzle_9_p2() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    return 0

print("Puzzle 9 Part 1:", puzzle_9())
print("Puzzle 9 Part 2:", puzzle_9_p2())
