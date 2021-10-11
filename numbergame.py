from random import randint

def numbersgame() :

    num = randint(1, 10)
    print(f'\nCheet: {num}')
    tries = 0
    guess = int(input('\nGuess a number between 1 and 10: \nYou have 10 tries to get it right ;) '))
    highscores = {}

    while guess :
        diff = num - guess
            
        if diff > 0 and tries < 9:
            tries += 1
            guess = int(input(f'\nSorry, the correct answer is bigger then {guess}\nNumber of tries: {tries}\n\nGuess again '))

        elif diff < 0 and tries < 9:
            tries += 1
            guess = int(input(f'\nSorry, the correct answer is smaller then {guess}\nNumber of tries: {tries}\n\nGuess again '))

        elif tries > 8:
            print('\n***************GAME OVER***************\nOh no, you ran out of tries!')
            break

        else:
            tries += 1
            if(tries > 1):
                print(f'\nGood job, you got it right in just {tries} tries!')

            else:    
                print(f'\nGood job, you got it right in just {tries} try!')
                
            
            if not tries in highscores.values():
                    save_highscore = input(f'Thats a new highscore, wanna save your score? y/n ')
                    if save_highscore.lower() == 'y':
                        user_name = input('Please enter your name: ')
                        highscores[user_name] = tries
                        print(highscores)
            break

# TODO: 
# Highscore
# Close guessing