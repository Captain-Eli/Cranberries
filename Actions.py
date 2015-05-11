# Cranberries
# Senior Project for Eli and Henry
from Player import Player

from Enemies import Enemy
class Action(object):
	def __init__(self, method, name, hotkey, **kwargs):
		self.method = method
		self.hotkey = hotkey
		self.name = name
		self.kwargs = kwargs
		print("method:", method)
		print("hotkey:", hotkey)
		print("name:", name)
		print("kwargs:", kwargs)

	def __str__(self):
		return "{}: {}".format(self.hotkey, self.name)
#movment hotkeys 
class MoveNorth(Action):
	def __init__(self):
		super(MoveNorth, self).__init__(method=Player.move_north, name='Move north', hotkey='w')

class MoveSouth(Action):
	def __init__(self):
		super(MoveSouth, self).__init__(method=Player.move_south, name='Move south', hotkey='s')
class MoveEast(Action):
	def __init__(self):
		super(MoveEast, self).__init__(method=Player.move_east, name='Move east',hotkey='d')
class MoveWest(Action):
	def __init__(self):
		super(MoveWest, self).__init__(method=Player.move_west, name='Move west',hotkey='a')
class ViewInventory(Action):
	"""Print the player's inventory"""
	def __init__(self):
		super(ViewInventory, self).__init__(method=Player.print_inventory, name='View inventory', hotkey='i')

class Attack(Action):
	def __init__(self, enemyToAttack):
		super(Attack, self).__init__(method=Player.attack, name="Attack", hotkey='e', enemy=enemyToAttack)

class Flee(Action):
	def __init__(self, Tile):
		super(Flee, self).__init__(method=Player.flee, name="Flee", hotkey='r', Tile=Tile)
