#Game central

#Games
from numbergame import numbersgame
from interest import countYourSavings
from highscore import save_highscore

print('Welcome to Python Game Central!')
first_game = True
invalid_answer = False

while True :
    if not first_game :
        another_game = input('\nGood job! Wanna play another game? y/n ')

        if another_game != 'y' :
            print('Thanks, bye!')
            quit()

    if not invalid_answer :
        print('\nWhat game do you want to play?\n1. Numbersgame 2. Count your savings')
        game = int(input('Please insert game number: '))

    first_game = False

    if game == 1 :
        highscore = numbersgame()

        if highscore:
            save_highscore(game, highscore)
        
    elif game == 2 :
        countYourSavings()
    else :
        first_game = True
        invalid_answer = True
        game = input('Sorry, not a valid game number, try again: ')
