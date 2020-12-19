def parse_field(field):
	name, range = field.split(": ")
	range = range.split(" or ")
	lower_range = tuple(int(x) for x in range[0].split("-"))
	upper_range = tuple(int(x) for x in range[1].split("-"))
	return name, lower_range + upper_range


def parse_input(path):
	whole_data = []
	data = []
	with open(path, "r") as f:
		for line in f:
			if "\n" == line:
				whole_data.append(data)
				data = []
				continue
			data.append(line.split("\n")[0])
	whole_data.append(data)
	fields, your_ticket, nearby_tickets = whole_data[:]
	return dict(parse_field(field) for field in fields), \
	       list(map(int, your_ticket[1].split(","))), \
	       [list(map(int, x.split(","))) for x in nearby_tickets[1:]]


def intervals_intersect(current_range, new_range):
	return (current_range[0] < new_range[0] <= current_range[1] + 1) or (current_range[0] -1 <= new_range[1] < current_range[1])


def reduce_intersection(intersections, new_range):
	min_val = new_range[0]
	max_val = new_range[1]
	for range in intersections:
		min_val = min(min_val, range[0])
		max_val = max(max_val, range[1])
	return (min_val, max_val)


def update_unique_ranges(new_range, unique_ranges):
	if not unique_ranges:
		return [new_range]
	new_unique_ranges = []
	intersections = []
	for current_range in unique_ranges:
		if intervals_intersect(current_range, new_range):
			intersections.append(current_range)
		else:
			new_unique_ranges.append(current_range)
	new_unique_ranges.append(reduce_intersection(intersections, new_range))
	return new_unique_ranges


def get_unique_ranges(fields):
	ranges = [fields[field] for field in fields]
	unique_ranges = []
	for range in ranges:
		lower_range, upper_range = range[0:2], range[2:]
		unique_ranges = update_unique_ranges(lower_range, unique_ranges)
		unique_ranges = update_unique_ranges(upper_range, unique_ranges)
	return unique_ranges


def invalid_value(value, unique_ranges):
	all_ranges = []
	for range in unique_ranges:
		if not (range[0] <= value <= range[1]):
			all_ranges.append(True)
		else:
			all_ranges.append(False)
	return all(all_ranges)


def problem_1(path):
	fields, my_ticket, nearby_tickets = parse_input(path)
	unique_ranges = get_unique_ranges(fields)
	error_rate = 0
	for ticket in nearby_tickets:
		for value in ticket:
			if invalid_value(value, unique_ranges):
				error_rate += value
	return error_rate


def tickets_to_fields(valid_tickets):
	num_fields = len(valid_tickets[0])
	fields = [set() for i in range(num_fields)]
	for ticket in valid_tickets:
		for i in range(num_fields):
			fields[i].add(ticket[i])
	return fields


def value_in_ranges(range, value):
	return (range[0] <= value <= range[1]) or (range[2] <= value <= range[3])


def check_values_for_given_range(range, values_for_field):
	return all([value_in_ranges(range, value) for value in values_for_field])


def possible_fields(values_for_field, fields):
	possibilities = set()
	for field, range in fields.items():
		if check_values_for_given_range(range, values_for_field):
			possibilities.add(field)
	return possibilities


def all_possibilities(values_per_field, fields):
	return [possible_fields(values_for_field, fields) for values_for_field in values_per_field]


def problem_2(path):
	fields, my_ticket, nearby_tickets = parse_input(path)
	unique_ranges = get_unique_ranges(fields)
	valid_tickets = []
	for ticket in nearby_tickets:
		if not any([invalid_value(value, unique_ranges) for value in ticket]):
			valid_tickets.append(ticket)
	values_per_field = tickets_to_fields(valid_tickets)
	index, possibilities = zip(*sorted(enumerate(all_possibilities(values_per_field, fields)), key=lambda x: len(x[1])))
	actual_fields = []
	for possibility in possibilities:
		field = list(possibility.difference(set(actual_fields)))[0]
		actual_fields.append(field)
	product = 1
	for i, field in enumerate(actual_fields):
		if field.startswith("departure"):
			product *= my_ticket[index[i]]
	return product

if __name__ == '__main__':
	path = "./input.txt"
	print(problem_1(path))
	print(problem_2(path))
