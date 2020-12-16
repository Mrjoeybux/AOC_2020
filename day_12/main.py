from dataclasses import dataclass


def parse_input(path):
	instructions = []
	with open(path, "r") as f:
		for line in f:
			line = line.split("\n")[0]
			instructions.append((line[0], int(line[1:])))
	return instructions


@dataclass
class WayPoint:
	north: int = 1
	east: int = 10


@dataclass
class Ship:
	north: int = 0
	east: int = 0
	orientation: int = 0


@dataclass
class ShipWithWayPoint:
	north: int = 0
	east: int = 0
	waypoint: WayPoint = WayPoint()


def forward(val, ship):
	actions[rotations[ship.orientation]](val, ship)


def north(val, ship):
	ship.north += val


def south(val, ship):
	ship.north -= val


def east(val, ship):
	ship.east += val


def west(val, ship):
	ship.east -= val


def right(val, ship):
	ship.orientation = (ship.orientation + val // 90) % 4


def left(val, ship):
	right(-val, ship)


def move_ship(instructions, ship):
	for instruction in instructions:
		actions[instruction[0]](instruction[1], ship)


def problem_1(path):
	instructions = parse_input(path)
	ship = Ship()
	move_ship(instructions, ship)
	return abs(ship.north) + abs(ship.east)


def waypoint_forward(val, ship):
	ship.north += val*ship.waypoint.north
	ship.east += val*ship.waypoint.east


def waypoint_north(val, ship):
	ship.waypoint.north += val


def waypoint_south(val, ship):
	ship.waypoint.north -= val


def waypoint_east(val, ship):
	ship.waypoint.east += val


def waypoint_west(val, ship):
	ship.waypoint.east -= val


def waypoint_right(val, ship):
	north = ship.waypoint.north
	east = ship.waypoint.east
	if val == 90:
		ship.waypoint.east = north
		ship.waypoint.north = -east
	elif val == 180:
		ship.waypoint.east = -east
		ship.waypoint.north = -north
	elif val == 270:
		ship.waypoint.east = -north
		ship.waypoint.north = east


def waypoint_left(val, ship):
	waypoint_right(360 - val, ship)


def move_ship_and_waypoint(instructions, ship):
	for instruction in instructions:
		waypoint_actions[instruction[0]](instruction[1], ship)


def problem_2(path):
	instructions = parse_input(path)
	ship = ShipWithWayPoint()
	move_ship_and_waypoint(instructions, ship)
	return abs(ship.north) + abs(ship.east)


if __name__ == "__main__":
	global actions, rotations, waypoint_actions
	actions = {
		"F": forward,
		"N": north,
		"S": south,
		"E": east,
		"W": west,
		"L": left,
		"R": right
		}
	rotations = {
		0: "E",
		1: "S",
		2: "W",
		3: "N"
		}
	waypoint_actions = {
		"F": waypoint_forward,
		"N": waypoint_north,
		"S": waypoint_south,
		"E": waypoint_east,
		"W": waypoint_west,
		"L": waypoint_left,
		"R": waypoint_right
		}
	path = "./input.txt"
	print(problem_1(path))
	print(problem_2(path))