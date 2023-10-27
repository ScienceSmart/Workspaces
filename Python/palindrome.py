#Checks if a string is a palindrome 

word = str(input("Enter a string: "))
reverse = word[::-1]
if (word != reverse):
    print(f"{word} is not a palindrome.")
else: 
    print(f"{word} is a palindrome.")