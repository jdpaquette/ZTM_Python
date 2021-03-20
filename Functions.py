# Functions
# ZTM Exercise 88

def highest_even(*args):
    even = []
    for items in args:
        if items % 2 == 0:
            even.append(items)
    return max(even)
print(highest_even(6,10,2,3,4,8,11))