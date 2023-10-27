#Take two lists and returns a list that contains only the elements that are common between the lists

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

import random

a = random.sample(range(0, 100), 10)
b = random.sample(range(0, 120), 13)
print(set([x for x in a for y in b if x==y ]))