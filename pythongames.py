#Game central

#Games
from numbergame import numbersgame
from interest import countYourSavings

print('Welcome to Python Game Central!')
print('What game do you want to play?\n1. Numbersgame 2. Count your savings')

game = input('Please insert gamenumber ')

if game == 1 :
    numbersgame()
elif game == 2 :
    countYourSavings()
else :
    game = input('Sorry, not a valid game number, try again ')