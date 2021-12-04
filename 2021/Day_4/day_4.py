
from copy import deepcopy

class Bingo_Caller:
    def __init__(self):
        self.input = open('input.txt').read().splitlines()
        self.called = self.input.pop(0).split(',')
        self.bingo_cards = self.card_maker(self.input)

    def card_maker(self, cards):
        count = 1
        bingo_cards = {}
        bingo_card = []

        for row in cards:
            if row =='':
                bingo_cards['card_'+str(count)] = bingo_card
                bingo_card = []
                count+=1
            else:
                bingo_card.append(row.split())
        return bingo_cards

    def call_nums(self,part_one=True):
        bingo_cards = deepcopy(self.bingo_cards)
        winners = {}

        for num in self.called:
            for card, rows in bingo_cards.items():
                if card not in winners:
                    for idx, row in enumerate(rows):
                        if num in row:
                            row[row.index(num)] = 'x'
                            bingo_cards[card][idx] = row
            
                            if self.check_winner(bingo_cards[card]):         
                                if part_one: 
                                    return self.calculate(int(num), bingo_cards[card])

                                winners[card] = self.calculate(int(num),bingo_cards[card])

        return winners[list(winners.keys())[-1]]

    def check_winner(self,card):
        for i in range(5):
            column = []

            for row in card:
                if self.validate(row):
                    return True
                column.append(row[i])
            if self.validate(column):
                return True

    def validate(self, row):
        return all([num=='x' for num in row])

    def calculate(self,num, card):
        unmarked_sum = sum([int(x) for y in card for x in y if x != 'x'])
        
        return unmarked_sum*num

b = Bingo_Caller()
print(f'Part one: {b.call_nums()}')
print(f'Part two: {b.call_nums(part_one=False)}')



