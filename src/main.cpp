#include <iostream>
#include <ctime>

std::string cards[52] = {
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
};
int values [52] = {
11,11,11,11,
2,2,2,2,
3,3,3,3,
4,4,4,4,
5,5,5,5,
6,6,6,6,
7,7,7,7,
8,8,8,8,
9,9,9,9,
10,10,10,10,
10,10,10,10,
10,10,10,10,
10,10,10,10
};

std::string hand[11];
std::string dealer[11];

int total = 0;
int counter = 1;

bool blackjack = false;

void deal() {
    srand(time(NULL));

    for (int i=0; i<2; i++) {
        int card = rand() % 52 + 1;

        while (cards[card] == "") {
            card = rand() % 52 + 1;
        }
        dealer[counter] = cards[card];

        cards[card] = "";
        for (int j=0; j<2; j++) {
            int card1 = rand() % 52 + 1;

            while (cards[card1] == "") {
                card1 = rand() % 52 + 1;
            }
            if (cards[card1] != "") {
                hand[counter] = cards[card1];
                total += values[counter];
            }
            if (total == 21) {
                blackjack == true;
            }
            cards[card1] = "";
        }
        counter += 1;
    }
}

int main() {
    bool stand = false;
    std::string choice;
    int cardchoice;
    deal();
    if (blackjack == false) {
        while (true) {
            std::system("clear");
            srand(time(NULL));
            std::cout << dealer[1] << " []\n\n";
            for (int z = 1; z<11; z++) {
                std::cout << hand[z] << " ";
            }
                
            std::cout << "\nHit[H] Stand[S]: "; std::cin >> choice;
            
            if (choice == "S" || choice == "s") {
                //stand = true;
                ;
            } else if (choice == "H" || choice == "h") {
                cardchoice = rand() % 52 + 1;
                while (cards[cardchoice] == "") {
                    cardchoice = rand() % 52 + 1;
                }
                if (cards[cardchoice] != "") {
                    cards[counter] = "";
                    hand[counter] = cards[cardchoice];
                    total += values[counter];
                    counter += 1;
                }
            }
            if (21 > total) {
                std::system("clear");
                for (int y = 1; y<12; y++) {
                    std::cout << dealer[y] << " ";
                }
                std::cout << "\n\n";
                for (int z = 1; z<12; z++) {
                    std::cout << hand[z] << " ";
                }
                std::cout << "\nBust!\nYou Lose:(\n";
                break;
            }
        }
    } else if (blackjack == true) {
        std::cout << dealer[1] << dealer[2] << "\n\n" << hand[1] << hand[2] << "\nBlackJack!\nYou Win!\n";
    }
}