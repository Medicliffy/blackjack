import Blackjack


def play_game(decks=1):

    while True:
        try:
            num_players = int(input("How many players do you want?"))
        except ValueError:
            print("Insert an integer.")
        else:
            break

    game = Blackjack.Game(num_decks=decks, players=num_players)

    while True:
        game.play_round()

        play_again = input("Would you like to play another round?")
        play_again.lower()
        if play_again.startswith("y"):
            continue
        else:
            break

if __name__ == '__main__':
    play_game()
