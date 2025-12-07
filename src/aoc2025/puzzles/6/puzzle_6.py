import operator
from pathlib import Path


def puzzle_6() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    *lines, operators_str = inp.strip().splitlines()
    operators = operators_str.split()
    values = [l.split() for l in lines]
    sum = 0
    for i in range(len(values[0])):
        total = int(values[0][i])
        if operators[i] == "*":
            oper = operator.mul
        elif operators[i] == "+":
            oper = operator.add
        else:
            print("WARNING Unknown operator", operators[i])
        for l in values[1:]:
            total = oper(total, int(l[i]))
        sum += total
    return sum

def get_operator(char: str):
    if char == "*":
        return operator.mul
    if char == "+":
        return operator.add
    print("WARNING Unknown operator", char)
    return operator.add

def puzzle_6_p2() -> int:
    inp = (Path(__file__).parent / Path("input.txt")).read_text()
    *lines, operators_str = inp.strip().splitlines()
    operators = operators_str.split()
    sum = 0
    total = None
    current_op_i = -1
    current_op = get_operator(operators[current_op_i])
    for i in range(len(lines[0])-1, -1, -1):
        is_split = True
        digit = []
        for j in range(len(lines)):
            if lines[j][i] != "" and lines[j][i] != " ":
                digit.append(lines[j][i])
                is_split = False
        if is_split:
            # Column contains only spaces
            if total is not None:
                sum += total
                current_op_i -= 1
                current_op = get_operator(operators[current_op_i])
            total = None
        else:
            int_digit = int("".join(digit))
            if total is None:
                total = int_digit
            else:
                total = current_op(total, int_digit)
    if total is not None:
        sum += total
    return sum

print("Puzzle 6 Part 1:", puzzle_6())
print("Puzzle 6 Part 2:", puzzle_6_p2())
