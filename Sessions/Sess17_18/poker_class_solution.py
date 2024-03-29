import random
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def is_pair(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True
        return False

    def is_straight(self):
        self.cards.sort()

        # special case A 2 3 4 5 (2 3 4 5 A)
        if self.cards[0].get_rank() == "2" and \
                self.cards[1].get_rank() == "3" and \
                self.cards[2].get_rank() == "4" and \
                self.cards[3].get_rank() == "5" and \
                self.cards[4].get_rank() == "A":
            return True

        for i in range(4):
            if ranks.index(self.cards[0].get_rank()) + 1 != ranks.index(self.cards[i + 1].get_rank()):
                return False
            return True

    # return True

    def __lt__(self, other):
        return ranks.index(self.get_rank()) < ranks.index(other.get_rank())

    #four of a kind: its either 25555 or 6666A (when you have sorted it): /
    # if number 2 != number 4 --> false or if




new_deck = Deck()
new_deck.shuffle()
print(new_deck)
hand = Hand(new_deck)
print(hand)


