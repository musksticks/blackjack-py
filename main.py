from random import randint
from colorama import Fore

turn = 0
playerturn = 0
gameinitiated = 0
defaultamount = 1000
totalamount = defaultamount


def hit():
    number = randint(2, 10)
    return number

while True:

    turn += 1

    try:
        if gameinitiated == 0:
            if totalamount <= 0:
                ans = input(Fore.RED + "You are broke, Restart the game? (Y)es, (N)o: " + Fore.RESET)
                if ans.upper() == "Y":
                    totalamount = defaultamount
                if ans.upper() == "N":
                    break
                else:
                    continue

            print("Balance:", totalamount)
            amount = int(input("How much would you like to bet?: "))
            if amount > totalamount or amount < 0:
                print("Invalid amount")
                continue
            totalamount -= amount
            gameinitiated = 1
            p1total = 0
            p2total = 0
            turn = 0
            playerturn = 0

        if gameinitiated == 1:

            if p1total > 21:
                gameinitiated = 0
                playerturn = -1
                print("Bust in", turn, "turn(s)!")  # Removed money handling on loss
            if p2total > 21:
                gameinitiated = 0
                playerturn = -1
                print("Dealer bust!")
                amount *= 2
                totalamount += amount

            if playerturn == 0:
                roll = str(input(Fore.BLUE + "Would you like to (H)it or (S)tand: " + Fore.RESET))  # "Please draw a card: (Y)es , (N)o"
                if roll.upper() == "H":
                    p1total += hit()
                    print("Your total:", p1total)
                elif roll.upper() == "S":
                    playerturn += 1
                    continue

            elif playerturn == 1:
                if not p1total > 0:
                    playerturn = 0
                    print("Please hit atleast once")
                    continue
                if p2total <= 16:
                    print("Dealer: Hit")
                    playerturn -= 1
                    p2total += hit()
                    print("Dealer:", p2total)

            if p2total >= 17 and p2total < 22:
                print("Dealer: Stand")
                playerturn -= 1
                if p1total > p2total and p1total < 22:
                    print("You:", p1total, "Dealer:", p2total)
                    print("You win in", turn, "turns!")
                    amount *= 2
                    totalamount += amount
                    gameinitiated = 0
                elif p2total > p1total and p2total < 22:
                    print("You:", p1total, "Dealer:", p2total)
                    print("You lose in", turn, "turns!")  # Removed money handling on loss
                    gameinitiated = 0
                elif p1total == p2total:
                    print("You both draw in", turn, "turns!")
                    gameinitiated = 0
                    totalamount += amount

    except ValueError:
        print("Invalid Entry")
