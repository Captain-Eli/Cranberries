import random
import Items, World
import Enemy

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
			print(Item)
			
	def move(self, dx, dy):
		if World.tile_exists(self.location_x + dx, self.location_y + dy):
                        self.location_x += dx
                        self.location_y += dy
                        print(World.tile_exists(self.location_x, self.location_y).intro_text())
                else:
                        print("You bump into an invisible wall.")

	def move_north(self):
		self.move(dx=0, dy=1)

	def move_south(self):
		self.move(dx=0, dy=-1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)

#attack command
	def attack(self, enemy):
		best_weapon = None
		max_dmg = 0
		for Item in self.inventory:
			if isinstance(Item, Items.Weapon):
				if Item.damage > max_dmg:
						max_dmg = Item.damage
						best_weapon = Item

		print("You use a {0} against the {1}!".format(best_weapon.name, enemy.name))
		enemy.hp -= best_weapon.damage
		if not enemy.is_alive():
			print("The {0} has been slain!".format(enemy.name))
		else:
			print("{0} HP is {1}.".format(enemy.name, enemy.hp))

	def flee(self, tile):		
		available_moves = tile.adjacent_move()
		r = random.randint(0, len(available_moves) - 1)
		self.do_action(available_moves[r])
	
