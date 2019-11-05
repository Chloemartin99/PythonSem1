
def is_straight(self):
    self.cards.sort()

    # special case A 2 3 4 5 (2 3 4 5 A)
    if self.cards[0].get_rank() == "2" and \
            self.cards[1].get_rank() == "3" and \
            self.cards[2].get_rank() == "4" and \
            self.cards[3].get_rank() == "5" and \
            self.cards[4] == "A":
        return True

    for i in range(4):
        if ranks.index(self.cards[0].get_rank()) + 1 != ranks.index(self.cards[i+1].get_rank()):
            return False
        return True

   # return True

def __lt__(self, other):
    return ranks.index(self.get_rank()) < ranks.index(other.get_rank())
