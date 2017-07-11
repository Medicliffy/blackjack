import random


class CardDeck(object):
    suits = ['heart', 'diamond', 'spade', 'club']
    numbers = [x for x in range(2, 11)] + ['J', 'Q', 'K', 'A']

    def __init__(self, decks=1, shuffled=True):

        self.my_deck = []
        self.counter = 0

        for x in range(decks):
            for suit in CardDeck.suits:
                suit_instance = [(suit, x) for x in CardDeck.numbers]
                for card in suit_instance:
                    self.my_deck.append(card)

        if shuffled:
            self.shuffle()

    def shuffle(self):
        # sort with random number as key - lambda to take but ignore parameter
        self.my_deck.sort(key=lambda x: random.random())

        # set counter to point back a top of deck
        self.counter = 0

    def deal(self, num=1):
        # returns a list with the requested number of cards
        # if you attempt to deal from an empty deck, it will reshuffle to deck for you
        res = []
        for x in range(num):
            try:
                res.append(self.my_deck[self.counter])
            except IndexError:
                print("You already dealt the entire deck! I'll shuffle all the cards for you.")
                self.shuffle()
                res.append(self.my_deck[self.counter])
            finally:
                self.counter += 1
        return res