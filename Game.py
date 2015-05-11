import World
from Player import Player

def play():
	World.load_tiles()
	player = Player()
	while player.is_alive() and not player.victory:
		room = World.tile_exists(player.location_x, player.location_y)
		room.modify_Player(player)
		if player.is_alive() and not player.victory:
			print	("What will you do?:\n")
			available_actions = room.available_Actions()
			for action in available_actions:
				print	(action)
			Action_input = raw_input('Action: ')
			for Action in available_actions:
				if Action_input == Action.hotkey:
					player.do_action(Action, **Action.kwargs)
				break


if __name__ == "__main__":
	play()
