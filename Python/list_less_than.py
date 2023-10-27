#Gives numbers than the list provided
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Enter a number: "))
b = [x for x in a if x < num]
print(b)