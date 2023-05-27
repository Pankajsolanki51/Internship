#q1 q2 
print("We're going to erase the file.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
filename = input("Enter the filename: ")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}\n")

# Move the input("?") statement here
input("Press Enter to continue...")

print("And finally, we close it.")
target.close()

#q3
'''The reason we pass the 'w' parameter to the open() function is to specify the mode in which we want to open the file. In this case, 'w' stands for write mode.'''

#q4
'''No, if you open the file with 'w' mode, calling target.truncate() immediately after is not necessary.

When you open a file in 'w' (write) mode using open(), it automatically truncates the file, which means it clears its contents. Opening the file in write mode effectively starts with an empty file, ready to be written to.

In the given code, calling target.truncate() after opening the file in write mode is redundant because the file is already truncated when it was opened. It doesn't have any impact on an empty file.'''
