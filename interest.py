# coding=utf-8

# print: investerat belopp
print('Hur mycket vill du investera?')
investment = float(input())
print(investment)

# input för att ta aarsavkastning som  input från user
print('Hur många procent är årsavkastning?')
annualReturn = float(input())/100
print(annualReturn)

# print: antal år
print('Hur många år vill du spara?')
years = int(input())
print(years)

# investerat belopp x (1+årsavksatning)^antal år
finalReturn = investment * (1 + annualReturn) ** years
print('Din besparing kommer efter ' + str(years) + ' år vara ' + str(finalReturn) + 'kr')
