# Cranberries
# Senior Project for Eli and Henry
from Player import Player

class Action():
	def __init__(self, method, name, hotkey, **kwargs):
		self.method = method
		self.hotkey = hotkey
		self.name = name
		self.kwargs = kwargs

	def __str__(self):
		return "{}: {}".format(self.hotkey, self.name)
#movment hotkeys 
class MoveNorth(Action):
	def __init__(self):
		super().__init__(method=Player.move_north, name='Move north', hotkey='w')

class MoveSouth(Action):
	def __init__(self):
		super().__init__(method=Player.move_south, name='Move south', hotkey='s')
class MoveEast(Action):
	def __init__(self):
		super().__init__(method=Player.move_east, name='Move east',hotkey='d')
class MoveWest(Action):
	def __init__(self):
		super().__init__(method=Player.move_east, name='Move east',hotkey='a')
class ViewInventory(Action):
	"""Print the player's inventory"""
	def __init__(self):
		super().__init__(method=Player.print_inventory, name='Veiw inventory', hotkey='i')

class Attack(Action):
	def __init__(self, enemy):
		super().__init__(method=Player.attack, name="Attack", hotkey='e', enemy=enemy)

class Flee(Action):
	def __init__(self, Tile):
		super().__init__(method=Player.flee, name="Flee", hotkey='r', Tile=Tile)
