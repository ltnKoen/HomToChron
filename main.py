#! /usr/bin/env python3

import cmd
from game import Game, Player

env = {
    'prompt': '$ ',
    'replname': 'HomToChron',
    'didntQuit': True
}

def print_return_value(ret, argv):
    if ret != 0:
        print('{}: command {} failed with return value {}'.format(env['replname'], argv[0], ret))

def read_input(env):
    v = input(env['prompt']).strip().split()
    if len(v) < 2:
        print('{}: please specify player name followed by your command'.format(env['replname']))
        return v[0], v
    else:
        player_name, *argv = v
        return player_name, argv

def main():
    print('hello and welcome')
    game = Game()
    game.players = [Player(x) for x in 'abc']
    while env['didntQuit']:
        player_name, argv = read_input(env)    # read
        player = game.get_player(player_name)
        ret = cmd.cmd_dict.get(argv[0], cmd.notfound)(player, argv, game)   # eval
        print_return_value(ret, argv)                         # error message

if __name__ == '__main__':
    main()
