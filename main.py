from random import randint
from colorama import Fore

# VARIABLES
turn = 0
stand = False
gameInitiated = 0
DEFAULT_MONEY = 1000
totalAmount = DEFAULT_MONEY

def hit():
    return randint(2, 10)

while True:
    turn += 1

    try:
        if gameInitiated == 0:
            # OUT OF MONEY HANDLING
            if totalAmount <= 0:
                ans = input(Fore.RED + "You are broke, Restart the game? (Y)es, (N)o: " + Fore.RESET)
                if ans.upper() == "Y":
                    totalAmount = DEFAULT_MONEY
                if ans.upper() == "N":
                    break
                else:
                    continue

            # START OF BET / GAME
            print("Balance:", totalAmount)
            amount = int(input(Fore.GREEN + "How much would you like to bet?: " + Fore.RESET))
            if amount > totalAmount or amount < 0:
                print("Invalid amount")
                continue
            totalAmount -= amount
            gameInitiated = 1
            playerturn = 0
            p1total = 0
            p2total = 0
            turn = 0

        # BUST HANDLING
        if gameInitiated == 1:
            if p1total > 21:
                gameInitiated = 0
                playerturn = -1
                print("Bust in", turn, "turn(s)!")  # Removed money handling on loss
            if p2total > 21:
                gameInitiated = 0
                playerturn = -1
                print("Dealer bust!")
                amount *= 2
                totalAmount += amount

            # ASK PLAYER (H)IT OR (S)TAND
            if playerturn == 0 and not stand:
                roll = str(input(Fore.BLUE + "Would you like to (H)it or (S)tand: " + Fore.RESET))  # "Please draw a card: (Y)es , (N)o"
                if roll.upper() == "H":
                    p1total += hit()
                    print("Your total:", p1total)
                elif roll.upper() == "S":
                    playerturn = 1
                    stand = True
                    continue
            
            # CHECK FOR HIT / STAND & START OF DEALER AI
            elif playerturn == 1 or stand:
                if not p1total > 0:
                    playerturn = 0
                    stand = False
                    print("Please hit atleast once")
                    continue
                if p2total <= 16:
                    playerturn = 0
                    p2total += hit()
                    print("Dealer hit:", p2total)

            # DEALER / PLAYER WIN HANDLING
            if p2total >= 17 and p2total < 22:
                print("Dealer stand:", p2total)
                playerturn = 0
                if p1total > p2total and p1total < 22:
                    print("You:", p1total, "Dealer:", p2total)
                    print("You win in", turn, "turns!")
                    amount *= 2
                    totalAmount += amount
                    gameInitiated = 0
                elif p2total > p1total and p2total < 22:
                    print("You:", p1total, "Dealer:", p2total)
                    print("You lose in", turn, "turns!")  # Removed money handling on loss
                    gameInitiated = 0
                elif p1total == p2total:
                    print("You:", p1total, "Dealer:", p2total)
                    print("You both draw in", turn, "turns!")
                    gameInitiated = 0
                    totalAmount += amount

    except ValueError:
        print("Invalid Entry")
