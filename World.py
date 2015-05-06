import Tiles

_world = {}

def tile_exists(x, y):
	print("Checking for a room tile...")
	return _world.get((0, 0))

def load_tiles():
	print("Loading Tiles...null")
	_world[(0, 0)] = Tiles.StartingRoom(0, 0)

#	with open('resources/map.txt','r') as f:
#		rows = f.readlines()
#		x_max = len(rows[0].split('\t'))
#		for y in range(len(rows)):
#			cols = rows[y].split('\t')
#
#		for x in range(x_max):
#			Tile_name = cols[x].replace('\n','')
#			_world[(x, y)] = None if Tile_name == ''else getattr(__import__('Tiles'), Tile_name)(x, y)
