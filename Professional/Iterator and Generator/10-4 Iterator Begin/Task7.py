# Реализуйте класс  CardDeck , порождающий итераторы, конструктор которого не принимает
# никаких аргументов.
# Итератор класса  CardDeck  должен генерировать последовательность из 52 игральных карт, а
# после возбуждать исключение  StopIteration . Каждая карта должна представлять собой
# строку в следующем формате:

class CardDeck:
    
    def __init__(self):
        self.mast = ['пик', 'треф', 'бубен', 'червей']
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
        self.mast_start = 0
        self.card_start = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.mast_start < len(self.mast):
            card = str(self.cards[self.card_start]) +' '+ self.mast[self.mast_start]
            self.card_start += 1
            if self.card_start == len(self.cards):
                self.mast_start += 1
                self.card_start = 0
                return card
            else: return card
        else: raise StopIteration    
        
    
    
# TEST_1:
cards = CardDeck()

print(next(cards))
print(next(cards))
print()
# TEST_2:
cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])
print()
# TEST_3:
cards = list(CardDeck())

print(cards)
print()
# TEST_4:
cards1 = list(CardDeck())
cards2 = tuple(CardDeck())
cards3 = list(CardDeck())

print(cards1)
print(cards2)
print(cards3)
print()
# TEST_5:
cards = list(CardDeck())

try:
    next(cards)
except:
    print('Error')  