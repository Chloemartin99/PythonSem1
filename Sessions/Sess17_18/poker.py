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
                    if self.cards[i].get_rank() in pairs_rank:
                        break
                    else:
                        counter += 1
                        pairs_rank.append(self.cards[i].get_rank())
        if counter == 2:
            return True, pairs_rank

        else:
            return False, pairs_rank

    def is_flush(self):
        suit = self.cards[0].get_suit()
        for i in range(5):
            if self.cards[i].get_suit()!=suit:
                return False
        return True

    def is_straight(self):
        rank_numbers = []
        for i in range(5):
            number = ranks.index(self.cards[i].get_rank())
            rank_numbers.append(number)

        rank_numbers.sort()
        for i in range(5):
            j = i + 1
            if j < 5:
                if rank_numbers[j] - rank_numbers[i] != 1:
                    return False
        return True

    def is_straight_flush(self):
        if hand.is_flush() == False:
            return False

        else:
            rank_numbers = []
            for i in range(5):
                number = ranks.index(self.cards[i].get_rank())
                rank_numbers.append(number)

            rank_numbers.sort()
            if rank_numbers[0] == 0 and \
                    rank_numbers[1] == 1 and \
                    rank_numbers[2] == 2 and \
                    rank_numbers[3] == 3 and \
                    rank_numbers[4] == 12:
                return True

            for i in range(5):
                j = i + 1
                if j < 5:
                    if rank_numbers[j] - rank_numbers[i] != 1:
                        return False
                    else:
                        return True

    def is_royal_flush(self):  # A, K, Q, J, 10, all the same suit.
        if hand.is_flush() == False:
            return False

        else:
            rank_numbers = []
            for i in range(5):
                number = ranks.index(self.cards[i].get_rank())
                rank_numbers.append(number)

            rank_numbers.sort()
            if rank_numbers[0] == 8 and \
                    rank_numbers[1] == 9 and \
                    rank_numbers[2] == 10 and \
                    rank_numbers[3] == 11 and \
                    rank_numbers[4] == 12:
                return True
        return False

    def is_x_of_a_kind(self):
        counter = 0
        condition, pair_rank = hand.is_pair()

        if condition == False:
            return 0

        for i in range(5):
            if self.cards[i].get_rank() == pair_rank:
                counter+=1
        if counter==4:
            return 4
        elif counter==3:
            return 3
        else:
            return 0

    def is_three_of_a_kind(self):
        if hand.is_x_of_a_kind() == 3:
            return True

    def is_four_of_a_kind(self):
        if hand.is_x_of_a_kind() == 4:
            return True

    def is_full_house(self):
        condition, pairs_rank = hand.is_two_pair()
        if condition == False:
            return False

        else:
            remaining_card = []
            for i in range(5):
                remaining_card.append(self.cards[i].get_rank())

            for i in range(2):
                while pairs_rank[i] in remaining_card:
                    remaining_card.remove(pairs_rank[i])

            if len(remaining_card) == 0:
                return True

            else:
                return False

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

for count in range(100):
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

    elif hand.is_four_of_a_kind() == True:
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

    elif hand.is_three_of_a_kind() == True:
        three_of_a_kind += 1
        print('Three of a Kind')
        continue

    elif True in hand.is_two_pair():
        two_pair+=1
        print('Two Pair')
        continue

    elif True in hand.is_pair():
        pair+=1
        print('Pair')
        continue

    else:
        nothing+=1
        print('Nothing')

print('Summary & statistics out of 10000 hands: ')
print('     Royal Flush: ',royal_flush,' times. Probability:  ', (royal_flush/10000))
print('     Straight Flush: ',straight_flush,' times. Probability:  ',straight_flush/10000)
print('     Four of a Kind: ',four_of_a_kind,' times. Probability:  ',four_of_a_kind/10000)
print('     Full House: ',full_house,' times. Probability:  ',full_house/10000)
print('     Flush: ',flush,' times. Probability:  ',flush/10000)
print('     Straight: ',straight,' times. Probability:  ',straight/10000)
print('     Three of a Kihd: ',three_of_a_kind,' times. Probability:  ',three_of_a_kind/10000)
print('     Two Pair: ',two_pair,' times. Probability:  ',two_pair/10000)
print('     Pair: ',pair,' times. Probability:  ',pair/10000)
print('     Nothing: ',nothing,' times. Probability:  ',nothing/10000)

total = royal_flush+straight_flush+four_of_a_kind+full_house+flush+straight+three_of_a_kind+two_pair+pair+nothing