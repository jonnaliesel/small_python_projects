import random

def numbersgame() :

    num = random.randint(1, 100)

    print('Guess a number between 1 and 100:')

    def evaulate() :
        guess = int(input())
        diff = num - guess


        if diff == 0 :
            print('Good job, you got it right!')
            
        elif diff > 0 :
            print('Sorry, the correct answer is bigger then ' + str(guess))
            evaulate()

        elif diff < 0 :
            print('Sorry, the correct answer is smaller then ' + str(guess))
            evaulate()

        else :
            print('Sorry, thats not a number. Try again')
            evaulate()

    evaulate()