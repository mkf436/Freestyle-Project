#seting up a card dictionary so that each card has a value associated with it
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
computer = random.choice(cards.keys())  #defining a variable so that the computer picks a random card from the deck to play
you = random.choice(cards.keys()) #defining a variable so that "you" pick a random card to play against the computer

print("------------------------")
print("Computer: " + computer)  #tells you what card the computer picked
print("You: " + you)  #tells you what card you picked
print("------------------------")


if (computer > you): #evaluates if the computer won
    print("Sorry, Computer Wins")
elif (computer == you): #evaluates if there is a tie
    print("Tie Game!")
else: #if the computer did not win and there is no tie, then you won
    print("You Win!")

print("------------------------")

computer_game_wins = 0 #setting up a count variable to count how many games the computer has won
your_game_wins = 0  #setting up a count variable to count how many games you won
ties = 0  #setting up a count variable to count how many ties there have been

for i in cards:
    if computer > you: #if the computer wins a game, add one game to the count
        computer_game_wins = computer_game_wins + 1
    if you > computer: #if you win a game, add one game to the count
        your_game_wins = your_game_wins + 1
    if computer == you:  #if there is a tie, add one game to the count
        ties = ties + 1
    #if computer_game_wins + your_game_wins + ties == 26:  #counts the total number of games played, once you play 26 games, the game is over
     #   print("Game Over")


#output: 
print("Number of Computer Wins:" + str(computer_game_wins)) #tells you how many games the computer has won
print("Number of Your Wins:" + str(your_game_wins))  #ells you how many games you have won
print("Number of Ties:" + str(ties))  #tells you how many ties there have been
print("------------------------")
print("Total Games Played:" + str(computer_game_wins + your_game_wins + ties))  #tells you how many games have been played so far
print("------------------------")