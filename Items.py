

class Item():
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value
def __str__(self):
	return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)



class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name, description, value)
	def __str__(self):
		return "{}\n======\n{}\nValue: {}\nDamage:{}".format(self.name, self.description, self.value, self.damage)
class WoodenSword(Weapon):
	def __init__(self):
		super().__init__(name="Wooden Sword",
				description="Stick'em with the pointy end.",
				value=15,
				damage=6)
class IronSword(Weapon):
	def __init__(self):
		super().__init__(name="Iron Sword",
			description="An iron sword that cuts a little better than a wooden one.",
			value=25,
			damage=10)
class SteelSword(Weapon):
	def __init__(self):
		super().__init__(name="Steel Sword",
			description="A steel sword that is pretty good at cutting things.",
			value=40,
			damage=15)
class ValerianSteelSword(Weapon):
	def __init__(self):
		super().__init__(name="Valerian Steel Sword",
			description="Nothing holds an edge quite like Valerian Steel-Meorge GG no re Rartin.",
			value=60,
			damage=20)
class WoodenStaff(Weapon):
	def __init__(self):
		super().__init__(name="Wooden Staff",
				description="Beat'em with the less pointy end.",
				value=10,
				damage=4)
class IronStaff(Weapon):
	def __init__(self):
		super().__init__(name="Iron Staff",
			description="This thing is really heavy.",
			value=15,
			damage=8)
class SteelStaff(Weapon):
	def __init__(self):
		super().__init__(name="Steel Staff",
			description="This one is even heavier.",
			value=20,
			damage=12)
class UnobtainiumStaff(Weapon):
	def __init__(self):
		super().__init__(name="Unobtainium Staff",
			description="The Staff is just inconceviable.",
			value=99999999,
			damage=18)
class WoodenAxe(Weapon):
	def __init__(self):
		super().__init__(name="Wooden Axe",
				description="Hack n'Slash.",
				value=20,
				damage=8)
class IronAxe(Weapon):
	def __init__(self):
		super().__init__(name="Iron Axe",
			description="Hack'n Slash II: Electric Boogaloo",
			value=30,
			damage=12)
class SteelAxe(Weapon):
	def __init__(self):
		super().__init__(name="Steel Axe",
			description="Hack'n Slash III: This Time it's Personal",
			value=45,
			damage=18)
class MythrilAxe(Weapon):
	def __init__(self):
		super().__init__(name="Mithril Axe",
			description="It looks like it has Klingon carved into the blade. Wait, it's Elvish.",
			value=60,
			damage=27)
class WoodenBow(Weapon):
	def __init__(self):
		super().__init__(name="Wooden Bow",
				description="(?)-I Don't even know how to use this thing.",
				value=25,
				damage=11)
class IronBow(Weapon):
	def __init__(self):
		super().__init__(name="Iron Bow",
			description="Still no idea.",
			value=40,
			damage=17)
class SteelBow(Weapon):
	def __init__(self):
		super().__init__(name="Steel Bow",
			description="I've just been hitting them with the bow the whole time.",
			value=60,
			damage=26)
class BowOfLightBow(Weapon):
	def __init__(self):
		super().__init__(name="Bow of Light Bow",
			description="Why is it glowing?",
			value=90,
			damage=40)
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="It's a rock...duh.",
                         value=0,
                         damage=5)


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="{} round coin/s probably made of silver.".format(str(self.amt)),
                         value=self.amt)
