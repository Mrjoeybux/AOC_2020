def parse_input(path):
	numbers = []
	with open(path, "r") as f:
		for line in f:
			numbers.append(int(line.split("\n")[0]))
	return numbers


def validity_check(numbers, index, preamble_length):
	preamble = sorted(numbers[index - preamble_length: index])
	number_to_check = numbers[index]
	odd_numbers = [i for i in preamble if i % 2 == 1]
	even_numbers = [i for i in preamble if i % 2 == 0]
	if number_to_check % 2 == 0:
		num_odd = len(odd_numbers)
		num_even = len(even_numbers)
		for i in range(num_odd):
			for j in range(i + 1, num_odd):
				if odd_numbers[i] + odd_numbers[j] == number_to_check:
					return True
		for i in range(num_even):
			for j in range(i + 1, num_even):
				if even_numbers[i] + even_numbers[j] == number_to_check:
					return True
	else:
		for odd in odd_numbers:
			for even in even_numbers:
				if odd + even == number_to_check:
					return True
	return False


def check_xmas(numbers, preamble_length):
	index = preamble_length
	while index < len(numbers):
		if not validity_check(numbers, index, preamble_length):
			return numbers[index]
		index += 1
	return "All valid"


def brute_force_contiguous_sum(numbers, invalid_number):
	invalid_index = numbers.index(invalid_number)
	N = len(numbers)
	for i in range(N):
		if i == invalid_index:
			continue
		sum = numbers[i]
		for j in range(i + 1, N):
			if j == invalid_index:
				continue
			sum += numbers[j]
			if sum == invalid_number:
				return i, j
			if sum > invalid_number:
				break


def problem_1(path):
	numbers = parse_input(path)
	return check_xmas(numbers, 25)


def problem_2(path):
	numbers = parse_input(path)
	invalid_number = check_xmas(numbers, 25)
	i, j = brute_force_contiguous_sum(numbers, invalid_number)
	return min(numbers[i: j]) + max(numbers[i: j])


if __name__ == "__main__":
	path = "./input.txt"
	print(problem_1(path))
	print(problem_2(path))

