from pathlib import Path


def puzzle_3() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    total = 0
    for l in inp.split("\n"):
        if len(l) == 0:
            continue
        first_digit = None
        second_digit = None
        for i in range(9, -1, -1):
            index = l.find(str(i), 0, len(l) - 1)
            if index != -1:
                first_digit = i
                break
        for i in range(9, -1, -1):
            index_2 = l.find(str(i), index + 1)
            if index_2 != -1:
                second_digit = i
                break
        battery_level = int(str(first_digit) + str(second_digit))
        total += battery_level
    return total

def puzzle_3_p2() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    total = 0
    for l in inp.split("\n"):
        digits = []
        last_index = 0
        if len(l) == 0:
            continue
        for d in range(12):
            for i in range(9, -1, -1):
                index = l.find(str(i), last_index, len(l) - 11 + d)
                if index != -1:
                    last_index = index + 1
                    digits.append(str(i))
                    break
        battery_level = int("".join(digits))
        total += battery_level
    return total

print("Puzzle 3 Part 1:", puzzle_3())
print("Puzzle 3 Part 2:", puzzle_3_p2())
