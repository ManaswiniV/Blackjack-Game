import random

suits = ["Hearts","Diamonds","Spades","Clubs"]
pack = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
line = "-------------------------------------------------------------"

print("Welcome to Blackjack")
print(line)

# Function to print the cards in hand
def printcards(hand):
    for suit,value in hand:
        print(f"({suit} : {value})",end=" ")
    print("")

# Function to deal a card from the deck
def dealCard(hand,deck):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)
    random.shuffle(deck)

# Function to calculate the total score along with ace adjustment
def total_count(hand):
    total = 0
    for suit,value in hand:
        if value in range(2,11):
            total += value
        elif value in ['J','Q','K']:
            total += 10
        else:
            if total <= 10:
                total += 11
            else:
                total += 1
    return total

play = True
dealer_chips,player_chips = 100,100 # Initially 100 chips are given to dealer and player

while play:

    deck = [] # Creating a deck of 52 cards with all possible combinations
    for suit in suits:
        for value in pack:
            deck.append((suit,value))

    print(f"You have {player_chips} chips.")

    # Asking the player for the bet
    while True:
        try:
            player_bet = int(input("How many chips would you like to bet : "))
        except:
            print("Please provide an integer!")
        else:
            if player_bet > player_chips or player_bet <= 0:
                if player_bet <= 0:
                    print("You should make a bet with positive number of chips!")
                else:
                    print(f"Sorry..You do not have enough chips! You have : {player_chips} chips.")
            else:
                break

    print(line)

    dealer_hand,dealer_total = [],0

    dealCard(dealer_hand,deck)
    dealCard(dealer_hand,deck)
    dealer_total = total_count(dealer_hand)

    hidden_card = dealer_hand[0] # Hidden card of the dealer

    print("Dealer hand : (Hidden Card)",end=" ")
    printcards(dealer_hand[1:])

    player_hand,player_total = [],0

    dealCard(player_hand,deck)
    dealCard(player_hand,deck)
    player_total = total_count(player_hand)


    print("Player Hand :",end=" ")
    printcards(player_hand)
    print(line)

    # Checking for blackjack
    if player_total == 21:
        print("It's a Blackjack!!...Player Won!")
        player_chips += (int(1.5*player_bet))
        dealer_chips -= (int(1.5*player_bet))
        further_game = False
    else:
        further_game = True

    # Game play
    while True and further_game:
        # Asking the player for hit or stay
        while True:
            hit_or_stay = input(("Enter 'h' for Hit and 's' for Stay : "))
            if hit_or_stay == 'h' or hit_or_stay == 's':
                break
            print("Please enter either 'h' or 's'!")
        print(line)
        if hit_or_stay == 'h':
            dealCard(player_hand,deck)
            player_total = total_count(player_hand)
            print("Dealer hand : (Hidden Card)",end=" ")
            printcards(dealer_hand[1:])
            print("Player Hand :",end=" ")
            printcards(player_hand)
            print(line)
            if player_total > 21:
                print("Dealer Hand :",end=" ")
                printcards(dealer_hand)
                print("Player Hand :",end=" ")
                printcards(player_hand)
                print("Player busts! and Dealer Won!")
                print(line)
                dealer_chips += player_bet
                player_chips -= player_bet
                break
        else:
            while dealer_total <= 16:
                dealCard(dealer_hand,deck)
                dealer_total = total_count(dealer_hand)

            if dealer_total > 21:
                print("Dealer Hand :",end=" ")
                printcards(dealer_hand)
                print("Player Hand :",end=" ")
                printcards(player_hand)
                print("Dealer busts! and Player Won!")
                print(line)
                player_chips += (2*player_bet)
                dealer_chips -= (2*player_bet)
                break
            else:
                if player_total == dealer_total:
                    print("Dealer Hand :",end=" ")
                    printcards(dealer_hand)
                    print("Player Hand :",end=" ")
                    printcards(player_hand)
                    print("It's a tie...")
                    print(line)
                    break
                elif player_total > dealer_total:
                    print("Dealer Hand :",end=" ")
                    printcards(dealer_hand)
                    print("Player Hand :",end=" ")
                    printcards(player_hand)
                    print("Player won!!")
                    print(line)
                    player_chips += (2*player_bet)
                    dealer_chips -= (2*player_bet)
                    break
                else:
                    print("Dealer Hand :",end=" ")
                    printcards(dealer_hand)
                    print("Player Hand :",end=" ")
                    printcards(player_hand)
                    print("Dealer won!!")
                    print(line)
                    dealer_chips += player_bet
                    player_chips -= player_bet
                    break

    print(f"You have {player_chips} chips now!")
    print(line)
    # Asking for one more round
    if player_chips <= 0:
        print(f"Sorry..No more bets are allowed. Since you have {player_chips} chips.")
        break
    new_game = input("Would you like to play an another round (y/n) : ")
    print(line)
    if new_game[0].lower() != 'y':
        print("Thanks for playing!")
        play = False