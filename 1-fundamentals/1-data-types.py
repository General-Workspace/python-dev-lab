# amount = 10
# tax = 0.06
# total = amount + amount*tax
# print(int(total))

# store_name = 'Sarah\'s store'
# print(store_name)

name = input('What\'s your name?\n')
greeting = 'Hey there, ' + name
print(greeting)

age = int(input('How old are you?\n'))
decades = age // 10
remainder = str(age % 10)
message = 'You are ' + str(decades) + ' decades and ' + remainder + ' years old.'
print(message)