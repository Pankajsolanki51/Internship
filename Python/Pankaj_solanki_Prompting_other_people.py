#q1
''' pydoc command is a built-in command-line utility that allows you to access documentation for Python modules, classes, functions, and methods directly from the command line.'''

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

'''on passing three agruments error is occurring because you are trying to unpack the argv list into four variables (script, first, second, third), but there are more than four values in argv.'''