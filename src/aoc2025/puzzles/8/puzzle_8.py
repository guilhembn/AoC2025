from pathlib import Path


def puzzle_8() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    return 0


def puzzle_8_p2() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    return 0


print("Puzzle 7 Part 1:", puzzle_8())
print("Puzzle 7 Part 2:", puzzle_8_p2())
