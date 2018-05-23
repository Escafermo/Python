# NORMAL DICT
print('Normal dictionary:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'
d['f'] = 'F'
d['g'] = 'G'
d['h'] = 'H'
for k, v in d.items():
    print(k, v)

# ORDERED DICT:
from collections import OrderedDict
print('OrderedDict:')
d2 = OrderedDict()
d2['a'] = 'A'
d2['b'] = 'B'
d2['c'] = 'C'
d2['d'] = 'D'
d2['e'] = 'E'
d2['f'] = 'F'
d2['g'] = 'G'
d2['h'] = 'H'
for k2, v2 in d2.items():
    print(k2, v2)

# NORMAL DICT COMPARISON
print('These dictionaries are equal?')
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'
print(d1==d2)

# ORDERED DICT COMPARISON
print('These ordered dictionaries are equal?')
d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'
print(d1==d2)