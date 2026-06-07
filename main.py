import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8 
}
symbol_values = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2 
}

def check_winnings(columns, lines, bet, values):
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


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        coloum =[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            coloum.append(value)
        columns.append(coloum)
    return columns

def print_slot_matchine(colomns):
    for row in range(len(colomns[0])):
        for i, col in enumerate(colomns):
            if i != len(colomns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposite? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Ammount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a valid number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough balance to bet that amount,\n""your current balance is ${balance}")
        else:
            break
    print(f"you are betting ${bet} on lines {lines} Total bet is equals to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_matchine(slots)
    winnings, winning_lines = check_winnings(slots, lines,bet,symbol_values)
    print(f"You won ${winnings}.")
    print(f"you won on lines:", *winning_lines)
    winnings = winnings - total_bet
    return winnings


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin_input = input("Press enter to play (q to quit).")
        if spin_input == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

main()