name = input("What is your name ")
print("hello", name)
age = input("How old are you? ")
try:
    age = int(age) # i am trying to convert it to a number
except ValueError:
    print("You are trying to trick me")
    print("Better luck next time")
except ZeroDivisionError:
    print("You can not divide by zero")
except:
    print("Something unexpected happened")
else: #this happens if no error occurred
    print("you were probably born in", 2024-age)
finally:
    print("Thanks for playing")