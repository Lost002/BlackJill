from random import randint, shuffle
from os import system

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
    global dealerhand, userhand, counter, total, dealertotal, bust
    userhand = []
    dealerhand = []
    counter = 0
    total = 0
    bust = False
    dealertotal = 0

    for _ in range(2):
        dealerhand.append(cards[counter])
        dealertotal += cardvalues[cards[counter]]
        counter += 1
        userhand.append(cards[counter])
        total += cardvalues[cards[counter]]
        counter += 1

def hit():
    global bust, counter, total
    userhand.append(cards[counter])
    total += cardvalues[cards[counter]]
    counter += 1
    for _ in userhand:
        if 'A' in _ and total > 21:
            total -= 10
    if total > 21:
        bust = True

def blackjack():
    if len(userhand) == 2 and total == 21:
        return True

def wlt():
    system("clear")
    for _ in dealerhand:
        print(_, end=" ")
    print(f" |  Total: {dealertotal}", end=" ")
    print("\n")
    for _ in userhand:
        print(_, end=" ")
    print(f" |  Total: {total}", end=" ")
    print("\n")

    if dealertotal > total:
        print("You lose...")
    elif total > dealertotal:
        print("You Win!")
    elif total == dealertotal:
        print("Tie!")

def AI():
    pass

shufflecards()
deal()

while True:
    if blackjack():
        system('clear')
        for _ in dealerhand:
            print(_, end=" ")
        print(f" |  Total: {dealertotal}", end=" ")
        print("\n")
        for _ in userhand:
            print(_, end=" ")
        print(f" |  Total: {total}", end=" ")
        print("Blackjack!\nYou Win.")
        break

    system('clear')
    print(dealerhand[0], "[]", end=" ")
    print("\n")
    for _ in userhand:
        print(_, end=" ")
    print(f" |  Total: {total}", end=" ")
    print("\n")
    H_S = input("Hit[H] or Stand[S]: ")

    if H_S == "H" or H_S == "h":
        hit()
    elif H_S == "S" or H_S == "s":
        wlt()
        break
    
    if bust:
        system('clear')
        for _ in dealerhand:
            print(_, end=" ")
        print(f" |  Total: {dealertotal}", end=" ")
        print("\n")
        for _ in userhand:
            print(_, end=" ")
        print(f" |  Total: {total}", end=" ")
        print("You Bust!\nYou Lose...")
        break