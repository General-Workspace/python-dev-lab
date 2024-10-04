acronyms_and_transalations = {"lol": "laugh out loud", 
                              "brb": "be right back", 
                              "g2g": "got to go", 
                              "smh": "shaking my head", 
                              "idk": "I don't know",
                              "tbh": "to be honest", 
                              "lmao": "laughing"}

for (acronym, translation) in acronyms_and_transalations.items():
    print(f"{acronym.upper()} means {translation.capitalize()}")

item_exists = acronyms_and_transalations.get("lol")
print(item_exists)

item_prices = {"apple": 0.50, "banana": 0.20, "orange": 0.35, "grapes": 0.75, "kiwi": 1.25, "mango": 0.80, "pear": 0.60, "strawberry": 0.90, "watermelon": 2.50, "pineapple": 1.50, "peach": 0.70, "plum": 0.65, "blueberry": 1.00, "raspberry": 1.10, "blackberry": 1.20, "cherry": 1.30, "apricot": 0.85, "pomegranate": 1.40, "lemon": 0.45, "lime": 0.40}

for (item, price) in item_prices.items():
    print(f"{item.capitalize()} costs ${price:.2f}")
print(f"Total price of all items: ${sum(item_prices.values()):.2f}")