#blackjack
import random
import time

cards = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
cardVal = [[11, 1], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]

'''
for x in range(10):
    print(cards[random.randint(0,len(cards)-1)])
'''

singleDeck = cards * 4
doubleDecks = singleDeck * 2

def drawHands(players, deck):
    totalPlayers = players + 1           #draw a hand for the dealer too

    pickedCards = []
    for totalCards in range(totalPlayers*2):
        card, deck = pickCard(deck)
        pickedCards.append(card)
    
    hands = []
    for player in range(totalPlayers):
        hand = pickedCards[player::totalPlayers]
        if player != totalPlayers-1:
            #all players are face up
            hands.append(hand)
        else:
            #except for the dealer
            hands.append([hand[0], "?"])
            dealerHand = hand

    return hands, deck, dealerHand

def pickCard(deck):
    #deck = total cards left to be drawn
    card = deck[random.randint(0,len(deck)-1)]
    deck.remove(card)

    return card, deck

def hit(hand, deck):
    card, deck = pickCard(deck)
    hand.append(card)
    handVal = calcValue(hand)
    print("Drew a(n) {}. New hand value is {}".format(card, handVal))

    if handVal > 21:
        time.sleep(1)
        print("Oof, Busted".format(hand))

    return hand, deck


def calcValue(hand):
    handVal = 0
    flagAce = hand.count("A")
    sortedHand = hand
    for aces in range(flagAce):
        sortedHand = sortHand(hand)

    for card in sortedHand:
        if card != "A":
            handVal += cardVal[cards.index(card)]
        elif handVal + 11 > 21 and handVal + 1 <= 21:
            handVal += 1
        elif handVal + 11 <= 21:
            #print("Two possible values {} or {}".format(handVal + 1, handVal + 11))
            handVal += 11
        else:
            handVal += 1

    return handVal

def sortHand(hand):
    if "A" in hand:
        hand.append(hand.pop(hand.index("A")))

    return hand

def dealerAction(dealerHand, deck):
    handVal = calcValue(dealerHand)
    print('The Dealer reveals their hand... {} with a value of {}'.format(dealerHand, handVal))
    time.sleep(1)
    if handVal == 21:
        print('Sorry, the Dealer got a blackjack.')

    while handVal < 17:
        print("The Dealer is going to 'hit'. ")
        dealerHand, deck = hit(dealerHand, deck)
        handVal = calcValue(dealerHand)
        time.sleep(1)

    return dealerHand, handVal

def results(hand, dealerHand):
    if calcValue(hand) > calcValue(dealerHand) and calcValue(hand) <= 21:
        print("You Win! Your hand {} beat the Dealer's hand {}".format(hand, dealerHand))
    elif calcValue(hand) <= 21 and calcValue(dealerHand) > 21:
        print('You Win! The Dealer busted: {}'.format(dealerHand))
    elif calcValue(hand) == calcValue(dealerHand):
        print('You drew with the Dealer.')
    else:
        print("You Lose... The Dealer's hand {} was better than yours {}".format(dealerHand, hand))

players = int(input("How many people would like to play? "))
if players <= 3:
    deck = singleDeck
else:
    deck = doubleDecks

hands, deck, dealerHand = drawHands(players, deck)

if players > 1:
    print("Here are the hands... {} and the Dealer has {}".format(hands[0:-1], hands[-1]))

for player in range(players):
    print("Player {} it is your turn...".format(player + 1))
    time.sleep(1)
    hand = hands[player]
    print("Your hand is {}, while the Dealer has {}".format(hands[player], hands[-1]))
    time.sleep(1)
    if calcValue(hand) == 21:
        print('Blackjack! Nice, you win!')
    else:
        hitOrStay = input("Would you like to hit? ('Yes' or 'No') ")
        while hitOrStay == "Yes":
            hand, deck = hit(hand, deck)
            if calcValue(hand) < 21:
                print('Your new hand is {}'.format(hand))
                hitOrStay = input("Would you like to hit? ('Yes' or 'No') ")
            elif calcValue(hand) == 21:
                print('You are sitting pretty at 21')
                hitOrStay = "No"
            else:
                print('Sorry, your turn is over')
                hitOrStay = "No"

dealerAction(dealerHand, deck)

for player in range(players):
    hand = hands[player]
    results(hand, dealerHand)

