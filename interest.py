def countYourSavings() :
    investment = float(input('\nHow much do you want to invest? '))
    annualReturn = float(input('How many percent is the anual return? ' ))/100
    years = int(input('How many years will you save? '))

    finalReturn = investment * (1 + annualReturn) ** years
    print('Your savings after ' + str(years) + ' years will be ' + str(int(finalReturn)) + ' SEK')
