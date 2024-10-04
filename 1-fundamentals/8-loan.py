money_owed = float(input("How much money do you owe in dollars?\n"))
interest_rate = float(input("What is the annual interest rate (in percent)?\n"))
monthly_payment = float(input("What is your monthly payment in dollars?\n"))
months = int(input("How many months do you want to calculate?\n"))

monthly_interest_rate = interest_rate / 12 / 100

for i in range(months):
    interest_paid = money_owed * monthly_interest_rate
    money_owed += interest_paid

    if money_owed < monthly_payment:
        monthly_payment = money_owed
    money_owed -= monthly_payment
    print("Month ", i + 1, ": $", money_owed, " remaining", sep='')

    print("Interest paid: $", interest_paid, sep='')