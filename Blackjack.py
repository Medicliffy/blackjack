import Cards


class Game(object):

    def __init__(self, dealer=True, num_decks=1):
        self.dealer = dealer
        self.players = []
        self.cards = Cards.CardDeck(decks=num_decks)

    def deal(self, players=1, reshuffle=True):

        # Emtpy cards from previous hand
        self.players.clear()

        # Reshuffle the deck
        if reshuffle:
            self.cards.shuffle()

        # Deal each player a hand
        for player in players:
            """
            After this method:
                self.players = list of players
                self.players[player] = list of cards which is that player's hand
            """

            # Create list of players
            self.players.append([])

            # Append 2 cards to the hand list for each of the players
            for x in range(2):
                self.players[player].append(self.cards.deal())

    def hit(self):
        # def turn instead?
        # TODO
        pass

    # TODO: separate into hand object? (then overwrite what I think is __sum__?)
    @staticmethod
    def sum_hand(hand):
        res = 0

        # Get each card
        for card in hand:

            # Card object is ('suit', #)
            x = card(1)

            # handle 2-10
            if type(x) == int:
                res += x
            # handle J, Q, K, & A
            else:
                if x == 'J' or x == 'Q' or x == 'K':
                    res += 10
                elif x == 'A':
                    # Can only be 1 if 11 makes hand bust
                    if res + 11 > 21:
                        res += 1
                    else:
                        # TODO
                        pass

        return res

    # TODO: move into hand class if refactored to such
    @staticmethod
    def bust(self):
        # TODO
        pass

    def play_round(self, players=1, reshuffle=True):
        self.deal(players=players, reshuffle=reshuffle)

        for player in self.players:
            hand = self.players[player]

            # fixme: handle dealer's hand

            # Stay on this player until pass or bust
            while True:
                this_sum = sum(hand)
                if this_sum > 21:
                    Game.bust()
                    break
                elif this_sum == 21:
                    # TODO: implement blackjack
                    pass
                elif this_sum < 21:
                    # TODO: option to hit or stand
                    pass

                # TODO...need to do anything else?
                pass

            # TODO
            pass


class Player(object):
    # TODO
    pass
