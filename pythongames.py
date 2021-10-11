#Game central

#Games
from numbergame import numbersgame
from interest import countYourSavings

print('Welcome to Python Game Central!')
first_game = True
invalid_answer = False
highscores = {1: {}}

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
            user_name = str(list(highscore.keys())[0])
            score = int(list(highscore.values())[0])
            highscores[1][user_name] = score
            print(highscores[1])
        
    elif game == 2 :
        countYourSavings()
    else :
        first_game = True
        invalid_answer = True
        game = input('Sorry, not a valid game number, try again: ')
