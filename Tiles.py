import Items, Enemies, Actions, World

class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError()

	def modify_Player(self, the_Player):
		print("FIFI is here")
		
	def adjacent_moves(self):
		moves = []
		if world.tile_exists(self.x + 1, self.y):
			moves.append(Actions.MoveEast())
		if world.tile_exists(self.x - 1, self.y):
			moves.append(Actions.MoveWest())
		if world.tiles_exist(self.x, self.y + 1):
			moves.append(Actions.MoveNorth())
		if world.tiles_exists(self.x, self.y - 1):
			moves.append(Actions.MoveSouth())

		return moves

	def available_Actions(self):
		moves = self.adjecent_moves()
		moves.append(Actions.ViewInventory())

		return moves

class StartingRoom(MapTile):
	"""Start here FIFI you suck!"""
	def intro_text(self):
		return"""
		You find yourself in a long dank hallway. 
		You are compelled to move foward.
		"""
	def modify_Player(self, the_Player):
		pass

class LootRoom(MapTile):
	"""Put loot here"""
	def __init__(self, x, y, Items):
		self.Items = Items
		super().__init__(x, y)

	def add_loot(self, the_Player):
		the_Player.inventory.append(self.Items)
		
	def modify_Player(self, the_Player):
		self.add_loot(Player)

class EnemyRoom(MapTile):
	"""Lion lives here"""
	def __init__(self, x, y, Enemy):
		self.Enemy = Enemy
		super().__init__(x, y)

	def modify_Player(self, the_Player):
		if self.Enemy.is_alive():
			the_Player.hp= th_Player.hp - self.Enemy.damage
			print("Enemy does {} damage. You have {} Hit Point.".format(self.Enemy.damage, the_Player.hp))

class EmptyCastleRoom(MapTile):
	"""Empty room"""
	def intro_text(self):
		return"""
		Another Empty room to the castle.
		Go away.
		"""

class StupidAnimalRoom(EnemyRoom):
	"""Stupid humans live here"""
	def __init__(self, x, y):
		super().__init__(x, y, Enemies.StupidAnimal())

	def intro_text(self):
		if self.enemy.is_alive():
			return"""
			you enter the room and are soon tackled by a stupid animal.
			"""
		else:
			return"""
			The stupid animal stupidly lies dead on the ground because its stupid
			"""
class SpookySkeletonRoom(EnemyRoom):
	"""Did you know dragons are better than undead?"""
	def __init__(self, x, y):
		super().__init__(x, y, Enemies.SpookySkeleton())
	def intro_init(self):
		if self.enemy.is_alive():
			return"""
			You are startled by the apperance of a Spooky Skeleton
			"""
		else:
			return"""
			The skeleton lies in peices it is far less spooky now
			"""
class MoistSlimeRoom(EnemyRoom):
	"""Wet and Nasty"""
	def __init__(self, x, y):
		super().__init__(x, y, Enemies.MoistSlime())

	def intro_text(self):
		if self.enemy.is_alive():
			return"""
			This room is moist... too wet. A Moist Slime Appears!
			"""
		else:
			return"""
			The Moist Slime's Moist corpse is on the ground Moistly... Moist
			"""

# item rooms

class FindWoodenStaffRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, Items.WoodenStaff())

	def intro_text(self):
		return"""
		You see a old man with a walking stick. Wood Staff Obtained 
		"""
class FindIronStaffRoom(LootRoom):
	"""Nice stick goes here"""
	def __init__(self, x, y):
		super().__init__(x, y, 	Items.IronStaff())

	def intro_text(self):
		return"""
		You find a broken wall torch. Iron Staff Obtained 
		"""
class FindSteelStaffRoom(LootRoom):
	"""Learning how of annel iron is good, eh?"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.SteelStaff())

	def intro_text(self):
		return"""
		Something shiny is on the floor.SteelS Staff Obtained!
		"""
class FindUnobtainiumStaffRoom(LootRoom):
	"""Ok Logan, your staff is ready."""
	def __init__(self, x, y):
		super().__init__(x, y, Items.Staff())

	def intro_text(self):
		return"""
		A very tall blue cat-man with a gross, feely tail gives you a stick. Unobtainium Staff Obtained
		"""
class FindWoodenSwordRoom(LootRoom):
	"""For the Anime fan"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.WoodenSword())

	def intro_text(self):
		return"""
		There is a child palying with a toy sword. Wooden Sword Obtained!
		"""
class FindIronSwordRoom(LootRoom):
	"""Not a light saber"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.IronSword())

	def intro_text(self):
		return"""
		You find a sword stuck in a pebble. Iron Sword obtained!
		"""
class FindSteelSwordRoom(LootRoom):
	"""Also not a light saber"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.SteelSword())

	def intro_text(self):
		return"""
		This one was definitely stuck in a rock. Steel Sword obtained!
		"""
class FindValerianSteelSwordRoom(LootRoom):
	"""Stick it to you!"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.ValerianSteelSword())

	def intro_text(self):
		return"""
		A blonde-haired woman with a dragon gives you a sword. Valerian Steel Sword obtained!
		"""
class FindWoodenAxeRoom(LootRoom):
	"""I have an Axe, Axe, Axe, Axe!"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.WoodenAxe())

	def intro_text(self):
		return"""
		There's a very square looking man punching trees. Wooden Axe obtained!
		"""
class FindIronAxeRoom(LootRoom):
	"""I like sticking it into your head!"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.IronAxe())

	def intro_text(self):
		return"""
		A crazed, bearded man throws an axe at you. Iron Axe obtained! 
		"""
class FindSteelAxeRoom(LootRoom):
	"""I steal axes!"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.SteelAxe())

	def intro_text(self):
		return"""
		A bandit lays asleep. Steel Axe obtained!
		"""
class FindMythrilAxeRoom(LootRoom):
	"""This one smells like butt"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.MythrilAxe())

	def intro_text(self):
		return"""
		A dwarf offers you his allegiance. You Take his axe. Mythril Axe obtained
		"""
class FindWoodenBowRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, Items.WoodenBow())

	def intro_text(self):
		return"""
		There's a small child playing with a toy swo-bow.Bow. Wooden Bow obtained!
		"""
class FindIronBowRoom(LootRoom):
	"""Hi there iron bow"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.IronBow())

	def intro_text(self):
		return"""
		A weirdly ornate bow is on the ground. Iron Bow obtained
		"""
class FindSteelBowRoom(LootRoom):
	"""Hi there steel bow"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.SteelBow())

	def intro_text(self):
		return"""
		There's a chest on the ground. du nu nu nuuuuuu! Steel bow obtained
		"""
class FindBowOfLightBowRoom(LootRoom):
	"""Hi there light bow"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.BowOfLightBow())

	def intro_text(self):
		return"""
		A green-clad boy hands youa shinning bow. Bow of Light Bow obtained!
		"""

#gold rooms
class FindGoldRoom1(LootRoom):
	"""Some gold"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.Gold(1))

		def intro_text(self):
			return"""
			I FOUND A PENNY! One Gold obtained!
			"""

class FindGoldRoom5(LootRoom):
	"""Lots of gold"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.Gold(5))

		def intro_text(self):
			return"""
			I found someone's wallet! Five Gold obtained!

			"""
class FindGoldRoom69(LootRoom):
	"""An obscene amount of gold"""
	def __init__(self, x, y):
		super().__init__(x, y, Items.Gold(69))

		def intro_text(self):
			return"""
			I found some Gold in the parking lot(don't ask questions)! 69 Gold obtained!
			"""

class CastleExit(MapTile):
	"""An exit"""
	def intro_text(self):
		return"""
		DOBBY IS FREE
		"""
	def modify_player(self, Player):
		Player.victory = True
