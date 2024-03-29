# Blackjack Projects

Blackjack Projects is a collection of short coding exercises to play and manipulate the card game Black Jack

## Blackjack.py

Base python script which runs the game of Black Jack.
Includes functions:

- drawHands - takes a number of players and a deck to generate hands for each player + the dealer
- pickCard - picks specific card from the deck based on random number
- playBlackjack - most of the functionality of the script, takes in a hand, the deck, a bet, and whether or not the hand has been split already in a boolean
- hit - adds one card to a specific hand
- calcValue - calculates the numerical value of the hand (assuming the highest allowed value for aces)
- sortHand - used in calcValue to put aces at the end of the hand for easier handling of the hand value
- dealerAction - determines whether the dealer hits or stays
- results - calculates whether a player won or lost their hand and how much their return was based on initial bet
- splitter - generates 2 split hands if a player gets 2 of the same card and wants to double their bet
- checkBlackjack - returns 1 if the value of a hand is 21, 0 else
- createDeck - creates a deck of cards with more decks depending on the amount of players

## Strategy.py

Python script to determine the optimal strategy for a given hand & dealer card
Includes functions:

- splitStrategy - determines if you can and should split your hand
- standStrategy - determines if you should stand
- doubleStrategy - deteremins if you can and should double
- hitStrategy - determines if you should hit

**These functions currently need to be ran in order to output the correct outcome**

## Helper.py

Python script to open a GUI for inputs on player's hand and dealer's upcard.

## To-Do

- Add "New Hand" button to helper and don't auto close it
- Change "Go" to "Submit" and output the strategy result in helper
- Add all hands on table option to helper for card counting?
- Add card counting to strategy or probabilistic model for card counting?