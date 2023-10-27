#Asks the user for a number and then prints out a list of all the divisors of that number. 

num = int(input("Enter a number: "))
x = [i for i in range(1,num) if num % i == 0]
print(x)