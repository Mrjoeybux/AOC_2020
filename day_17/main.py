from itertools import product
import operator

def parse_input(path):
	initial_state = set()
	extra_dims = [0 for _ in range(DIMS - 2)]
	with open(path, "r") as f:
		for x, line in enumerate(f):
			for y, val in enumerate(line.split("\n")[0]):
				if val == "#":
					initial_state.add((x, y, *extra_dims))
	return initial_state


def neighbour_coords(coords):
	center = tuple([0 for _ in range(DIMS)])
	for offset in product(*[range(-1, 2) for _ in range(DIMS)]):
		if offset == center:
			continue
		yield tuple(map(operator.add, coords, offset))


def active_map(coords, state_dict, updated_state_dict):
	count = sum([(neighbour in state_dict) for neighbour in neighbour_coords(coords)])
	if (count == 2) or (count == 3):
		updated_state_dict.add(coords)


def inactive_map(coords, state_dict, updated_state_dict):
	count = sum([(neighbour in state_dict) for neighbour in neighbour_coords(coords)])
	if count == 3:
		updated_state_dict.add(coords)


def state_map(coords, state_dict, updated_state_dict):
	return active_map(coords, state_dict, updated_state_dict) if coords in state_dict else inactive_map(coords, state_dict, updated_state_dict)


def one_iteration(state_dict):
	updated_state_dict = set()
	for coord in state_dict:
		state_map(coord, state_dict.copy(), updated_state_dict)
		for neighbour in neighbour_coords(coord):
			state_map(neighbour, state_dict.copy(), updated_state_dict)
	return updated_state_dict


def print_state_space(state_dict):
	max_coords = tuple(max([coord[i] for coord in state_dict]) + 1 for i in range(3))
	min_coords = tuple(min([coord[i] for coord in state_dict]) for i in range(3))
	for k in range(min_coords[2], max_coords[2]):
		print("z = {}".format(k))
		for i in range(min_coords[0], max_coords[0]):
			line = ""
			for j in range(min_coords[1], max_coords[1]):
				if (i, j, k) in state_dict:
					line += "#"
				else:
					line += "."
			print(line)
		print()


def problem_1(path):
	global DIMS
	DIMS = 3
	state_space = parse_input(path)
	cycle = 0
	while cycle < 6:
		state_space = one_iteration(state_space)
		cycle += 1
	return len(state_space)


def problem_2(path):
	global DIMS
	DIMS = 4
	state_space = parse_input(path)
	cycle = 0
	while cycle < 6:
		state_space = one_iteration(state_space)
		cycle += 1
	return len(state_space)

if __name__ == '__main__':
	path = "./input.txt"
	import time
	start = time.time()
	print(problem_1(path), time.time() - start)
	print(problem_2(path), time.time() - start)