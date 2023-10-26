from random import randint, shuffle

cards = [
    "A♠", "A♠", "A♥", "A♣",
    "2♠", "2♦", "2♥", "2♣",
    "3♠", "3♦", "3♥", "3♣",
    "4♠", "4♦", "4♥", "4♣",
    "5♠", "5♦", "5♥", "5♣",
    "6♠", "6♦", "6♥", "6♣",
    "7♠", "7♦", "7♥", "7♣",
    "8♠", "8♦", "8♥", "8♣",
    "9♠", "9♦", "9♥", "9♣",
    "10♠", "10♦", "10♥", "10♣",
    "J♠", "J♦", "J♥", "J♣",
    "Q♠", "Q♦", "Q♥", "Q♣",
    "K♠", "K♦", "K♥", "K♣"
]

cardvalues = {
    "A♠":11, "A♠":11, "A♥":11, "A♣":11,
    "2♠":2, "2♦":2, "2♥":2, "2♣":2,
    "3♠":3, "3♦":3, "3♥":3, "3♣":3,
    "4♠":4, "4♦":4, "4♥":4, "4♣":4,
    "5♠":5, "5♦":5, "5♥":5, "5♣":5,
    "6♠":6, "6♦":6, "6♥":6, "6♣":6,
    "7♠":7, "7♦":7, "7♥":7, "7♣":7,
    "8♠":8, "8♦":8, "8♥":8, "8♣":8,
    "9♠":9, "9♦":9, "9♥":9, "9♣":9,
    "10♠":10, "10♦":10, "10♥":10, "10♣":10,
    "J♠":10, "J♦":10, "J♥":10, "J♣":10,
    "Q♠":10, "Q♦":10, "Q♥":10, "Q♣":10,
    "K♠":10, "K♦":10, "K♥":10, "K♣":10
}

def shufflecards():
    global cards
    shuffle(cards)

def deal():
    global dealerhand, userhand, counter, total, dealertotal
    userhand = []
    dealerhand = []
    counter = 0
    total = 0
    dealertotal = 0
    for _ in range(2):
        dealerhand.append(cards[counter])
        dealertotal += cardvalues[cards[counter]]
        counter += 1
        userhand.append(cards[counter])
        total += cardvalues[cards[counter]]
        counter += 1

def hit():
    userhand.append(cardvalues[cards[counter]])
    total += cardvalues[cards[counter]]
    counter += 1

def bust():
    if total > 21:
        return True

def blackjack():
    if len(userhand) == 2 and total == 21:
        return True

while True:
    shufflecards()
    deal()

    print(dealerhand, " ", dealertotal, "\n", userhand, " ", total)

    if blackjack():
        print("Blackjack")
        break