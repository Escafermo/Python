import pdb

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

# Set a trace using Python Debugger
print ('\n<<< STARTING PYTHON DEBUGGER >>>\n>>> INPUT q TO QUIT <<<\n')
pdb.set_trace()

result2 = y+x
print(result2)