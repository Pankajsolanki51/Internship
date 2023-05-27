#q1
def number_game(limit):
    i = 0
    numbers = []

    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1

        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers:")

    for num in numbers:
        print(num)

# Call the function with a specific limit
number_game(6)


#q2
def number_game(limit):
    i = 0
    numbers = []

    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1

        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers:")

    for num in numbers:
        print(num)

# Prompt the user for a limit
limit = int(input("Enter a limit: "))

# Call the number_game function with the user-defined limit
number_game(limit)


#q3
def number_game(limit, increment):
    i = 0
    numbers = []

    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment

        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers:")

    for num in numbers:
        print(num)

# Prompt the user for a limit and an increment value
limit = int(input("Enter a limit: "))
increment = int(input("Enter an increment value: "))

# Call the number_game function with the user-defined limit and increment
number_game(limit, increment)


#q4
def number_game(limit, increment):
    numbers = []

    for i in range(0, limit, increment):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now:", numbers)
        print(f"At the bottom i is {i + increment}")

    print("The numbers:")

    for num in numbers:
        print(num)

# Prompt the user for a limit and an increment value
limit = int(input("Enter a limit: "))
increment = int(input("Enter an increment value: "))

# Call the number_game function with the user-defined limit and increment
number_game(limit, increment)


'''The incrementor in the middle is no longer needed since the range takes care of that. The behavior of the code remains the same; however, if you do not remove the incrementor in the middle (i = i + increment), it will result in an incorrect incrementing behavior since the for-loop and the range function already handle the iteration and incrementing automatically.'''