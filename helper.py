import tkinter as tk
from functools import partial
from tkinter import Radiobutton
import strategy

def close_window():
    window.destroy()

def close_new_window():
    new_window.destroy()  # Close without resetting

def add_to_hand(text):
    if selection.get() == 1:
        hand.append(text)
        hand_label["text"] = "Player hand: " + ", ".join(hand)
    elif selection.get() == 2:
        dealer[0] = text
        dealer_label["text"] = "Dealer card: " + ", ".join(dealer)

def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x
    
def open_new_window():
    global new_window

    # Check if new_window already exists
    try:
        # If it exists, bring it to the front instead of creating a new one
        new_window.lift()
    except:
        # If it doesn't exist, create a new one
        new_window = tk.Toplevel(window)
        new_window.title("New Window")

        # Clean hand and dealer to remove symbols
        clean_hand = [try_int(card[:-1]) for card in hand]
        clean_dealer = [try_int(dealer[0][:-1])]

        output = ""
        if strategy.splitStrategy(clean_hand, clean_dealer):
            output = "You should split your hand."
        elif strategy.standStrategy(clean_hand, clean_dealer):
            output = "You should stand."
        elif strategy.doubleStrategy(clean_hand, clean_dealer):
            output = "You should double."
        elif strategy.hitStrategy(clean_hand, clean_dealer):
            output = "You should hit."

        hello_label = tk.Label(new_window, text=output)
        hello_label.pack()   

        # Create a frame for the buttons in the new window
        button_frame = tk.Frame(new_window)
        button_frame.pack()

        # Create "Keep Hand" button
        keep_button = tk.Button(
            button_frame,
            text="Keep Hand",
            command=close_new_window
        )
        keep_button.pack(side="left", padx=gap_size)

        # Create reset button
        reset_button = tk.Button(
            button_frame, 
            text="Reset", 
            command=reset_window
        )
        reset_button.pack(side="left", padx=gap_size) 

def reset_window():
    # Clear hand and dealer
    global hand, dealer
    hand = []
    dealer = [0]

    # Update labels
    hand_label["text"] = "Player hand:"
    dealer_label["text"] = "Dealer card:"

    # Close the current new window
    new_window.destroy()

window = tk.Tk()
window.title("Blackjack helper")

# Gap size (adjust as needed)
suits = {"Hearts": ("♥", "red"), 
         "Diamonds": ("♦", "blue"), 
         "Clubs": ("♣", "green"), 
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
            command=partial(add_to_hand,button_text),
            activeforeground="white", 
            activebackground=color
        )
        button.grid(row=row, column=col)
        row_buttons.append(button)
    button_grid.append(row_buttons)

grid_frame.pack(expand=True, fill="both", padx=gap_size, pady=gap_size)

# Container frame for Submit and Clear buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=gap_size)  # Add padding above the buttons

# Create and position the "Go" button at the bottom
go_button = tk.Button(button_frame, 
                      text="Submit", 
                      command=open_new_window, 
                      font=("Times New Roman", 10))
go_button.pack(side="left", padx=gap_size)  # Add padding for the gap

# Create and position the "Clear" button next to "Submit"
clear_button = tk.Button(button_frame, 
                         text="Clear", 
                         command=reset_window, 
                         font=("Times New Roman", 10))
clear_button.pack(side="left", padx=gap_size)

window.mainloop()
'''
hand = [try_int(x[:-1]) for x in hand]
dealer = [try_int(dealer[0][:-1])]

if strategy.splitStrategy(hand, dealer):
    print("You should split your hand.")
elif strategy.standStrategy(hand, dealer):
    print("You should stand.")
elif strategy.doubleStrategy(hand, dealer):
    print("You should double.")
elif strategy.hitStrategy(hand, dealer):
    print("You should hit.")
'''