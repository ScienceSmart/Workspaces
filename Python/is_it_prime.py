#Checks if a number is prime 

num = int(input("Enter a number to check if is prime: "))
if ([i for i in range(1,num+1) if num % i == 0]) == [1,num]:
    print(f"{num} is a prime number. ")
else: 
    print(f"{num} is a composite number. ")

