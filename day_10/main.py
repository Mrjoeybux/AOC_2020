def parse_input(path):
	adapter_joltages = []
	with open(path, "r") as f:
		for line in f:
			adapter_joltages.append(int(line.split("\n")[0]))
	return adapter_joltages


def find_valid_adapters(adapter_joltages, current_joltage, index):
	return [joltage for joltage in adapter_joltages[index:] if joltage - current_joltage <= 3]


def find_connections(adapter_joltages):
	adapter_joltages = sorted(adapter_joltages)
	current_joltage = 0
	index = 0
	num_adapters = len(adapter_joltages)
	chain = {}
	while index < num_adapters:
		valid_adapters = find_valid_adapters(adapter_joltages, current_joltage, index)
		for adapter in valid_adapters:
			chain[current_joltage] = adapter
			index += 1
			current_joltage = adapter
	chain[current_joltage] = adapter_joltages[-1] + 3
	return chain


def count_differences(chain):
	differences = {1: 0, 2: 0, 3: 0}
	for start, end in chain.items():
		differences[end - start] += 1
	return differences


def get_arrangements(adapter_joltages):
	paths = {0: 1}
	adapter_joltages = [0] + sorted(adapter_joltages)
	for adapter in adapter_joltages:
		for diff in range(1, 4):
			next = diff + adapter
			if next in adapter_joltages:
				if next in paths:
					paths[next] += paths[adapter]
				else:
					paths[next] = paths[adapter]
	return paths[adapter_joltages[-1]]



def problem_1(path):
	joltages = parse_input("./input.txt")
	chain = find_connections(joltages)
	differences = count_differences(chain)
	return differences[1]*differences[3]


def problem_2(path):
	joltages = parse_input("./input.txt")
	return get_arrangements(joltages)


def test():
	n = ["n{}".format(i) for i in range(1, 5)]
	for i in range(len(n)):
		my = n[i]
		for j in [x for x in range(i+1, len(n)) if x != i]:
			my += "->{}".format(n[j])
		print(my)

if __name__ == "__main__":
	path = "./input.txt"
	print(problem_1(path))
	print(problem_2(path))