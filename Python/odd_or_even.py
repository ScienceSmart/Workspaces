#Asks the user for a number and prints an appropiate message depending on the number
num = int(input("Enter an integer: "))
if (num % 4 == 0):
    print(f"{num} is a multiple of 4.")
elif (num % 2 == 0):
    print(f"{num} is an even number.")
else: 
    print(f"{num} is an odd number.")