import random
import Items, World

class Player:
	inventory = [Items.Gold(15), Items.Rock()]
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
		for item in self.inventory:
			print(item, '\n')
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
	def attack(self, enemy):
		best_weapon = None
		max_dmg = 0	
		for i in self.inventory:
			if isinstance(i, items.Weapon):
				if i.damage > max_dmg:
						max_dmg = i.damage
						best_weapon = i

		print("You use {} against {}!".format(best_weapon.name, enemy.name))
		enemy.hp -= best_weapon.damage
		if not enemy.is_alive():
			print("{} has been slain!".format(enemy.name))
		else:
			print("{} HP is {}.".format(enemy.name, enemy.hp))

	def flee(self, tile):		
		available_moves = tile.adjacent_move()
		r = random.randint(0, len(available_moves) - 1)
		self.do_action(available_moves[r])
	
