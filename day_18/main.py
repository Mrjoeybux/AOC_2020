def parse_expression(line):
	expression = []
	for val in line.split(" "):
		if val.isdigit():
			expression.append(int(val))
		elif "(" in val:
			for _ in range(len(val) - 1):
				expression.append("(")
			expression.append(int(val[1]))
		elif ")" in val:
			expression.append(int(val[0]))
			for _ in range(len(val) - 1):
				expression.append(")")
		else:
			expression.append(val)
	return expression


def parse_input(path):
	with open(path, "r") as f:
		for line in f:
			yield parse_expression(line.split("\n")[0])

operations = {
	"+": lambda x, y: x + y,
	"*": lambda x, y: x*y,
	}

def evaluate(expression):
	if len(expression) == 3:
		return operations[expression[1]](expression[0], expression[2])
	#print(expression)
	if expression[-1] == ")":
		left = 0
		right = 1
		index = len(expression) - 1
		start_index = index
		while left != right:
			index -= 1
			left += (expression[index] == "(")
			right += (expression[index] == ")")
		new_expression = expression[index + 1: start_index]
		val = evaluate(new_expression)
	else:
		val = expression[-1]
		index = len(expression) - 1
	print(index)
	return operations[expression[index - 1]](expression[index - 2], val)


#print(parse_expression("1 + 2 * 3 + 4 * 5 + 6"))
#print(evaluate(parse_expression("1 + 2 * 3 + 4 * 5 + 6")))
print(parse_expression("1 + 2 * 3"))
print(evaluate(parse_expression("1 + (2 * 3)")))