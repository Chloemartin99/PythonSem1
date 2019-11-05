#poker homework
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
        pair_rank = ''
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    pair_rank = self.cards[i].get_rank()
                    return True, pair_rank
        return False, pair_rank

    def is_two_pair(self):
        pairs_rank = []
        counter = 0
        for i in range(5):
            for j in range(i + 1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    counter += 1
                    pairs_rank.append(self.cards[i].get_rank())

        if counter == 2:
            return True, pairs_rank
        else:
            return False, pairs_rank

    def is_flush(self):
        check = True
        suit = self.cards[0].get_suit()
        for i in range(5):
            if self.cards[i].get_suit()!=suit:
                check= False
                break

        return check

    def is_straight(self):
        check = True

        rank_numbers = []
        for i in range(5):
            number = ranks.index(self.cards[i].get_rank())
            rank_numbers.append(number)

        rank_numbers.sort()

        for i in range(5):
            j = i + 1
            if j < 5:
                if rank_numbers[j] - rank_numbers[i] != 1:
                    check = False
                    break
        return check

    def is_straight_flush(self):
        check = True
        if hand.is_flush() == False:
            check= False

        else:
            rank_numbers = []
            for i in range(5):
                number = ranks.index(self.cards[i].get_rank())
                rank_numbers.append(number)

            rank_numbers.sort()

            for i in range(5):
                j = i + 1
                if j < 5:
                    if rank_numbers[j] - rank_numbers[i] != 1:
                        check = False
                        break
        return check

    def is_royal_flush(self):  # A, K, Q, J, 10, all the same suit.
        check = True

        if hand.is_flush() == False:
            check = False

        else:
            royal = ["A", "K", "Q", "J", "10"]
            for i in range(5):
                for r in royal:
                    if self.cards[i].get_rank()!=r:
                        check = False
                        break
        return check

    def is_x_of_a_kind(self):
        condition, pair_rank = hand.is_pair()
        counter = 0
        if condition == False:
            return False, 0

        else:
            for i in range(5):
                if self.cards[i].get_rank() == pair_rank:
                    counter+=1

        if counter==4:
            return True, 4

        elif counter==3:
            return True, 3

        else:
            return False, 0

    def is_full_house(self):
        check = True
        bool, pairs_rank = hand.is_two_pair()

        if bool == False:
            check = False

        elif bool == True:
            for i in range(5):
                if self.cards[i].get_rank()!= pairs_rank[0] or self.cards[i].get_rank()!= pairs_rank[1]:
                    check = False
                    break
        return check

royal_flush = 0
straight_flush = 0
four_of_a_kind = 0
full_house = 0
flush = 0
straight = 0
three_of_a_kind = 0
two_pair = 0
pair = 0
nothing = 0

count = 0

while count<25:
    new_deck = Deck()
    new_deck.shuffle()
    print(new_deck)
    hand = Hand(new_deck)
    print(hand)

    if hand.is_royal_flush() == True:
        royal_flush+=1
        print('Royal Flush')
        continue

    elif hand.is_straight_flush() == True:
        straight_flush+=1
        print('Straight Flush')
        continue

    elif (True, 4) in hand.is_x_of_a_kind():
        four_of_a_kind+=1
        print('Four of a Kind')
        continue

    elif hand.is_full_house() == True:
        full_house+=1
        print('Full House')
        continue

    elif hand.is_flush() == True:
        flush+=1
        print('Flush')
        continue

    elif hand.is_straight() == True:
        straight+=1
        print('Straight')
        continue

    elif (True, 3) in hand.is_x_of_a_kind():
        three_of_a_kind+=1
        print('Three of a Kind')
        continue

    elif True in hand.is_two_pair():
        two_pair+=1
        print('Two Pair')
        continue

    elif True in hand.is_pair():
        pair+=1
        print('Pair')

    else:
        nothing+=1
        print('Nothing')

    count+=1

print('Summary & statistics out of 10000 hands: ')
print('     Royal Flush: ',royal_flush,' times. Probability:  ',royal_flush/10000)
print('     Straight Flush: ',straight_flush,' times. Probability:  ',straight_flush/10000)
print('     Four of a Kind: ',four_of_a_kind,' times. Probability:  ',four_of_a_kind/10000)
print('     Full House: ',full_house,' times. Probability:  ',full_house/10000)
print('     Flush: ',flush,' times. Probability:  ',flush/10000)
print('     Straight: ',straight,' times. Probability:  ',straight/10000)
print('     Three of a Kihd: ',three_of_a_kind,' times. Probability:  ',three_of_a_kind/10000)
print('     Two Pair: ',two_pair,' times. Probability:  ',two_pair/10000)
print('     Pair: ',pair,' times. Probability:  ',pair/10000)
print('     Nothing: ',nothing,' times. Probability:  ',nothing/10000)