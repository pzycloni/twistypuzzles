import random

class Field:

	def __init__(self, size = 3):
		self.size = 3
		self.field = self.set_random()


	def set_random(self):
		elements = [number for number in range(1, self.size**2)]
		elements.append(None)
		random.shuffle(elements)

		line = list()
		for i in range(self.size):
			line.append(elements[i*3:(i + 1)*3])
		return line


	def get_empty_position(self):
		for i, arr in enumerate(self.field):
			for j, el in enumerate(arr):
				if el == None:
					return [i, j]

	def get_imbalance(self):
		counter, imbalance = 1, 0
		for row in range(self.size):
			for col in range(self.size):
				if counter != self.field[row][col]:
					if self.field[row][col] is not None:
						imbalance += 1
				counter += 1
		return imbalance


class Control:

	def __init__(self, size = 3):
		self.table = Field(size)
		self.l = -1
		self.r = 1
		self.u = -1
		self.d = 1

		
		self.imbalance = self.table.get_imbalance()
		self.empty = self.table.get_empty_position()


	def can_move(self, action):
		if action == 'left':
			if self.empty[1] == 0:
				return False
		elif action == 'right':
			if self.empty[1] == 2:
				return False
		elif action == 'up':
			if self.empty[0] == 0:
				return False
		elif action == 'down':
			if self.empty[0] == 2:
				return False

		return True


	def swap(self, pos1, pos2):
		row1, row2 = pos1[0], pos2[0]
		col1, col2 = pos1[1], pos2[1]

		self.table.field[row1][col1], self.table.field[row2][col2] = self.table.field[row2][col2], self.table.field[row1][col1]
		self.empty = pos2



	def left(self):
		if self.can_move('left'):
			neighbor = [self.empty[0], self.empty[1] + self.l]
			self.swap(self.empty, neighbor)
		return self.table.field


	def right(self):
		if self.can_move('right'):
			neighbor = [self.empty[0], self.empty[1] + self.r]
			self.swap(self.empty, neighbor)
		return self.table.field


	def up(self):
		if self.can_move('up'):
			neighbor = [self.empty[0] + self.u, self.empty[1]]
			self.swap(self.empty, neighbor)
		return self.table.field


	def down(self):
		if self.can_move('down'):
			neighbor = [self.empty[0] + self.d, self.empty[1]]
			self.swap(self.empty, neighbor)
		return self.table.field

	def print(self):
		for i in self.table.field:
			print(i)
		print('---------')


class Node:

	def __init__(self, field, parent = None):
		self.grade = 0
		self.weight = 0
		self.field = field
		self.parent = parent
		self.children = list()


	def has_children(self):
		return bool(len(self.children))


	def set_branch(self, node):
		self.children.append(node)


	def get_children(self):
		return self.children


class Game:

	def __init__(self, size = 3):
		self.joystick = Control(size)


def move(joystick, action):

	if action == 'left':
		return joystick.left()
	if action == 'right':
		return joystick.right()
	if action == 'up':
		return joystick.up()
	if action == 'down':
		return joystick.down()




if __name__ == '__main__':

	game = Game()
	game.joystick.print()
	game.joystick.left()
	game.joystick.print()
	game.joystick.right()
	game.joystick.print()
	game.joystick.up()
	game.joystick.print()
	game.joystick.up()
	game.joystick.print()
	game.joystick.down()
	game.joystick.print()
	game.joystick.down()
	game.joystick.print()
	game.joystick.down()
	game.joystick.print()