"""
A Game of "War". 2 Players.
Each Player is dealt a card. The Player with the highest rank of Card wins the round.
Cards are ranked by face number value, "Jack", "Queen", "King", and then "Ace" is highest.
In the event of a tie the card suit value breaks the tie.
Suits are ranked alphabetically with "Spades" as the highest.
When all 52 cards are dealt, the Player with the most rounds won, wins "War".
"""

from random import shuffle

class Card:
    suits = ["clubs", "diamonds", "hearts", "spades"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"] # "None" in index 0 and 1 to align values to index.
    def __init__(self, v, s):
        """
        Value and Suit.
        :param v: int.
        :param s: int.
        """
        self.value = v
        self.suit = s
    def __lt__(self, c2):
        """
        Compares two Card and determines which is less than (lt) based on value then suit.
        """
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    def __gt__(self, c2):
        """
        Compares two Card and determines which is greater than (gt) based on value then suit.
        """
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    def __repr__(self):
        """
        Returns string with Card peramiters insted of Card memory location.
        """
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        """
        Make Deck of each Card combination.
        Shuffle Deck.
        """
        self.cards = []
        for i in range (2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    def rm_card(self):
        """
        Deals Card from Deck if not empty.
        """
        if len (self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        """
        Creates Player.
        Tracks hands won.
        Tracks Card currently played.
        :param name: str.
        """
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        """
        Creates Players.
        Creates deck tuple.
        """
        name1 = input("Enter Player 1 Name: ")
        name2 = input("Enter Player 2 Name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    def wins(self, winner):
        """
        Prints who won round.
        :param winner: str.
        """
        w = f"{winner} wins this round."
        print(w)
    def draw(self, p1n, p1c, p2n, p2c):
        """
        Prints Player Names and Cards they drew.
        :param p1n: str.
        :param p1c: Card Object.
        :param p2n: str.
        :param p1n: Card Object.

        """
        d = f"\n{p1n} drew {p1c}\n{p2n} drew {p2c}\n"
        print(d)
    def play_game(self):
        """
        Starts Game.
        """
        cards = self.deck.cards
        print("Beginning War!")
        while len(cards) >= 2:
            response = input("q to quit. Any key to play: ")
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print(f"\nWar is over. {win} wins!")
    def winner(self, p1, p2):
        """
        Determines winner based on wins tracked in Player.
        :param p1: str.
        :param p2: str.
        """
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Tie! Nobody"

def play_war():
    game = Game()
    game.play_game()

def show_deck():
    deck = Deck()
    for card in deck.cards:
        print(card)

play_war()

# show_deck()