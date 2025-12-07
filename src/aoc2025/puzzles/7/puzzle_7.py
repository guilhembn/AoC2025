import operator
from pathlib import Path


def puzzle_7() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    lines = inp.strip().splitlines()
    m_map = [[c for c in l.strip()] for l in lines]
    start = None
    for row, l in enumerate(m_map):
        for col, c in enumerate(l):
            if c == "S":
                start = (row, col)
                break
        if start is not None:
            break
    stack = [start]
    discovered = set()
    split_num = 0
    while len(stack) > 0:
        pos = stack.pop()
        if pos is None:
            # Should not happen, but type hinting...
            break
        if pos not in discovered:
            discovered.add(pos)
            pos_r, pos_c = pos
            c = m_map[pos_r][pos_c]
            if c != "^":
                if pos_r < len(m_map) - 1:
                    stack.append((pos_r + 1, pos_c))
            else:
                split_num += 1
                if pos_c > 0:
                    stack.append((pos_r, pos_c - 1))
                if pos_c < len(m_map[0]) - 1:
                    stack.append((pos_r, pos_c + 1))

    for d_r, d_c in discovered:
        c = m_map[d_r][d_c]
        if c != "^" and c != "S":
            m_map[d_r][d_c] = "|"
    t = "\n".join(map(lambda l: "".join(l), m_map))
    # print(t)
    return split_num


def puzzle_7_p2() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    lines = inp.strip().splitlines()
    m_map = [[c for c in l.strip()] for l in lines]
    start = None
    for row, l in enumerate(m_map):
        for col, c in enumerate(l):
            if c == "S":
                start = (row, col)
                break
        if start is not None:
            break
    cell_to_pathes_n = {}
    for row, l in enumerate(m_map):
        for col, c in enumerate(l):
            curr_val = 0
            if row == 0:
                cell_to_pathes_n[(row, col)] = 0 if c != "S" else 1
                continue
            if c == "^":
                cell_to_pathes_n[(row, col)] = 0
                continue
            curr_val += cell_to_pathes_n[(row - 1, col)]
            if col > 0 and m_map[row][col - 1] == "^":
                # If the cell has a splitter to its left, we add number of pathes above the splitter
                curr_val += cell_to_pathes_n[(row - 1, col - 1)]
            if col < len(l) - 1 and m_map[row][col + 1] == "^":
                # If the cell has a splitter to its right, we add number of pathes above the splitter
                curr_val += cell_to_pathes_n[((row - 1, col + 1))]
            cell_to_pathes_n[(row, col)] = curr_val

    pathes = 0
    last_line = len(m_map) - 1
    for col in range(len(m_map[last_line])):
        pathes += cell_to_pathes_n[(last_line, col)]
    output = [[c for c in l] for l in m_map]
    for d_r, d_c in cell_to_pathes_n:
        output[d_r][d_c] = str(cell_to_pathes_n[(d_r, d_c)])
    t = "\n".join(map(lambda l: "".join(l), output))
    # print(t)
    return pathes


print("Puzzle 7 Part 1:", puzzle_7())
print("Puzzle 7 Part 2:", puzzle_7_p2())
