import Tiles

_world = {}

def tile_exists(x, y):
	return _world.get((x, y))

def load_tiles():
        
        _world[(0, -3)] = Tiles.FindBowOfLightBowRoom(0, -3)

        _world[(0, -2)] = Tiles.EmptyCastleRoom(0, -2)
        
        
        _world[(0, -1)] = Tiles.StupidAnimalRoom(0, -1)
        
	
        _world[(-5, 0)] = Tiles.FindMythrilAxeRoom(-5, 0)
        _world[(-2, 0)] = Tiles.EmptyCastleRoom(-2, 0)
        _world[(-1, 0)] = Tiles.EmptyCastleRoom(-1, 0)
	_world[(0, 0)] = Tiles.StartingRoom(0, 0)
	_world[(1, 0)] = Tiles.FindWoodenStaffRoom(1, 0)
	_world[(3, 0)] = Tiles.SpookySkeletonRoom(3, 0)
	_world[(4, 0)] = Tiles.EmptyCastleRoom(4, 0)
	_world[(5, 0)] = Tiles.EmptyCastleRoom(5, 0)

        _world[(-5, 1)] = Tiles.EmptyCastleRoom(-5, 1)
        _world[(-2, 1)] = Tiles.StartingRoom(-2, 1)
	_world[(0, 1)] = Tiles.FindWoodenAxeRoom(0, 1)
	_world[(1, 1)] = Tiles.EmptyCastleRoom(1, 1)
	_world[(2, 1)] = Tiles.EmptyCastleRoom(2, 1)
	_world[(3, 1)] = Tiles.EmptyCastleRoom(3, 1)
	_world[(5, 1)] = Tiles.FindValerianSteelSwordRoom(5, 1)

	
	_world[(-5, 2)] = Tiles.EmptyCastleRoom(-5, 2)
	_world[(-4, 2)] = Tiles.EmptyCastleRoom(-4, 2)
	_world[(-3, 2)] = Tiles.EmptyCastleRoom(-3, 2)
	_world[(-2, 2)] = Tiles.EmptyCastleRoom(-2, 2)
	_world[(3, 2)] = Tiles.EmptyCastleRoom(3, 2)

	_world[(-2, 3)] = Tiles.EmptyCastleRoom(-2, 3)
	_world[(3, 3)] = Tiles.EmptyCastleRoom(3, 3)

        _world[(3, 4)] = Tiles.EmptyCastleRoom(3, 4)
        _world[(4, 4)] = Tiles.EmptyCastleRoom(4, 4)
	_world[(5, 4)] = Tiles.EmptyCastleRoom(-2, 4)
	
	_world[(-2, 5)] = Tiles.EmptyCastleRoom(-2, 5)
	_world[(-1, 5)] = Tiles.FindIronAxeRoom(-1, 5)
	_world[(0, 5)] = Tiles.FindUnobtainiumStaffRoom(0, 5)
	_world[(1, 5)] = Tiles.EmptyCastleRoom(1, 5)
	_world[(2, 5)] = Tiles.EmptyCastleRoom(2, 5)
	_world[(3, 5)] = Tiles.CastleExit(3, 5)
	
	
	


#	with open('resources/map.txt','r') as fa:
#		rows = f.readlines()
#		x_max = len(rows[0].split('\t'))
#		for y in range(len(rows)):
#			cols = rows[y].split('\t')
#
#		for x in range(x_max):
#			Tile_name = cols[x].replace('\n','')
#			_world[(x, y)] = None if Tile_name == ''else getattr(__import__('Tiles'), Tile_name)(x, y)
