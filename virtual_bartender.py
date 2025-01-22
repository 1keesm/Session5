from random import choice
drinks = ["vodka", "gin", "whiskey", "rum", "tequila", "absinthe", "sake"]
#print(choice(drinks))
name = input("I am the virtual bartender. What is your name? ")
try:
    age = input("what is your age? ")
    age = int(age)
    country = input("What is your country? ")
    legal = False
    if age >= 21:
        legal = True
    elif age >= 18 and (country != "USA" and country != "UAE"):
        legal = True
    elif age >= 16 and country == "Luxembourg":
        legal = True
except ValueError:
    print("dont play games with me")
else:
    if legal:
        print("Dear ", name, " i will be serving you ", choice(drinks))
    else:
        print("dear ", name, " unfortunately i can not serve you")