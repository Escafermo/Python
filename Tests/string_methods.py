s = 'hello world'

# Capitalize first word in string
print (s.capitalize())

# Uppercase entire string
print (s.upper())

# Lowercase entire string
print (s.lower())

# Count occurrences
print (s.count('o'))

# Returns position of first occurence
print (s.find('o'))

# Input string as center
print (s.center(20,'z'))     # String of total size 20, with the string 's' in the midle

# Expanding tabs without print \t
'hello\thi'.expandtabs()

# Is check methods
s = 'hello'
print (s.isalnum())     # Will return True if all characters in s are alphanumeric
print (s.isalpha())		# Will return True if all characters in s are alphabetic
print (s.islower())		# Will return True if all cased characters in s are lowercase and there is at least one cased character in s
print (s.isspace())		# Will return True if all characters in s are whitespace.
print (s.istitle())		# Will return True if s is a title cased string and there is at least one character in s
print (s.isupper())		# Will return True if all cased characters in s are uppercase and there is at least one cased character in s
print (s.endswith('o'))	# Essentially the same as a boolean check on s[-1]

# Split and partition 
print (s.split('e'))		# We can use split() to split the string at a certain element and return a list of the results
print (s.partition('l'))	# We can use partition() to return a tuple that includes the first occurrence of the separator sandwiched between the first 					# half and the end half