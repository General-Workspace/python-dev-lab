total = 0
expenses = []
num_expenses = int(input("Enter the number of expenses: "))

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense: ")))
    total += expenses[i]
print("You spent $", total, " on lunch this week.", sep='')