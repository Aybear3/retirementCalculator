# import datetime to determine how many years a person has until they want to retire
from datetime import datetime
currentYear = datetime.now().year

# title
print('\nRetirement Calculator:')

# total amount of money invested towards retirement
startingValue = float(input('\nHow much money do you currently have invested? '))

# how much money is going towards retirement accounts per month
monthlyAddition = float(input('\nHow much money do you plan on contributing per month? '))

# expected rate of return (interest) 7 is a conservative vale
interestRate = float(input('\nWhat is your expected rate of return? ')) / 100

#determines number of years until year they give using datetime
yearsLeft = int(input('\nWhat year do you plan on retiring? ')) - currentYear

# Ok so there are three parts of this equation. 
# It looks like $$$ = A + (B / C)
# interest is A, numerator is B and denominator is C
interest = startingValue * (1 + interestRate / 12) ** (12 * yearsLeft)
numerator = (interest / startingValue - 1) * monthlyAddition
denominator = interestRate / 12

grandTotal = interest + numerator / denominator

print('\nTotal = $%0.2f\n' %grandTotal)

# print variables to check myself
#print()
#print(interestRate)
#print(yearsLeft)
#print(interest)
#print(numerator)
#print(denominator)