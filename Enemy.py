class Enemy(object):
	def	__init__(self, hp, name, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
		
	def is_alive(self):
		return self.hp > 0

class SpookySkeleton(Enemy):
	def __init__(self):
		super(SpookySkeleton, self).__init__(name="Spooky Skeleton", hp=15, damage=3)

class LackyJoblin(Enemy):
	def __init__(self):
		super(LackyJoblin, self).__init__(name="Lacky Joblin", hp=15, damage=2)

class StupidAnimal(Enemy):
	def __init__(self):
		super(StupidAnimal, self).__init__(name="Stupid Animal", hp=5, damage=1)

class MoistSlime(Enemy):
	def __init__(self):
		super(MoistSlime, self).__init__(name="Moist Slime", hp=10, damage=1)
class CEOJoblin(Enemy):
	def __init__(self):
		super(CEOJoblin, self).__init__(name="CEO Joblin", hp=69, damage=8)
class SimianAngle(Enemy):
	def __init__(self):
		super(SimianAngle, self).__init__(name="Simian Angle", hp=42, damage=6)
