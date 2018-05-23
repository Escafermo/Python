from collections import namedtuple

Dog = namedtuple('Dog','age breed name')

sam = Dog(age=2,breed='Lab',name='Sammy')

print (sam)
print (sam.age)
print (sam[0])
print (sam.breed)
print (sam[1])
print (sam.name)
print (sam[2])