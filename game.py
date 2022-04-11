from enum import Enum
from random import shuffle
import cards

class Player:
    def __init__(self, name, ident = 42):
        self.ident = ident
        self.name = name
        self.hand = []
        self.allies = []

# 'meeting' is just a fancy name for 'trick'
class Meeting:
    def __init__(self, players, suit = None):
        self.players = players
        self.suit = suit
        self.card = {p: None for p in players}

# class Status(enum):
#
# statuses = ['init', '']
class Game:
    def __init__(self):
        #self.status = ''
        self.round_number  = -1
        self.meeting_number = 0
        self.players = []
        self.meeting = None
        self.objective = None
    def new_game(self):
        self.round_number = -1
        self.new_round()
    def new_round(self):
        self.round_number += 1
        self.objective = cards.random_objective()
        suit_powers = cards.random_powers(10)
        joker_powers = iter(cards.random_jokers(6))
        self.deck = list(cards.plain_deck)
        for card in self.deck:
            if card.suit == 'Joker':
                card.text, card.effect = next(joker_powers)
            else:
                card.text, card.effect = suit_powers[card.rank - 1]
        shuffle(self.deck)
    def get_player(self, player_name):
        return next((p for p in self.players if p.name == player_name), None)
