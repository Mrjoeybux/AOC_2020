from collections import defaultdict
def parse_input(path):
	with open(path, "r") as f:
		line = f.readline().split("\n")[0]
		return list(map(int, line.split(",")))


def next_move(last_number, number_dict, turn):
	if number_dict[last_number] == turn:
		next_number = 0
	else:
		next_number = turn - number_dict[last_number]
	number_dict[last_number] = turn
	return next_number


def play_game(starting_numbers, turns=2020):
	number_dict = defaultdict(int)
	starting_turns = len(starting_numbers)
	for i in range(starting_turns):
		number_dict[starting_numbers[i]] = i + 1
	last_number = starting_numbers[-1]
	for i in range(starting_turns + 1, turns + 1):
		last_number = next_move(last_number, number_dict, i - 1)
		if number_dict[last_number] == 0:
			number_dict[last_number] = i
	return last_number


def problem_1(path):
	numbers = parse_input(path)
	return play_game(numbers, turns=2020)


def problem_2(path):
	numbers = parse_input(path)
	return play_game(numbers, turns=30000000)


if __name__ == '__main__':
	import time
	path = "./input.txt"
	print(problem_1(path))
	start = time.time()
	print(problem_2(path))
	print(time.time() - start)