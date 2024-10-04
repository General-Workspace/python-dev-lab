expenses = [10.50, 8, 5, 15, 20, 5, 3]
total = sum(expenses)
print(total)

sum_total = 0
for expense in expenses:
    sum_total += expense

print("You spent $", sum_total, " on lunch this week.", sep='')