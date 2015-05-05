import Tiles

_world = {[None, None, None, None, CastleExit, None, None, None],
	 [None, None, None, None, StupidAnimalRoom, None, None, None],
	 [None,None,EmptyCastleRoom, None, FindWoodenSword, None, None, None],
	 [FindGoldRoom69, SpookySkeletonRoom, FindWoodenStaff, StartingRoom, FindWoodenBow, MoistSlimeRoom, FindGoldRoom1],
	[None, None, MoistSlimeRoom, None, FindWoodenAxeRoom, None, None, None],
	[None, None, FindGoldRoom5, None, MoistSlimeRoom, None, None, None]}


def tile_exists(x, y):
	print(x, y, "rgws ")
	print(_world.get ((x, y)))
	return _world.get((x, y))



def load_tiles():
	
#	with open('resources/map.txt','r') as f:
#		rows = f.readlines()
#	x_max = len(rows[0].split('\t'))
#	for y in range(len(rows)):
#		cols = rows[y].split('\t')
#		for x in range(x_max):
#			print(x,"FIFI----")
#			Tile_name = cols[x].replace('\n','')
#			print (Tile_name,"----Done")
#			_world[(x, y)] = None if Tile_name == ''else getattr(__import__('Tiles'), Tile_name)(x, y)
