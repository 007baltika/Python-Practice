# Реализуйте генераторную функцию  card_deck() , которая принимает один аргумент:
# suit  — одна из четырех карточных мастей:  пик, треф, бубен, червей

# Функция должна возвращать генератор, циклично порождающий колоду игральных карт без
# масти  suit . 
# 
# Каждая карта должна представлять собой строку в следующем формате:
# <номинал> <масть>

def card_deck(suit = None):
    masts = ['пик', 'треф', 'бубен', 'червей']
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
    if suit != None: 
        masts.remove(suit)
    while True:
        for mast in masts:
            for card in cards:
                yield str(card) + ' ' + mast





# TEST_1:
generator = card_deck('пик')

print(next(generator))
print(next(generator))
print(next(generator))
print()
# TEST_2:
generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)
print()
# TEST_3:
generator = card_deck('бубен')

cards = [next(generator) for _ in range(50)]

print(*cards)
print()
# TEST_4:
generator = card_deck('червей')

cards = [next(generator) for _ in range(60)]

print(*cards)
print()
# TEST_5:
generator = card_deck('пик')

cards = [next(generator) for _ in range(80)]

print(*cards)