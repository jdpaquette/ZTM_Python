# Exercise 78 ZTM_Python
# Find Duplicates

some_list = ["a", "b", "c", "b", "d,","m","n","n"]

duplicates = []

for value in some_list:
    if some_list.count(value) > 1: # counts number of times item in list exists
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
