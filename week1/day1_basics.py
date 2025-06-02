## data type parent: primitives

# ints
xInt = 1
yInt = 2
print(xInt, "is an int.")
print(yInt, "is an int.\n")

# floats
xFloat = 1.234
yFloat = 2.468
print(xFloat, "is a float.")
print(yFloat, "is a float.\n")

# booleans
xBool = True
yBool = False
print("The value of xBool is", xBool, ".")
print("The value of yBool is", yBool, ".\n")

## data type parent: containers

# lists
xList = ["apple", "pear", "strawberry", "mango", "lemon", "lime", "peach"]
print(xList, " is a list.")
print("The second through fourth items in the xList list are,", xList[1:5], ".\n")

# sets
xSet = {"Ben", "Val", "Prentiss", "Anita", "Bill"}
print(xSet, "is a set of people in Inno.\n")

# dictionaries
xDict = {"Rylee":"GSD", "Daniel":"Doodle", "Scout":"Cavapoo"}
print("The second dictionary value is", xDict["Daniel"], ".\n") 

# tuples

## accessing things in containers (lists, in this case)

# direct indexing takes a known position and returns the value
print("The second item in the xList list is", xList[1], ".")
print("The first item in teh xList list is", xList[-7], ".\n")

# using index() takes a value and returns its position
print("What item index is 'strawberry'? It's #", xList.index("strawberry"), ".\n")

# slicing
print("The third item in the xList list is", xList[3], ".")
print("The second, third, and fourth items in the xList are,", xList[1:3], ".")
print("Every other item in the xList list is", xList[0::2], ".")
print("The reverse order of the items in xList are", xList[::-1], ".\n")

# unpacking
first, *rest = xList
print(first, "is the first item in the list.", rest, "are the rest of the items.")
first, *middle, last = xList
print(first, "is the first item in the list.", middle, "are the middle items, and", last, "is the last item in the list.\n")

## modifying things in containers - append method
xList.append("guava")
print("Just appended to xList was", xList[-1], ".\n")
