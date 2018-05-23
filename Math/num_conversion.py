# Using the function hex() you can convert numbers into a hexadecimal format:

print('\nCONVERTING TO HEXADECIMAL\n')

print (hex(246))
print(hex(512))

# Using the function bin() you can convert numbers into their binary format.

print('\nCONVERTING TO BINARY\n')

print (bin(1234))
print (bin(128))
print (bin(512))

# The function pow() takes two arguments, equivalent to x^y. 
# With three arguments it is equivalent to (x^y)%z, but may be more efficient for long integers.

print('\nCONVERTING TO POTENCY\n')

print (pow(3,4))
print (pow(2,2))
print (pow(3,4,5))

# The function abs() returns the absolute value of a number. 
# The argument may be an integer or a floating point number. If the argument is a complex number, its magnitude is returned.

print('\nCONVERTING TO ABSOLUTE\n')

print (abs(-3.14))
print (abs(-50))
print (abs(3))

# The function round() will round a number to a given precision in decimal digits (default 0 digits). 
# It does not convert integers to floats.

print('\nCONVERTING TO ROUNDED\n')

print (round(3,2))
print (round(395,-2))
print (round(3.1415926535,2))
