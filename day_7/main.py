class BagDataStructure:
	def __init__(self, colour):
		self.colour = colour
		self.contents = None
		self.root = False

	def add_child_bag(self, colour, number):
		if self.contents is None:
			self.contents = {}
		self.contents[colour] = number

	def is_empty(self):
		return None in self.contents

	def children(self):
		return self.contents.keys()

	def has_child(self, colour):
		return colour in self.contents

	def bags_per_child(self, colour):
		return self.contents[colour]

	def total_child_bags(self):
		return sum([self.contents[colour] for colour in self.contents])

	def __str__(self):
		if self.root:
			ret_str = "A root {} bag that can hold: \n".format(self.colour)
		else:
			ret_str = "A {} bag that can hold: \n".format(self.colour)
		for child_colour in self.contents.keys():
			if child_colour == None:
				ret_str += "-No other bags\n"
			elif self.contents[child_colour] == 1:
				ret_str += "-{} {} bag\n".format(self.contents[child_colour], child_colour)
			else:
				ret_str += "-{} {} bags\n".format(self.contents[child_colour], child_colour)
		return ret_str


def parse_child(child_line):
	split = child_line.split(" bag")[0].split(" ")
	number = split[0]
	if number == "no":
		return None, None
	else:
		number = int(number)
	colour = " ".join(split[1:])
	return colour, number


def parse_line(line):
	colour, contents = line.split(".")[0].split(" bags contain ")
	bag = BagDataStructure(colour)
	for child_bag in contents.split(", "):
		child_colour, number = parse_child(child_bag)
		bag.add_child_bag(child_colour, number)
	return bag


def parse_input(path):
	bags = {}
	with open(path, "r") as f:
		for line in f:
			bag = parse_line(line)
			bags[bag.colour] = bag
	return bags


def get_parents_of_child(bag_dict, child_colour):
	parents = []
	for bag_colour in bag_dict.keys():
		if bag_dict[bag_colour].has_child(child_colour):
			parents.append(bag_colour)
	return parents


def problem_1(path):
	bag_dict = parse_input(path)
	possible_routes = set()
	curent_children = ["shiny gold"]
	while True:
		new_parents = set()
		for bag_colour in curent_children:
			parents = get_parents_of_child(bag_dict, bag_colour)
			new_parents.update(parents)
		possible_routes.update(new_parents)
		curent_children = list(new_parents)
		if curent_children == []:
			break
	return len(possible_routes)


def traverse_bag_tree(bag_dict, current_node):
	if bag_dict[current_node].is_empty():
		return 0
	children = bag_dict[current_node].children()
	count = 0
	for child in children:
		count += bag_dict[current_node].bags_per_child(child)*(traverse_bag_tree(bag_dict, child) + 1)
	return count




def problem_2(path):
	bag_dict = parse_input(path)
	bag_counter = 0
	current_bag = "shiny gold"
	print(traverse_bag_tree(bag_dict, current_bag), "hi")
	"""while True:
		for bag in current_bags:
			children = bag_dict[bag].children()
			for child in children:
				bag_counter += bag_dict[bag].bags_per_child(child)
		current_bags = children
		if all([bag_dict[bag].is_empty() for bag in current_bags]):
			break
	return bag_counter"""




if __name__ == "__main__":
	path = "./input.txt"
	#print(problem_1(path))
	print(problem_2(path))

