weather = input("What's the weather today?\n")
temp = input("What is the temperature?\n")
if weather == "sunny" or temp >= 90:
    print("It's too hot")
    print("Stay inside")
elif weather == 'raining' or temp < 80:
    print("It'swet and cold")
    print("Stay inside")
else:
    print("It's safe to go hiking!")
