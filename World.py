import Tiles

_world = {}

def tile_exists(x, y):
	print(_world.get ((x, y)))
	return _world.get((x, y))

def load_tiles():	
	with open('resources/map.txt','r') as f:
		rows = f.readlines()
	x_max = len(rows[0].split('\t'))
	for y in range(len(rows)):
		cols = rows[y].split('\t')
		for x in range(x_max):
			print(x,"FIFI----")
			Tile_name = cols[x].replace('\n','')
			print (Tile_name,"----Done")
			_world[(x, y)] = None if Tile_name == ''else getattr(__import__('Tiles'), Tile_name)(x, y)
