
def parse_input(path):
	instructions = []
	with open(path, "r") as f:
		for line in f:
			operation = line[:3]
			argument = int(line.split("\n")[0].split(" ")[1])
			instructions.append((operation, argument))
	return instructions


class InstructionExecutor:
	def __init__(self):
		self.accumulator = 0
		self.instruction_index = 0
		self.indices_visted = set()
		self.execution_functions = {
		"acc": self._acc,
		"jmp": self._jmp,
		"nop": self._nop
		}

	def run(self, instructions, until_repeat=True):
		if until_repeat:
			return self._run_until_repeat(instructions)

	def _run_until_repeat(self, instructions):
		indices_visted = set()
		for instruction in instructions:
			print(self.accumulator)
			self.execute_instruction(instruction)
			if self.instruction_index in indices_visted:
				return self.accumulator
			indices_visted.add(self.instruction_index)

	def execute_instruction(self, instruction):
		operation, argument = instruction
		self.execution_functions[operation](argument)

	def _acc(self, argument):
		self.accumulator += argument
		self.instruction_index += 1


	def _jmp(self, argument):
		self.instruction_index += argument


	def _nop(self, argument):
		self.instruction_index += 1


def run_instructions(instructions):
	ins_exec = InstructionExecutor()
	acc = ins_exec.run(instructions)
	print(acc)






ins = parse_input("input.txt")
print(ins)
print(run_instructions(ins))