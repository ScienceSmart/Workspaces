#Takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

#Uses set
def no_duplicates0(x):
    return list(set(x))

#Uses for loop
def no_duplicates1(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

print(no_duplicates0([5,5,5,45,23,4]))

#Exercise 15: Reverse Word Order
def reverse(x):
   rword = ""
   words = x.split()[::-1]
   for x in range(0, len(words)):
        rword = rword + words[x] + " "
   return rword
print(reverse("My name is Erkin"))

#Exercise 15: Reverse Word Order Quicker
def reverseWord(w):
  return ' '.join(w.split()[::-1])