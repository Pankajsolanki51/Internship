#q1
# Assign the value 10 to the variable types_of_people
types_of_people = 10

# Create a string using f-string formatting, incorporating the value of types_of_people
x = f"There are {types_of_people} types of people."

# Assign the strings "binary" and "don't" to the variables binary and do_not, respectively
binary = "binary"
do_not = "don't"

# Create a string using f-string formatting, incorporating the values of binary and do_not
y = f"Those who know {binary} and those who {do_not}."

# Print the value of x
print(x)

# Print the value of y
print(y)

# Create a string with a placeholder for later formatting
joke_evaluation = "Isn't that joke so funny?! {}"

# Assign the value False to the variable hilarious
hilarious = False

# Print the formatted joke_evaluation string, replacing the placeholder with the value of hilarious
print(joke_evaluation.format(hilarious))

# Assign the string "This is the left side of..." to the variable w
w = "This is the left side of..."

# Assign the string "a string with a right side." to the variable e
e = "a string with a right side."

# Concatenate the strings w and e and print the result
print(w + e)


#q2
#Line 6: x = f"There are {types_of_people} types of people."
#Line 13: y = f"Those who know {binary} and those who {do_not}."

#q3
'''The reason the resulting string is longer is that the + operator, when used with strings, performs concatenation, meaning it combines the characters of the two strings to create a new string.'''