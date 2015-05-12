import random
import Items, World, Enemies

class Player:
	inventory = [Items.Rock()]
	hp=100
	location_x, location_y = (0, 0)
	victory = False

	def is_alive(self):
		return self.hp > 0

	def do_action(self, action, **kwargs):
		action_method = getattr(self, action.method.__name__)
		if action_method:
			action_method(**kwargs)


	def print_inventory(self):
		for Item in self.inventory:
			print(Item, '\n')
			
	def move(self, dx, dy):
		self.location_x += dx
		self.location_y += dy
		print(World.tile_exists(self.location_x, self.location_y).intro_text())

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_south(self):
		self.move(dx=0, dy=1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)

#attack command
	def attack(self, Enemy):
		best_weapon = None
		max_dmg = 0
		for Item in self.inventory:
			if isinstance(Item, Items.Weapon):
				if Item.damage > max_dmg:
						max_dmg = Item.damage
						best_weapon = Item

		print("You use {} against {}!", format(best_weapon.name, Enemy.name))
		Enemy.hp -= best_weapon.damage
		if not Enemy.is_alive():
			print("{} has been slain!", format(Enemy.name))
		else:
			print("{} HP is {}.", format(Enemy.name, Enemy.hp))

	def flee(self, tile):		
		available_moves = tile.adjacent_move()
		r = random.randint(0, len(available_moves) - 1)
		self.do_action(available_moves[r])
	
