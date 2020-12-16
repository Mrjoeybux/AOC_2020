class DiscreteFloorPlanProcess:
	def __init__(self, floorplan, adjacent=True, empty_val="L", occupied_val="#", floor_val=".", debug=False, max_iter=50):
		self._floorplan = floorplan
		self._rows = len(floorplan)
		self._cols = len(floorplan[0])
		self._timestep = None
		self._converged = True
		self._empty_val = empty_val
		self._occupied_val = occupied_val
		self._floor_val = floor_val
		self._debug = debug
		self._max_iter = max_iter
		self._empty_update = None
		self._occupied_update = None
		if adjacent:
			self._empty_update = self._empty_adjacent_update
			self._occupied_update = self._occupied_adjacent_update
		else:
			self._empty_update = self._empty_visible_update
			self._occupied_update = self._occupied_visible_update
			self.directions = [self._N, self._NE, self._E, self._SE, self._S, self._SW, self._W, self._NW]

	def _update_one(self, row, col):
		if self._is_empty(row, col):
			return self._empty_update(row, col)
		if self._is_occupied(row, col):
			return self._occupied_update(row, col)
		return self._floor_val

	def _empty_adjacent_update(self, row, col):
		above = row if row == 0 else row - 1
		below = row + 1if row == self._rows - 1 else row + 2
		left = col if col == 0 else col - 1
		right = col + 1 if col == self._cols - 1 else col + 2
		for i in range(above, below):
			for j in range(left, right):
				if (i == row) and (j == col):
					continue
				if self._is_occupied(i, j):
					return self._empty_val
		return self._occupied_val

	def _occupied_adjacent_update(self, row, col):
		above = row if row == 0 else row - 1
		below = row + 1 if row == self._rows - 1 else row + 2
		left = col if col == 0 else col - 1
		right = col + 1 if col == self._cols - 1 else col + 2
		count = 0
		for i in range(above, below):
			for j in range(left, right):
				if (i == row) and (j == col):
					continue
				if self._is_occupied(i, j):
					count += 1
				if count == 4:
					return self._empty_val
		return self._occupied_val

	def _is_seat(self, i, j):
		return self._floorplan[i][j] in [self._empty_val, self._occupied_val]

	def _N(self, row, col):
		i = row - 1
		j = col
		while i >= 0:
			if self._is_seat(i, j):
				return i, j
			i -= 1
		return None, None

	def _NE(self, row, col):
		i = row - 1
		j = col + 1
		while (j < self._cols) and (i >= 0):
			if self._is_seat(i, j):
				return i, j
			j += 1
			i -= 1
		return None, None

	def _E(self, row, col):
		i = row
		j = col + 1
		while j < self._cols:
			if self._is_seat(i, j):
				return i, j
			j += 1
		return None, None

	def _SE(self, row, col):
		i = row + 1
		j = col + 1
		while (j < self._cols) and (i < self._rows):
			if self._is_seat(i, j):
				return i, j
			j += 1
			i += 1
		return None, None

	def _S(self, row, col):
		i = row + 1
		j = col
		while i < self._rows:
			if self._is_seat(i, j):
				return i, j
			i += 1
		return None, None

	def _SW(self, row, col):
		i = row + 1
		j = col - 1
		while (j >= 0) and (i < self._rows):
			if self._is_seat(i, j):
				return i, j
			j -= 1
			i += 1
		return None, None

	def _W(self, row, col):
		i = row
		j = col - 1
		while j >= 0:
			if self._is_seat(i, j):
				return i, j
			j -= 1
		return None, None

	def _NW(self, row, col):
		i = row - 1
		j = col - 1
		while (j >= 0) and (i >= 0):
			if self._is_seat(i, j):
				return i, j
			j -= 1
			i -= 1
		return None, None

	def _empty_visible_update(self, row, col):
		seats = [direction(row, col) for direction in self.directions]
		#print(seats)
		for seat in seats:
			if seat == (None, None):
				continue
			if self._is_occupied(*seat):
				return self._empty_val
		return self._occupied_val

	def _occupied_visible_update(self, row, col):
		seats = [direction(row, col) for direction in self.directions]
		#print(seats)
		count = 0
		for seat in seats:
			if seat == (None, None):
				continue
			if self._is_occupied(*seat):
				count += 1
			if count == 5:
				return self._empty_val
		return self._occupied_val

	def _is_empty(self, i, j):
		return self._floorplan[i][j] == self._empty_val

	def _is_occupied(self, i, j):
		return self._floorplan[i][j] == self._occupied_val

	def _is_floor(self, i, j):
		return self._floorplan[i][j] == self._floor_val

	def update(self):
		new_floorplan = []
		for i in range(self._rows):
			new_floorplan.append([])
			for j in range(self._cols):
				new_floorplan[i].append(self._update_one(i, j))
		self._check_convergence(new_floorplan)
		self._floorplan = new_floorplan

	def display(self):
		for i in range(self._rows):
			print("".join(self._floorplan[i]))
		print()

	def _check_convergence(self, new_floorplan):
		for i in range(self._rows):
			for j in range(self._cols):
				if self._floorplan[i][j] != new_floorplan[i][j]:
					return
		self._converged = True
		return

	def run(self):
		if self._timestep is None:
			self._timestep = 0
		if self._debug:
			self.display()
		self._converged = False
		while not self._converged:
			self.update()
			self._timestep += 1
			if self._debug:
				self.display()
			if self._timestep == self._max_iter:
				break

	def count_occupied(self):
		count = 0
		for i in range(self._rows):
			count += self._floorplan[i].count(self._occupied_val)
		return count


def parse_input(path):
	floorplan = []
	with open(path, "r") as f:
		for line in f:
			floorplan.append(list(line.split("\n")[0]))
	return floorplan


def problem_1(path):
	floorplan = parse_input(path)
	dfpp = DiscreteFloorPlanProcess(floorplan, debug=False)
	dfpp.run()
	return dfpp.count_occupied()


def problem_2(path):
	floorplan = parse_input(path)
	dfpp = DiscreteFloorPlanProcess(floorplan, debug=False, adjacent=False, max_iter=500)
	dfpp.run()
	return dfpp.count_occupied()


if __name__ == "__main__":
	path = "./input.txt"
	print(problem_1(path))
	print(problem_2(path))



