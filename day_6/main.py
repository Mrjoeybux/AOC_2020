def parse_input(path, intersection=False):
	groups = []
	current_group = []
	with open(path, "r") as f:
		for line in f:
			if line == "\n":
				if intersection:
					groups.append(set.intersection(*current_group))
				else:
					groups.append(set.union(*current_group))
				current_group = []
				continue
			current_group.append(set(line.split("\n")[0]))
	if intersection:
		groups.append(set.intersection(*current_group))
	else:
		groups.append(set.union(*current_group))
	return groups


def problem_1(path):
	groups = parse_input(path, intersection=False)
	size = 0
	for group in groups:
		size += len(group)
	return size


def problem_2(path):
	groups = parse_input(path, intersection=True)
	size = 0
	for group in groups:
		size += len(group)
	return size



if __name__ == "__main__":
	path = "./input.txt"
	print(problem_1(path))
	print(problem_2(path))
