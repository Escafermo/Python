# Create in-memory file-like objects within your program that Python treats the same way. 
# Text data is stored in a StringIO object, while binary data would be stored in a BytesIO object. 
# This object can then be used as input or output to most functions that would expect a standard file object.

import io

# Arbitrary String
message = 'This is just a normal string.'

# Use StringIO method to set as file object
f = io.StringIO(message)

#Now we have an object f that we will be able to treat just like a file. For example:
print (f.read())

#We can also write to it:
f.write(' Second line written to file-like object')

# Reset cursor just like you would a file
f.seek(0)

# Read again
print (f.read())

# Close the object when contents are no longer needed
f.close()