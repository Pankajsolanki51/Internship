#q1
# Import the 'argv' module from the 'sys' package
from sys import argv

# Unpack the command line arguments
script, input_file = argv

# Define a function to print the contents of a file
def print_all(f):
    print(f.read())

# Define a function to rewind the file back to the start
def rewind(f):
    f.seek(0)

# Define a function to print a specific line of the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open the file specified by the command line argument
current_file = open(input_file)

print("First let's print the whole file:\n")

# Call the print_all function to print the entire contents of the file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Call the rewind function to set the file pointer back to the beginning of the file
rewind(current_file)

print("Let's print three lines:")

# Set the current line variable to 1 and print the first line
current_line = 1
print_a_line(current_line, current_file)

# Increment the current line variable and print the second line
current_line += 1
print_a_line(current_line, current_file)

# Increment the current line variable again and print the third line
current_line += 1
print_a_line(current_line, current_file)


#q2
'''The seek() function is a method available for file objects in Python. It is used to change the current position (or offset) within the file'''