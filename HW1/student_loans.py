# CS-171-A Prof Mark Boady
# Homework 1
# Cameron Kelliher
# 10/2/17

print('Welcome to the Student Loan Calculator')

principle = int(input('Enter the amount of the loan in dollars:\n'))
years = int(input('Enter the number of years the loan will be for:\n'))

def calcMonthlyPayment(p, y, interestRate):
    return (p * interestRate) / (12 * (1 - ((1 + (interestRate / 12)) ** (-y * 12))))

def calcBalance(y, monthly):
    return monthly * 12 * y

def calcInterest(p, bal):
    return bal - p

def calcFee(p, feeRate):
    return p * feeRate

def printLoan(name, p, y, interestRate, feeRate, unsubsidized):
    startingPrinciple = p

    if unsubsidized:
        p = p * (1 + interestRate * 4.25)

    monthlyPayment = calcMonthlyPayment(p, y, interestRate)
    balance = calcBalance(y, monthlyPayment)
    interest = calcInterest(p, balance) + (p - startingPrinciple)
    fee = calcFee(startingPrinciple, feeRate)

    print('\n%s Loan' % name)
    print('---------------------------')
    print('Principle: $%d' % startingPrinciple)
    print('Interest Rate: %s%%' % round(interestRate * 100, 1))
    print('Years: %d' % y)
    print('Monthly Payment: $%s' % round(monthlyPayment, 2))
    print('Total Paid on Loan: $%s' % round(balance, 2))
    print('Total Interest Paid: $%s' % round(interest, 2))
    print('Additional Fees Paid: $%s' % round(fee, 2))
    print('Total Costs Over Principle: $%s' % round(balance + fee - startingPrinciple, 2))

# Loans
printLoan('Subsidized Federal Direct', principle, years, .034, .01051, False)
printLoan('Unsubsidized Federal Direct', principle, years, .068, .01051, True)
printLoan('Federal PLUS', principle, years, .079, .04204, True)