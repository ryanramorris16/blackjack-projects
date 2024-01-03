#strategy bot
import time
from blackjack import calcValue
from blackjack import sortHand

def splitStrategy(hand, dealer):
    #should we split this hand?
    if len(set(hand)) == 1:
        #the cards in the hand are the same > you CAN split
        if hand[0] in [8, 'A']:
            return True
        elif hand[0] in [9]:
            if dealer[0] not in [7, 10, 'J', "Q", 'K', 'A']:
                return True
        elif hand[0] in [2, 3, 7]:
            if dealer[0] not in [8, 9, 10, 'J', "Q", 'K', 'A']:
                return True
        elif hand[0] in [6]:
            if dealer[0] not in [7, 8, 9, 10, 'J', "Q", 'K', 'A']:
                return True
        elif hand[0] in [4]:
            if dealer[0] not in [2, 3, 4, 7, 8, 9, 10, 'J', "Q", 'K', 'A']:
                return True
    
    return False

def standStrategy(hand, dealer):
    handVal = calcValue(hand)
    if "A" not in hand:
        if handVal >= 17:
            return True
        elif handVal in [13, 14, 15, 16] and dealer[0] in [2, 3, 4, 5, 6]:
            return True
        elif handVal == 12 and dealer[0] in [4, 5, 6]:
            return True
    elif "A" in hand and len(hand) == 2:
        hand.append(hand.pop(hand.index("A")))
        subVal = calcValue(hand[:-1])
        if subVal >= 9:
            return True
        elif subVal == 8 and dealer[0] != 6:
            return True
        elif subVal == 7 and dealer[0] in [7, 8]:
            return True
    else:
        hand.append(hand.pop(hand.index("A")))
        subVal = calcValue(hand[:-1])
        if subVal >= 8:
            return True
        elif subVal == 7 and dealer[0] not in [9, 10, 'J', "Q", 'K', 'A']:
            return True

    return False

def doubleStrategy(hand, dealer):
    if len(hand) != 2:
        return False
    handVal = calcValue(hand)
    if "A" not in hand:
        if handVal == 11:
            return True
        elif handVal == 10 and dealer[0] not in [10, 'J', "Q", 'K', 'A']:
            return True
        elif handVal == 9 and dealer[0] in [3, 4, 5, 6]:
            return True
    else:
        hand.append(hand.pop(hand.index("A")))
        subVal = calcValue(hand[:-1])
        if subVal == 8 and dealer[0] == 6:
            return True
        elif subVal == 7 and dealer[0] in [2, 3, 4, 5, 6]:
            return True
        elif subVal == 6 and dealer[0] in [3, 4, 5, 6]:
            return True
        elif subVal in [4, 5] and dealer[0] in [4, 5, 6]:
            return True
        elif subVal in [2, 3] and dealer[0] in [5, 6]:
            return True

    return False

def hitStrategy(hand, dealer):
    handVal = calcValue(hand)
    if "A" not in hand:
        return True
    else:
        if handVal == 18 and dealer[0] in [9, 10, 'J', "Q", 'K', 'A']:
            return True
        elif handVal < 18:
            return True

    return False    

def main():
    cards = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]

    hand = []
    while len(hand) < 2 or not set(hand).issubset(cards):
        hand = input("What is your hand? (Separated by ', ' please)").split(', ')
        for ind, card in enumerate(hand):
            try:
                hand[ind] = int(card)
            except:
                continue
        if len(hand) < 2 or not set(hand).issubset(cards):
            print(set(hand).issubset(cards))
            print('Sorry, try inputting your hand again...')
        time.sleep(1)

    dealer = []
    while len(dealer) != 1 or not set(dealer).issubset(cards):
        dealerCard = input("What is the Dealer's upcard? ")
        try: 
            dealerCard = int(dealerCard)
        except:
            pass
        dealer.append(dealerCard)
        if len(dealer) != 1 or not set(dealer).issubset(cards):
            print("Sorry, try inputting the Dealer's card again...")
            dealer = []
        time.sleep(1)


    if splitStrategy(hand, dealer):
        print("You should split your hand.")
    elif standStrategy(hand, dealer):
        print("You should stand.")
    elif doubleStrategy(hand, dealer):
        print("You should double.")
    elif hitStrategy(hand, dealer):
        print("You should hit.")


if __name__ == '__main__':
    main()
