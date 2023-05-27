'''from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())


file_again = input("> ")
txt_again = open(file_again)'''

#q2

filename = input("Enter the filename: ")

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())

#q3
filename = input("Enter the filename: ")

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())
