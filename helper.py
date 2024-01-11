import tkinter as tk
from functools import partial
from tkinter import Radiobutton
import strategy

def close_window():
    window.destroy()

def add_to_hand(text):
    if selection.get() == 1:
        hand.append(text)
        hand_label["text"] = "Player hand: " + ", ".join(hand)
    elif selection.get() == 2:
        dealer[0] = text
        dealer_label["text"] = "Dealer hand: " + ", ".join(dealer)

def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x

window = tk.Tk()
window.title("Blackjack helper")

# Gap size (adjust as needed)
suits = {"Hearts": ("♥", "red"), 
         "Diamonds": ("♦", "red"), 
         "Clubs": ("♣", "black"), 
         "Spades": ("♠", "black")
        }
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
gap_size = 10 

# Add player or dealer selector
selector_label = tk.Label(window, text="Which would you like to modify? ")
selector_label.pack(pady=gap_size)
selection = tk.IntVar()
player_sel = Radiobutton(window, text="Player", variable=selection, value=1)
player_sel.pack()
dealer_sel = Radiobutton(window, text="Dealer", variable=selection, value=2)
dealer_sel.pack()

# Create the hand label
hand = []
hand_label = tk.Label(window, text="Player hand:")
hand_label.pack(pady=gap_size)

# Create the dealer label
dealer = [0]
dealer_label = tk.Label(window, text="Dealer card:")
dealer_label.pack(pady=gap_size)

# Create the grid of buttons
grid_frame = tk.Frame(window)  # Use a Frame to center the grid
button_grid = []  # Store button references
for row, suit in enumerate(suits):
    row_buttons = []
    for col, number in enumerate(numbers):
        symbol, color = suits[suit]
        button_text = number + symbol
        button = tk.Button(
            grid_frame, 
            text=button_text, 
            fg=color,
            command=partial(add_to_hand,button_text)
        )
        button.grid(row=row, column=col)
        row_buttons.append(button)
    button_grid.append(row_buttons)

grid_frame.pack(expand=True, fill="both", padx=gap_size, pady=gap_size)

# Create and position the "Go" button at the bottom
go_button = tk.Button(window, text="Go", command=close_window, font=("Times New Roman", 10))
go_button.pack(pady=gap_size)  # Add padding for the gap

window.mainloop()

hand = [try_int(x[:-1]) for x in hand]
dealer = try_int(dealer[0][:-1])

if strategy.splitStrategy(hand, dealer):
    print("You should split your hand.")
elif strategy.standStrategy(hand, dealer):
    print("You should stand.")
elif strategy.doubleStrategy(hand, dealer):
    print("You should double.")
elif strategy.hitStrategy(hand, dealer):
    print("You should hit.")