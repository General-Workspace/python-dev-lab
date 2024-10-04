menus = {"breakfast": ["eggs", "bacon", "toast", "coffee", "bagel"],
                 "lunch": ["soup", "salad", "sandwich", "soda", "water"],
                 "dinner": ["steak", "potatoes", "vegetables", "wine", "beer"]}

for (key, value) in menus.items():
    print(f"For {key}, you can have: {value}", end='\n')