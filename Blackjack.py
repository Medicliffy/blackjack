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
                self.players[player] = list of cards in that player's hand
            """

            # Create list of players
            self.players.append([])

            # Append 2 cards to the hand list for each of the players
            for x in range(2):
                self.players[player].append(self.cards.deal())

    def hit(self, hand):
        # hand passed should be a list of cards
        # TODO: test
        hand.append(self.cards.deal(1))
        return hand

    @staticmethod
    def sum_hand(hand):
        res = 0

        # Used below to track A's counting for 1 or 11
        num_aces = 0

        # Get each card
        for card in hand:

            # Card object is ('suit', #)
            x = card[1]

            # handle 2-10
            if type(x) == int:
                res += x
            # handle J, Q, K, & A
            else:
                if x == 'J' or x == 'Q' or x == 'K':
                    res += 10
                elif x == 'A':
                    res += 11
                    num_aces += 1

        # Makes A's count for only 1 if hand otherwise will bust
        while num_aces > 0 and res > 21:
            res -= 10
            num_aces -= 1

        return res

    def play_round(self, players=1, reshuffle=True):
        self.deal(players=players, reshuffle=reshuffle)

        for player in self.players:
            hand = self.players[player]

            # TODO: handle dealer's hand
            # TODO: gather bets

            # Stay on this player until pass or bust
            while True:
                this_sum = sum(hand)
                if this_sum >= 21:
                    break
                elif this_sum < 21:
                    # TODO: option to hit or stand
                    pass

        # TODO: resolve hands


class Player(object):

    def __init__(self, money=100):
        hand_resolved = False
        bet = 0
        self.money = money
