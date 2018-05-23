from collections import Counter


lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]

print (Counter(lst))

print (Counter('aabsbsbsbhshhbbsbs'))


s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

print (Counter(words))

# Methods with Counter()
c = Counter(words)

print (c.most_common(2))

#sum(c.values())                 # total of all counts
#c.clear()                       # reset all counts
#list(c)                         # list unique elements
#set(c)                          # convert to a set
#dict(c)                         # convert to a regular dictionary
#c.items()                       # convert to a list of (elem, cnt) pairs
#Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
#c.most_common()[:-n-1:-1]       # n least common elements
#c += Counter()                  # remove zero and negative counts
