import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value ={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2    
}

def your_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
        
    return winnings, winning_lines
            
                

def spin_the_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = [[], [], []]
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns
            

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in columns:
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
                
def deposit():
    while True:
        amt = input("How much would you like to deposit? $")
        if amt.isdigit():
            amt = int(amt)
            if amt > 0:
                break
            else:
                print("Amount must be a positive, non-zero number.")
        else:
            print("Error. Please enter a number.")
            
    return amt

def get_bet():
    while True:
        amt = input("How much would you like to bet? $")
        if amt.isdigit():
            amt = int(amt)
            if MIN_BET <= amt <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Error. Please enter a number.")
            
    return amt    
def get_number_of_lines():
    while True:
        lines = input("How many lines are you betting on? (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Error. Please enter a number.")
            
    return lines        

def slots(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    print(balance, lines)
    
    
    slots = spin_the_machine(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
    winnings, winning_lines = your_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet    
    
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        result = input('Press enter to spin (q to quit)')
        if result == "q":
            break
    balance += slots(balance)   
  
  
main()