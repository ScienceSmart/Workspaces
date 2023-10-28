#Generates a random number between 1 and 9 (including 1 and 9). 
#Ask the user to guess the number, then tell them whether they guessed 
#too low, too high, or exactly right

import random


num = random.randint(1,9)
i = 0
guess = 0
while (guess != num and guess != "exit"):
    guess = input("Guess a number between 1-9 or type exit to quit: ")
    if (guess == "exit"):
        break
    elif (int(guess) == num):
        print("Your answer is exactly right. ")
        break
    elif (int(guess) < num):
        print("Your answer is too low. ")
        i = i + 1
    elif (int(guess) > num):
        print("Your answer is too high. ")
        i = i + 1
print(f"You took {i} guesses before getting it right. ")
    