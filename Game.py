import World
from Player import Player 

def play():
    World.load_tiles()
    gamePlayer = Player()
    while gamePlayer.is_alive() and not gamePlayer.victory:
        room = World.tile_exists(gamePlayer.location_x, gamePlayer.location_y)
        room.modify_Player(gamePlayer)
        if gamePlayer.is_alive() and not gamePlayer.victory:
            print   ("What will you do?:\n")
            available_actions = room.available_Actions()
            for action in available_actions:
                print   (action)
            Action_input = raw_input('Action: ')
            for checkAction in available_actions:
                if Action_input == checkAction.hotkey:
                        gamePlayer.do_action(checkAction, **checkAction.kwargs)
                        break


if __name__ == "__main__":
    play()
