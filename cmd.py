
def join(player, argv, game):
    if game.round_number == -1:
        print('join: Starting a game!')
        return new_game(player, argv, game)
    elif game.round_number == 0:
        if player not in game.players:
            print('join: Adding player {} to the game!'.format(player.name))
            game.players.append(player)
        else:
            print('join: Player {} is already playing the game!'.format(player))
            return -1
    return 0

def leave(player, argv, game):
    if game.round_number == -1 or player not in game.players:
        print('leave: Player {} is not currently playing.'.format(player.name))
        return -1
    elif game.round_number == 0:
        i = game.players.index(player)
        game.players.pop(i)
        print('leave: Player {} has been removed from the player list.'.format(player.name))
    else:
        print('leave: The game has already begun. Quitting a game after it has begun is currently not supported.'.format(player.name))
        return -1
    return 0

def new_game(player, argv, game):
    if game.round_number == -1:
        print('new_game: Initiating a new game!')
        game.round_number = 0
    else:
        print('new_game: A game is already started.')
        return -1
    return 0

def start(player, argv, game):
    if game.round_number == 0:
        print('start: The game begins!')
        game.new_game()
    elif game.round_number == -1:
        print('start: No game was initiated.')
        return -1
    elif game.round_number > 0:
        print('start: The game has already begun.')
        return -1
    return 0

def rm(player, argv, game):
    if len(argv) < 2:
        print('rm: please specify the index of the item you want to remove')
        return -1
    try:
        i = int(argv[1])
        env['todo_list'].pop(i)
        return 0
    except ValueError:
        print('rm: failed to interpret "{}" as a list index'.format(argv[1]))
        return -1
    except IndexError:
        print('rm: index out of range')
        return -1

def quit(player, argv, game):
    env['didntQuit'] = False
    return 0

def notfound(player, argv, game):
    print('{}: {}: command not found'.format('replname', argv[0]))
    return -1

cmd_dict = {'join': join, 'leave': leave, 'new_game': new_game, 'start': start, 'quit': quit}
