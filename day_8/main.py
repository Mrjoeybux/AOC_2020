def parse_input(path):
	instructions = []
	with open(path, "r") as f:
		for line in f:
			operation = line[:3]
			argument = int(line.split("\n")[0].split(" ")[1])
			instructions.append((operation, argument))
	return instructions


class InstructionExecutor:
	def __init__(self, debug=False):
		self.accumulator = 0
		self.instruction_index = 0
		self.debug = debug
		self.execution_functions = {
			"acc": self._acc,
			"jmp": self._jmp,
			"nop": self._nop
			}

	def run(self, instructions, until_repeat=True):
		if until_repeat:
			return self._run_until_repeat(instructions)
		return self._run_and_fix(instructions)

	def _run_until_repeat(self, instructions):
		indices_visited = set()
		while True:
			self.execute_instruction(instructions[self.instruction_index])
			if self.instruction_index in indices_visited:
				return self.accumulator
			indices_visited.add(self.instruction_index)

	def _run_and_fix(self, instructions):
		instructions_to_change = [i for i in range(len(instructions)) if instructions[i][0] in ["jmp", "nop"]]
		for index in instructions_to_change:
			if self._convergence_check(self._change_instruction(index, instructions)):
				return self.accumulator
			self._reset()

	def _reset(self):
		self.accumulator = 0
		self.instruction_index = 0

	def _convergence_check(self, instructions):
		indices_visited = set()
		while True:
			self.execute_instruction(instructions[self.instruction_index])
			if self.instruction_index in indices_visited:
				return False
			if self.instruction_index == len(instructions):
				return True
			indices_visited.add(self.instruction_index)

	def _change_instruction(self, index, instructions):
		operation, argument = instructions[index]
		if operation == "jmp":
			new = ("nop", argument)
		else:
			new = ("jmp", argument)
		return instructions[:index] + [new] + instructions[index + 1:]

	def execute_instruction(self, instruction):
		operation, argument = instruction
		self.execution_functions[operation](argument)

	def _acc(self, argument):
		if self.debug:
			print("acc: {}".format(argument))
		self.accumulator += argument
		self.instruction_index += 1

	def _jmp(self, argument):
		if self.debug:
			print("jmp: {}".format(argument))
		self.instruction_index += argument

	def _nop(self, argument):
		if self.debug:
			print("nop: {}".format(argument))
		self.instruction_index += 1


def run_instructions(instructions):
	ins_exec = InstructionExecutor(debug=False)
	return ins_exec.run(instructions)


def fix_instructions(instructions):
	ins_exec = InstructionExecutor(debug=False)
	return ins_exec.run(instructions, until_repeat=False)


def problem_1(path):
	instructions = parse_input(path)
	return run_instructions(instructions)


def problem_2(path):
	instructions = parse_input(path)
	return fix_instructions(instructions)


if __name__ == "__main__":
	path = "input.txt"
	print(problem_1(path))
	print(problem_2(path))
