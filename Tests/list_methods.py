# APPEND - Appends an element to the end of a list

print ('\nAPPENDING TO THE END OF THE LIST\n')

list1 = [1,2,3]
print(list1)
list1.append(4)
print(list1)


# CREATE NEW AND APPEND

print ('\nCREATING NEW LIST AND APPENDING TO THE END OF THE LIST\n')


x = [1,2,3]
y = x.copy()
print (y)
y.append(4)
print (y)
print(x)

# EXTEND - Extends list by appending elements from the iterable

print ('\nAPPENDING x EXTENDING THE LIST\n')

x = [1, 2, 3]
print(x)
x.append([4, 5])
print(x)

x = [1, 2, 3]
print(x)
x.extend([4, 5])
print(x)


# COUNT - Returns the number of times it occurs in a list

print ('\nCOUNTING OCCURENCES OF 10 AND 2\n')

print(list1)
print (list1.count(10))
print (list1.count(2))

# INDEX - Returns the index of whatever element is placed as an argument

print ('\nRETURNING THE INDEX OF 2\n')

print(list1)
print (list1.index(2))
#print (list1.index(12)) <- ERROR

# INSERT - Places the object at the index supplied

print ('\nPLACING OBJECT IN INDEX POS\n')

print (list1)
list1.insert(2,'inserted')
print (list1)


# POP - Removes the last element of a list. Passing an index position can remove and return a specific element.

print ('\nPOPING - REMOVING ELEMENTS FROM LIST\n')

print(list1)
l1 = list1.pop(1)
print (list1)
print (l1)


# REMOVE - Removes the first occurrence of a value

print ('\nREMOVING FIRST OCCURENCE OF VALUE\n')

print(list1)
list1.remove('inserted')
print(list1)

list2 = [1,2,3,4,3]
print(list2)
list2.remove(3)
print(list2)

# REVERSE - Reverses a list

print ('\nREVERSING LIST\n')

print(list2)
list2.reverse()
print(list2)


# SORT - Sorts a list

print ('\nSORTING LIST\n')

print(list2)
list2.sort()
print(list2)
