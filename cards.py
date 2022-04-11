import random

class Card:
    def __init__(self, name, suit, rank, tags = [], text = '', effect = None):
        self.name = name
        self.suit = suit
        self.rank = rank
        self.tags = tags
        self.text = text
        self.effect = effect

class Objective:
    def __init__(self, name, first_card, text, key):
        self.name = name
        self.first_card = first_card
        self.text = text
        self.key = key

plain_deck = [
    Card(" d'".join((str(rank), suit)), suit, rank)
    for rank in range(1,11) for suit in ('Amour', 'Courage', 'Sagesse')
] + [
    Card('Joker ' + x, 'Joker', 'Joker')
    for x in 'ABCDEF'
]

objectives = [
    Objective(' '.join((direction, suit)),
              random.choice(plain_deck),
              ' '.join((direction, suit)),
              lambda p: sum(1 for card in (p.allies + p.hand) if card.suit == suit) * (1 if direction == 'Most' else -1)
    )
    for direction in ('Most', 'Least') for suit in ('Amour', 'Courage', 'Sagesse')
]

special_powers = [
    ('Cannot win points this round', None),
    ('Worth 3 allies', None),
    ('Rank strength is decreasing this meeting', None),
    ("1 card from a player's hand to discard", None),
    ("1 card from a player's allies or discard to hand", None)
]

joker_powers = list(special_powers)

def random_objective():
    return random.choice(objectives)

def random_powers(k = 10):
    return random.choices(special_powers, k = k)

def random_jokers(k = 6):
    return random.choices(joker_powers, k = k)
