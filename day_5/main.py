def one_partition(lb, ub, char, lower_char):
    midpoint = ub - (ub - lb) // 2
    return (lb, midpoint - 1) if char == lower_char else (midpoint, ub)


def index_and_id(specification):
    lb = 0
    ub = NUM_ROWS - 1
    lower_char = "F"
    for i in range(len(specification)):
        lb, ub = one_partition(lb, ub, specification[i], lower_char)
        if i == 6:
            row_index = lb
            lower_char = "L"
            lb = 0
            ub = NUM_COLS - 1
    return row_index, lb, row_index*8 + lb

def problem_1(path):
    max_id = 0
    with open(path, "r") as f:
        for line in f:
            row, col, id = index_and_id(line.split("\n")[0])
            if id > max_id:
                max_id = id
    return max_id

def problem_2(path):
    ids = []
    with open(path, "r") as f:
        for line in f:
            _, _, id = index_and_id(line.split("\n")[0])
            ids.append(id)
    for id in sorted(ids):
        if (id + 2 in ids) and (id + 1 not in ids):
            return id + 1


if __name__ == "__main__":
    global NUM_ROWS, NUM_COLS
    NUM_ROWS = 128
    NUM_COLS = 8
    path = "./input.txt"
    print(problem_1(path))
    print(problem_2(path))