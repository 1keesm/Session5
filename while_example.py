#you have 3 lives, if you get a 6 you win
# if you do not get a 6, you lose a life
from random import randint

lives = 3
while lives >6: #as long as i have more lives
    # roll the dic e
    dice = randint(1,6)
    if dice == 6:
        print("You rolled a 6 you win!")
        break
    lives -=1
    print("you rolled a ", dice, " you have ", lives, " lives left")

if lives == 0:
    print("You lose!")