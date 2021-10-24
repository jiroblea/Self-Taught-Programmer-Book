# the program was copied from the book
# I fixed the bug that may occur when the players draw--the output looks like this: "The War is over. It was a tie wins!""

from random import shuffle

class Card():
    suits = ["spades", "hearts", "diamonds", "clubs"] 
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    def __init__(self, value, suit) -> None:
        """suit and value should be integers"""
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            return False
        return False
    
    def __repr__(self) -> str:
        return self.values[self.value] + " of " + self.suits[self.suit]

class Deck():
    def __init__(self) -> None:
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
    
    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player():
    def __init__(self, name) -> None:
        self.wins = 0
        self.card = None
        self.name = name

class Game():
    def __init__(self) -> None:
        name1 = input("player 1 name: ")
        name2 = input("player 2 name: ")
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def play_game(self):
        cards = self.deck.cards
        print("Beginning War!\n")
        response = None
        while len(cards) >= 2 and response != "q":
            player1_card = self.deck.remove_card()
            player2_card = self.deck.remove_card()
            print("{} drew {}, {} drew {}".format(self.player1.name, player1_card, self.player2.name, player2_card))

            if player1_card > player2_card:
                self.player1.wins += 1
                print("{} wins this round".format(self.player1.name))
            else:
                self.player2.wins += 1
                print("{} wins this round".format(self.player2.name))

            response = input("\nq to quit. Any other key to play: ").lower()    # moved it from the top to quit after pressing q

        # the code I added
        if self.winner(self.player1, self.player2) == self.player1.name:
            print(f"\nThe War is over. {self.player1.name} wins!")
        elif self.winner(self.player1, self.player2) == self.player2.name:
            print(f"\nThe War is over. {self.player2.name} wins!")
        else:
            print("\nThe War is over. {}".format(self.winner(self.player1, self.player2)))

    def winner(self, player1, player2):
        if player1.wins > player2.wins:
            return player1.name
        elif player1.wins < player2.wins:
            return player2.name
        else:
            return "It was a tie!"
        

game = Game()
game.play_game()
