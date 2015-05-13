class Enemy(object):
	def	__init__(self, hp, name, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
		
	def is_alive(self):
		return self.hp > 0

class SpookySkeleton(Enemy):
	def __init__(self):
		super(SpookySkeleton, self).__init__(name="Enemy.SpookySkeleton", hp=15, damage=3)

class LackyJoblin(Enemy):
	def __init__(self):
		super(LackyJoblin, self).__init__(name="Enemy.LackyJoblin", hp=15, damage=2)

class StupidAnimal(Enemy):
	def __init__(self):
		super(StupidAnimal, self).__init__(name="Enemy.StupidAnimal", hp=5, damage=1)

class MoistSlime(Enemy):
	def __init__(self):
		super(MoistSlime, self).__init__(name="Enemy.MoistSlime", hp=10, damage=1)
