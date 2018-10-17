# retirementCalculator
Prompt user for variables to output money left at retirement

from datetime import datetime
currentYear = datetime.now().year

print('\nRetirement Calulator:')
startingValue = float(input('\nHow much money do you currently have invested? '))
monthlyAddition = float(input('\nHow much money do you plan on contributing per month? '))
interestRate = float(input('\nWhat is your expected rate of return? ')) / 100
yearsLeft = int(input('\nWhat year do you plan on retiring? ')) - currentYear
total = startingValue * (1 + interestRate / 12) ** (12 * yearsLeft)
numerator = (total / startingValue - 1) * monthlyAddition
denominator = interestRate / 12

grandTotal = total + numerator / denominator

print('\nTotal = $%0.2f\n' %grandTotal)
#print()
#print(interestRate)
#print(yearsLeft)
#print(total)
#print(numerator)
#print(denominator)
