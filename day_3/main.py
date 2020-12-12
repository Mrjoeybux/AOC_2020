
def problem_1(tree_map, slope):
    row_step, col_step = slope
    nrows = len(tree_map)
    ncols = len(tree_map[0])
    ntrees = 0
    col = 0
    row = 0
    while row < nrows:
        if tree_map[row][col]:
            ntrees += 1
        col = (col + col_step) % ncols
        row += row_step
    return ntrees

def read_tree_map(path):
    tree_map = []
    with open(path, "r") as f:
        for line in f:
            tree_map.append([x == "#" for x in line.split("\n")[0]])
    return tree_map

def problem_2(tree_map):
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    val = 1
    for slope in slopes:
        val *= problem_1(tree_map, slope)
    return val

if __name__ == "__main__":
    tree_map = read_tree_map("input.txt")
    trees = problem_1(tree_map, (1, 3))
    print(problem_2(tree_map))
    