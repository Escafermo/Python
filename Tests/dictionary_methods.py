# DICTIONARY COMPREHENSION - Dictionary Data Types also support their own version of comprehension for quick creation

print('\nCREATING A DICTIONARY USING COMPREHENSION')

d = {x:x**2 for x in range(10)}
print (d)

# ITERATION - Dictionaries can be iterated over using the keys(), values() and items() methods

print('\nITERATING THROUGH KEYS, VALUES, ITEMS')

d = {'k1':1,'k2':2}

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for item in d.items():
    print(item)

# VIEWING - By themselves the keys(), values() and items() methods return a dictionary view object. This is not a separate list of items.
#			Instead, the view is always tied to the original dictionary.

print('\nVIEWING KEYS')

key_view = d.keys()
print(key_view)
d['k3'] = 3
print(d)
print(key_view)