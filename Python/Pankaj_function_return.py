
#q1
# Function that returns the sum of two numbers
def add_numbers(a, b):
    return a + b

# Function that returns the square of a number
def square_number(num):
    return num ** 2

# Function that checks if a number is even
def is_even(num):
    return num % 2 == 0

# Function that returns a greeting message
def greet(name):
    return f"Hello, {name}!"

# Function that concatenates two strings
def concatenate_strings(str1, str2):
    return str1 + str2

# Usage examples
result = add_numbers(5, 3)
print("Sum:", result)

result = square_number(4)
print("Square:", result)

result = is_even(7)
print("Is even?", result)

message = greet("John")
print(message)

result = concatenate_strings("Hello", "World")
print("Concatenated string:", result)


#q2
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")

# Normal formula to recreate the operations
result = age + (height - (weight * (iq / 2)))
print("Result using normal formula:", result)


#q3
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

result = divide(subtract(multiply(add(10, 5), 2), 4), 3)
print("Result:", result)
