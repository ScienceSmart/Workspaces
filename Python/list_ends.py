#Takes a list of numbers and makes a new list of only the first and last elements of the given list.

def list_ends(a):
    return [a[0], a[(len(a)-1)]]

print(list_ends([56, 37, 45]))