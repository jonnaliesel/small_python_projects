import random

def numbersgame() :

    num = random.randint(1, 100)
    print(num)

    guess = int(input('\nGuess a number between 1 and 100: ' ))
    diff = num - guess

    while guess :
        if diff == 0 :
            print('Good job, you got it right!')
            break
            
        elif diff > 0 :
            print('Sorry, the correct answer is bigger then ' + str(guess))

        elif diff < 0 :
            print('Sorry, the correct answer is smaller then ' + str(guess))

        else :
            print('Sorry, thats not a number. Try again')