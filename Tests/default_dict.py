from collections import defaultdict
d  = defaultdict(object)
d['one'] 
for item in d:
    print(item)

#Can also initialize with default values:
d2 = defaultdict(lambda: 0)
d2['one']
print(d2)