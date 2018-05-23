s = set()

s.add(1)
s.add(2)
print (s)

# CLEAR - removes all elements from the set

print ('\nCLEARING\n')

s.clear()
print (s)

# COPY - returns a copy of the set

print ('\nCOPYING\n')

s = {1,2,3}
sc = s.copy()
s.add(4)
print (sc)
print (s)

# DIFFERENCE - returns the difference of two or more sets

print ('\nCHECKING DIFFERENCE\n')

print (s.difference(sc))

# DIFFERENCE UPDATE - returns set1 after removing elements found in set2

print ('\nUPDATING FROM DIFFERENCE\n')

s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2)
print (s1)
print (s2)

# DISCARD - Removes an element from a set if it is a member. If the element is not a member, do nothing.

print ('\nDISCARDING NUM 2\n')

s = {1,2,3,4}
print(s)
s.discard(2)
print(s)

# INTERSECTION - Returns the intersection of two or more sets as a new set.(i.e. elements that are common to all of the sets.)

print ('\nINTERSECTION BETEWEEN SETS\n')

s1 = {1,2,3}
s2 = {1,2,4}
print (s1.intersection(s2))
print (s1)
print (s2)

# INTERSECTION UPDATE - Returns the intersection of two or more sets and UPDATES s1

print ('\nUPDATING FROM INTERSECTION BETEWEEN SETS\n')

print (s1.intersection_update(s2))
print (s1)
print (s2)


# ISDISJOINT - This method will return True if two sets have a null intersection.

print ('\nCHECKING IF SETS ARE DISJOINT\n')

s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
print (s1.isdisjoint(s2))
print (s1.isdisjoint(s3))

# ISSUBSET - This method reports whether another set contains this set.

print ('\nCHECKING IF SUBSET\n')

print(s1.issubset(s2))

# ISSUPERSET - This method will report whether this set contains another set.

print ('\nCHECKING IF SUPERSET\n')

print(s2.issuperset(s1))
print(s1.issuperset(s2))

# SYMETRIC DIFFERENCE - Return the symmetric difference of two sets as a new set.(i.e. all elements that are in exactly one of the sets.)

print ('\nCHECKING SYMETRIC DIFFERENCE\n')

print(s1.symmetric_difference(s2))

# UNION - Returns the union of two sets (i.e. all elements that are in either set.)

print ('\nRETURNING UNION OF SETS\n')

print(s1.union(s2))

# UPDATE - Update a set with the union of itself and others.

print ('\nUPDATING FROM UNION OF SETS\n')

s1.update(s2)
print (s1)