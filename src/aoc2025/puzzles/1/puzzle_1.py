from pathlib import Path

DIAL_MAX = 99

def puzzle_1() -> int:
    zeroed = 0
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    pos = 50
    for line in inp.split("\n"):
        if len(line) < 2:
            continue
        if line[0] == 'L':
            left = int(line[1:])
            while pos - left < 0:
                left -= pos + 1 
                pos = 99
            pos -= left
        elif line[0] == 'R':
            left = int(line[1:])
            while pos + left > DIAL_MAX:
                left -= DIAL_MAX - pos + 1
                pos = 0
            pos += left
        else:
            continue
        if pos == 0:
            zeroed += 1
    return zeroed

def puzzle_1_p2() -> int:
    zeroed = 0
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    pos = 50
    for line in inp.split("\n"):
        old_pos = pos
        if len(line) < 2:
            continue
        left = int(line[1:])
        if line[0] == 'L':
            for _ in range(left):
                pos -= 1
                if pos == 0:
                    zeroed += 1
                elif pos == -1:
                    pos = 99
        elif line[0] == 'R':
            for _ in range(left):
                pos += 1
                if pos == 100:
                    pos = 0
                if pos == 0:
                    zeroed += 1
        else:
            continue
    print(pos)
    return zeroed

print("Puzzle 1 Part 1:", puzzle_1())
print("Puzzle 1 Part 2:", puzzle_1_p2())