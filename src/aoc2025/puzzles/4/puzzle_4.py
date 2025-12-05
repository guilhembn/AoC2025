from pathlib import Path


def neighbours_indices(row, col, height, width):
    for i in range(-1, 2):
        row_n = row + i
        if row_n < 0 or row_n >= height:
            continue
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            col_n = col + j
            if col_n < 0 or col_n >= width:
                continue
            yield(row_n, col_n)

def puzzle_4() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    lines = inp.strip().splitlines()
    chart = [[c for c in l.strip()] for l in lines]
    rolls_pos = []
    total = 0
    for row_i, row in enumerate(chart):
        for col_i, c in enumerate(row):
            if c != "@":
                continue
            neighbours_count = 0
            for r, c in neighbours_indices(row_i, col_i, len(chart), len(row)):
                if chart[r][c] == "@":
                    neighbours_count += 1
            if neighbours_count < 4:
                rolls_pos.append((row_i, col_i))
                total += 1
    for r, c in rolls_pos:
        chart[r][c] = "x"
    print("\n".join(map(lambda x: "".join(x), chart)))
    return total
            
def puzzle_4_p2() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    lines = inp.strip().splitlines()
    chart = [[c for c in l.strip()] for l in lines]
    rolls_pos = []
    total = 0
    while True:
        replaced_run = 0
        for row_i, row in enumerate(chart):
            for col_i, c in enumerate(row):
                if c != "@":
                    continue
                neighbours_count = 0
                for r, c in neighbours_indices(row_i, col_i, len(chart), len(row)):
                    if chart[r][c] == "@":
                        neighbours_count += 1
                if neighbours_count < 4:
                    rolls_pos.append((row_i, col_i))
                    total += 1
                    replaced_run += 1
        for r, c in rolls_pos:
            chart[r][c] = "x"
        if replaced_run == 0:
            break
    print("\n".join(map(lambda x: "".join(x), chart)))
    return total

print("Puzzle 4 Part 1:", puzzle_4())
print("Puzzle 4 Part 2:", puzzle_4_p2())
