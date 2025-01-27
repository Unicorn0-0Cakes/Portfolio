"""

0_0

Project Name   : Text-Based Slot Machine
Description    : Python-based game simulating a virtual slot machine
                 with betting and balance management mechanics.
Version        : 0.0.1
Created By     : @Unicorn0-0Cakes
Date Created   : 2025.01.23

Notes:
- This project was inspired by a tutorial by @TechWithTim.
- For educational and portfolio purposes.
- There are a ton of comments for a well documented project source

"""

#---
#plan to add global variables to change themes using a random number generator
#gv
#---

#import modules
import random

#---

#global constants

global balance

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "🐸": 2,  # Less frequent, rare symbol
    "🌮": 3,
    "🎩": 4,
    "🦄": 5,
    "🐙": 6,
    "🍕": 7,
    "🪩": 8,  # More frequent, common symbol
    "🍩": 6,
    "👽": 3,
    "🌈": 5
}

symbol_values = {
    "🐸": 50,  # Very rare symbol
    "🌮": 30,  # Rare symbol
    "🎩": 25,  # Uncommon symbol
    "🦄": 40,  # Rare symbol
    "🐙": 15,  # Slightly uncommon symbol
    "🍕": 10,  # More frequent symbol
    "🪩": 5,   # Very common symbol
    "🍩": 8,   # Common symbol
    "👽": 20,  # Uncommon symbol
    "🌈": 35   # Rare symbol
}


#---

#generates what symbols are in each column
def get_slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)

  columns = []
  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      column.append(value)

    columns.append(column)

  return columns

#---

#transpose the matrix
def print_slot_machine(columns):
  for row in range(len(columns[0])):
      for i, column in enumerate(columns):
        if i != len(columns) - 1:
          print(column[row], end=" | ")
        else:
          print(column[row], end="")

      print()

#---


#define deposit/input

def deposit():
    # Initiates a loop to repeatedly prompt the user for a valid deposit amount.

    while True:
        # Prompts the user to input an amount, displaying a fun and quirky message.

        amount = input("Time to fatten your balance. How much? 🐷   $")  # gv: Customized prompt for user input.

        print()  # Adds an empty line

        # Checks if the input consists only of digits (i.e., a valid number).
        if amount.isdigit():

            # Converts the valid string input to an integer.
            amount = int(amount)

            # Checks if the entered number is greater than 0.
            if amount > 0:
                # Breaks the loop if the input is valid.
                break

            else:
                # Displays an error message if the number is less than or equal to 0.
                print("Oops! You can’t deposit the air in your wallet. 🍃")  # gv: Humorous error for zero or negative values.
                
                print()  # Adds an empty line
        
        else:
            # Displays an error message if the input is not numeric.
            print("Are you trying to code in hieroglyphs? Digits, please. 🛸")  
            # gv: Lighthearted message for non-numeric input.
            
            print()  # Adds an empty line

    # Returns the valid deposit amount to the caller.
    return amount

#---


#define number of lines
def get_number_of_lines():
    
    # Initiates a loop to repeatedly prompt the user for betting lines.
    while True:
        
        # Prompts the user to input an amount, displaying a fun and quirky message.
        lines = input("Spin smarter, not harder. How many lines will it be 🧠 (1-" +str(MAX_LINES) + ")? ")         
        
        print()  # Adds an empty line
        
        if lines.isdigit():
            # Converts the valid string input to an integer.
            lines = int(lines)
            
            # Checks if the entered number is greater than 0.
            if 1 <= lines <= MAX_LINES:
                # Breaks the loop if the input is valid.
                break
            
            else:
                # Displays an error message if the number is less than or equal to 0.
                print("No funny business! We need a valid line count to play. 🎰")  # gv: Humorous error for zero or negative values.
                
                print()  # Adds an empty line
        else:
            # Displays an error message if the input is not numeric.
            print("Are you trying to code in hieroglyphs? Digits, please. 🛸")  # gv: Lighthearted message for non-numeric input.
            
            print()  # Adds an empty line

    # Returns the chosen number of lines 
    return lines

#---

#define the bet input function
def get_bet():

    while True:
        # Prompts the user to input an amount, displaying a fun and quirky message.

        amount = input("Drop the digits—how much are you gambling this time? (per line bet) $")  # gv: Customized prompt for user input.

        print()  # Adds an empty line

        # Checks if the input consists only of digits (i.e., a valid number).
        if amount.isdigit():

            # Converts the valid string input to an integer.
            amount = int(amount)

            # Checks if the entered number is greater than 0.
            if MIN_BET <= amount <= MAX_BET:
                # Breaks the loop if the input is valid.
                break

            else:
                # Displays an error message if the number not within the allowable betting range.
                print(f"Whoa, ambitious much? Stick to ${MIN_BET} - ${MAX_BET}, my friend.")  # gv: Humorous error for zero or negative values.
                
                print()  # Adds an empty line
        
        else:
            # Displays an error message if the input is not numeric.
            print("Are you trying to code in hieroglyphs? Digits, please. 🛸")  
            # gv: Lighthearted message for non-numeric input.
            
            print()  # Adds an empty line

    # Returns the valid bet amount to the caller.
    return amount

#---

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    # Define the line indices for 1, 2, or 3 lines
    line_map = {
        1: [1],          # Middle line (index 1)
        2: [0, 2],       # Top and bottom lines (indices 0 and 2)
        3: [0, 1, 2]     # All lines
    }

    # Get the lines to check based on the user's choice
    lines_to_check = line_map[lines]

    for line in lines_to_check:
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)  # Add 1 to convert 0-based to 1-based indexing

    return winnings, winning_lines


#---
def spin(balance):
    # Define the number of lines
    lines = get_number_of_lines()

    # Check to make sure the balance is high enough to cover the bets
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Trying to bet like royalty, but your treasury holds only ${balance}!")
            print()  # Adds an empty line
        else:
            break

    # Computation for all lines bet
    total_bet = bet * lines
    print(f"Math time: ${bet} times {lines} equals a total wager of ${total_bet}. Feeling lucky?")
    print()  # Adds an empty line

    # Spin prompt
    print("Spinning...")
    print()  # Adds an empty line

    # Generate the slot machine spin
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    print()  # Adds an empty line

    # Calculate winnings
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)

    if winnings > 0:
        print(f"Cha-ching! 💸 You just pocketed ${winnings}.")
        print()  # Adds an empty line
        print(f"Payday on lines ", *winning_lines, " 🚀")
        print()  # Adds an empty line
    else:
        print("The slot wheels are teasing—better luck next spin! 🎭")
        print()  # Adds an empty line

    # Return the net result of the spin (winnings minus the total bet)
    return winnings - total_bet



#---
#Main Function
#---

#main function
def main():


#welcome message

    print("🎈 Ready to take a spin on the wild side? The slot machine awaits your courage! 🌀")

    print()  # Adds an empty line
    print()  # Adds an empty line

    # Calls the deposit function to get the initial balance from the user.
    # The user's deposit is stored in the 'balance' variable.
    balance = deposit()

    while True:
        print(f"Your stash: ${balance}. Time to make it rain? 🌧️💸")
        print()  # Adds an empty line

        ready_to_spin = input("🎰 Are you ready to spin the slot wheels? (Press Enter to play or 'q' to quit)").strip().lower()
        print()  # Adds an empty line

    # Handle the user's response
        if ready_to_spin == "q":
          print("No problem! Come back when you're ready. 😊")
          print()  # Adds an empty line
          print(f"Your final haul: ${balance}. What an adventure! 🌟")
          return  # Exit the program if the user doesn't want to spin

        print("Spinning the wheels... Good luck! 🍀🎉")
        print()  # Adds an empty line
        balance += spin(balance)


#---     

# Calls the main function to start the program.
main()
