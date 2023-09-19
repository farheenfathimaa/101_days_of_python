import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program")
list = {}
bidder = 'yes'

def finding_highest(list):
    highest_bid = 0
    winner = ''
    for name, bid_amount in list.items():  # Iterate over the dictionary items
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = name
    print(f"the winner is {winner} with a bid of ${highest_bid}")

while bidder == 'yes':
    name = input("What is your name?: ")
    bid = int(input("what's your bid? $"))
    list[name] = bid
    bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if bidder == 'yes':
        os.system('cls')
    elif bidder == 'no':
        os.system('cls')
        finding_highest(list)
