import Cards


class Game(object):

    def __init__(self, num_decks=1, players=1):
        # Instantiate player objects
        self.players = []
        for x in range(players):
            self.players.append(Player())

        # Instantiate dealer
        self.players.append(Player(money=0))

        # Instantiate card deck
        self.cards = Cards.CardDeck(decks=num_decks)

    def deal(self, reshuffle=True):

        # Reshuffle the deck
        if reshuffle:
            self.cards.shuffle()

        # Deal each player a hand
        for x, player in enumerate(self.players):
            money = player.money

            # Get legal bet, ignore dealer
            if x < len(self.players) - 1:

                # Check if player has money
                if money <= 0:
                    print(" Player " + str(x) + " you're out of money!")
                    player.set_hand([], 0)
                    continue

                while True:
                    try:
                        bet = int(input("Player " + str(x) + ", how much do you want to bet? \nYou have " + str(money) + " dollars."))
                        assert(0 < bet <= money)
                    except ValueError:
                        print("Input an integer value.")
                    except AssertionError:
                        print("You can't bet less than 0 or more than you have!")
                    else:
                        break
            else:
                # Dealer's bet is 0
                bet = 0

            # Deal hand & assign data to player object
            hand = self.cards.deal(2)
            player.set_hand(hand, bet)

    def play_round(self, reshuffle=True):
        self.deal(reshuffle=reshuffle)

        for x, player in enumerate(self.players):
            hand = player.hand

            if x == len(self.players) - 1:
                # Handle dealer's hand
                print("Dealer's hand:")
                while True:
                    show_hand(hand)
                    dealer_sum = sum_hand(hand)
                    if dealer_sum < 17:
                        # Dealer hits until sum >= 17
                        player.hit(self.cards.deal(1))
                    else:
                        # Break while loop
                        break
                # Skip below code fore dealer
                continue
            # Handle players out of money (bet = 0, otherwise this is not allowed except for the dealer)
            elif player.bet == 0:
                print("Skipping player " + str(x) + " who is broke.")
                continue

            # Announce player's turn
            print("Your turn, player " + str(x) + ".")

            # Stay on this player until pass or bust
            while True:
                show_hand(hand)
                this_sum = sum_hand(hand)
                if this_sum >= 21:
                    break
                elif this_sum < 21:
                    while True:
                        hit_stand = input("Would you like to hit or stand?")
                        if hit_stand == 'hit' or hit_stand == 'stand':
                            break
                    if hit_stand == 'stand':
                        # Player chose to stand, break from loop, go to next player in for loop
                        break
                    else:
                        # Player chose to hit
                        player.hit(self.cards.deal(1))

        # Resolve hands
        dealer_position = len(self.players) - 1
        dealer = self.players[dealer_position]
        dealer_sum = sum_hand(dealer.hand)
        dealer_bust = dealer_sum > 21

        # Iterate through non-dealer hands
        for x, position in enumerate(range(dealer_position)):
            player = self.players[position]

            # Skip broke players
            if player.bet == 0:
                print("Player " + str(x) + " is still broke.")
                continue

            hand_sum = sum_hand(player.hand)

            # Message that's always unchanged
            print("Player " + str(x), end='')

            # Check for bust, blackjack, and beating dealer
            if hand_sum == 21:
                print(", you got a blackjack!")
                player.blackjack()
            elif hand_sum > 21:
                print(", you bust!")
                player.lose_bet()
            elif hand_sum > dealer_sum or dealer_bust:
                print(", you beat the dealer!")
                player.beat_dealer()
            else:
                print(", the dealer beat you!")
                player.lose_bet()

            # Update user to their money
            print("You now have " + str(player.money) + " dollars.")


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


class Player(object):

    def __init__(self, money=100):
        self.money = money
        self.hand = []
        self.bet = 0

    def set_hand(self, hand, bet):
        # hand should be a list of card tuples
        # bet should be a number (should support int or float)
        self.hand = hand
        self.bet = bet

    def hit(self, cards):
        for card in cards:
            self.hand.append(card)

    def blackjack(self):
        self.money += int(self.bet * 1.5)

    def beat_dealer(self):
        self.money += self.bet

    def lose_bet(self):
        self.money -= self.bet


def show_hand(hand):
    for card in hand:
        print(card, end=', ')
    print('\nSum: ' + str(sum_hand(hand)))
