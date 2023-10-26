#Asks the user their name and age and prints a message that tells them the year they turn a hundred
#Asks a number and prints out that many copies of the previous message
import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = datetime.date.today().year - age + 100 
print(f"Hey, {name}, you will turn 100 in {year}")

num = int(input("Enter an integer for how many copies: "))
for x in range(0,num):
    print(f"Hey, {name}, you will turn 100 in {year}\n")