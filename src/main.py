from random import randint

shuffleSeed = ""

cards = {
    "A♠":1, "A♠":1, "A♥":1, "A♣":1,
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

def shuffle():
    global shuffleSeed
    used = []
    for _ in range(52):
        number = randint(0,52)
        if number not in used:
            shuffleSeed += str(number)+"%"
            used.append(number)
    print(shuffleSeed)

shuffle()