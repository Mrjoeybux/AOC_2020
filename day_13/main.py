def parse_input(path):
	with open(path, "r") as f:
		inp = f.read().splitlines()
	data = inp[1].split(",")
	return int(inp[0]), [(int(x), i) for i, x in enumerate(data) if x != "x"]


def closest_time_for_bus(ID, my_time):
	multiple = 0
	while(multiple*ID) < my_time:
		multiple += 1
	return ID, multiple*ID


def problem_1(path):
	my_time, buses = parse_input(path)
	min_time = None
	my_bus = None
	for bus in buses:
		ID, earliest_time = closest_time_for_bus(bus[0], my_time)
		if (min_time is None) or (earliest_time < min_time):
			min_time = earliest_time
			my_bus = ID
	return (min_time - my_time)*my_bus


def check_given_multiplier(IDs, multiplier):
	timestamp = IDs[0]*multiplier
	for i, ID in enumerate(IDs):
		if ID is None:
			continue
		if (timestamp + i) % ID != 0:
			return False
	return True


def problem_2(path):
	_, buses = parse_input(path)
	time = 0
	step = 1
	for i in range(len(buses) - 1):
		ID, idx = buses[i + 1]
		step *= buses[i][0]
		while (time + idx) % ID != 0:
			time += step
	return time



if __name__ == "__main__":
	path = "./input.txt"
	print(problem_1(path))
	print(problem_2(path))