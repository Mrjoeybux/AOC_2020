from collections import defaultdict


def parse_input(path):
	bitmasks_and_values = []
	with open(path, "r") as f:
		for i, line in enumerate(f):
			left, right = line.split("\n")[0].split(" = ")
			if i == 0:
				current_bitmask = [right]
				continue
			if ("mask" in line):
				bitmasks_and_values.append(current_bitmask)
				current_bitmask = [right]
				continue
			current_bitmask.append((int(left.split("mem[")[1].split("]")[0]), int(right)))
	bitmasks_and_values.append(current_bitmask)
	return bitmasks_and_values


def int_to_bit_array(x, digits=36):
	return [x for x in "{:0{size}b}".format(x, size=digits)]


def apply_bitmask(bitmask, bit_array):
	for i, mask in enumerate(bitmask):
		if mask == "X":
			continue
		bit_array[i] = mask
	return int("".join(bit_array), 2)


def problem_1(path):
	memory = defaultdict(int)
	bitmasks_and_values = parse_input(path)
	for mask_and_vals in bitmasks_and_values:
		mask = mask_and_vals[0]
		for val in mask_and_vals[1:]:
			bit_array = int_to_bit_array(val[1])
			memory[val[0]] = apply_bitmask(mask, bit_array)
	sum = 0
	for address in memory.keys():
		sum += memory[address]
	return sum


def apply_bitmask_version_2(bitmask, bit_array):
	for i, mask in enumerate(bitmask):
		if mask in ["1", "X"]:
			bit_array[i] = mask
	return bit_array


def memory_combinations(bit_array):
	combs = []
	indices = [i for i, x in enumerate(bit_array) if x == "X"]
	n = len(indices)
	possible_combinations = 2**n
	for i in range(possible_combinations):
		val = int_to_bit_array(i, digits=n)
		comb = bit_array.copy()
		for j in range(n):
			comb[indices[j]] = val[j]
		combs.append(int("".join(comb), 2))
	return combs


def write_to_memory(address, to_write, mask, memory):
	array = apply_bitmask_version_2(mask, int_to_bit_array(address))
	for mem_address in memory_combinations(array):
		memory[mem_address] = to_write


def problem_2(path):
	memory = defaultdict(int)
	bitmasks_and_values = parse_input(path)
	for mask_and_vals in bitmasks_and_values:
		mask = mask_and_vals[0]
		for val in mask_and_vals[1:]:
			write_to_memory(val[0], val[1], mask, memory)
	sum = 0
	for address in memory.keys():
		sum += memory[address]
	return sum

if __name__ == "__main__":
	path = "./input.txt"
	print(problem_1(path))
	print(problem_2(path))