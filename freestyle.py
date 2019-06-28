cards = {
    "2C":2,
    "2D":2,
    "2H":2,
    "2S":2,
    "3C":3,
    "3D":3,
    "3H":3,
    "3S":3,
    "4C":4,
    "4D":4,
    "4H":4,
    "4S":4,
    "5C":5,
    "5D":5,
    "5H":5,
    "5S":5,
    "6C":6,
    "6D":6,
    "6H":6,
    "6S":6,
    "7C":7,
    "7D":7,
    "7H":7,
    "7S":7,
    "8C":8,
    "8D":8,
    "8H":8,
    "8S":8,
    "9C":9,
    "9D":9,
    "9H":9,
    "9S":9,
    "10C":10,
    "10D":10,
    "10H":10,
    "10S":10,
    "JC":11,
    "JD":11,
    "JH":11,
    "JS":11,
    "QC":12,
    "QD":12,
    "QH":12,
    "QS":12,
    "KC":13,
    "KD":13,
    "KH":13,
    "KS":13,
    "AC":14,
    "AD":14,
    "AH":14,
    "AS":14,
}


import random
computer = random.choice(cards.keys())
you = random.choice(cards.keys())



print("Computer: " + computer)
print("You: " + you)

computer_game_wins = 0
your_game_wins = 0
ties = 0





if (computer > you):
    print("Sorry, Computer Wins")
elif (computer == you):
    print("Tie Game!")
else:
    print("You Win!")



for i in cards:
    if computer > you:
        computer_game_wins = computer_game_wins + 5
    if you > computer:
        your_game_wins = your_game_wins + 6
    if computer == you:
        ties = ties + 7

print("Number of Computer Wins:" + str(computer_game_wins))
print("Number of Your Wins:" + str(your_game_wins))
print("Number of Ties:" + str(ties))
print("Total Games Played:" + str(computer_game_wins + your_game_wins + ties))
