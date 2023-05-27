#q1
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Prints the number of cheeses
    print(f"You have {cheese_count} cheeses!")
    # Prints the number of boxes of crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # Prints a statement about having enough for a party
    print("Man that's enough for a party!")
    # Prints a statement to get a blanket
    print("Get a blanket.\n")

# Prints a line using function arguments directly
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Prints a line using variables defined in the script
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Prints a line using math operations in the function arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Prints a line using variables and math operations in the function arguments
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#q2
def calculate_discount(original_price, discount_percentage):
    # Calculate the discounted price
    discount_amount = original_price * (discount_percentage / 100)
    discounted_price = original_price - discount_amount

    # Return the discounted price
    return discounted_price


# 1. Passing arguments directly
print(calculate_discount(100, 20))

# 2. Using variables for the original price and discount percentage
price = 75
discount = 15
print(calculate_discount(price, discount))

# 3. Accepting input from the user for the original price and discount percentage
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))
print(calculate_discount(original_price, discount_percentage))

# 4. Using default values for the original price and discount percentage
def calculate_discount(original_price=200, discount_percentage=10):
    # Rest of the function code remains the same
    pass

print(calculate_discount())

# 5. Assigning the function to a variable and calling it later
discount_func = calculate_discount
print(discount_func(80, 25))

# 6. Passing the arguments as a dictionary
args = {"original_price": 150, "discount_percentage": 30}
print(calculate_discount(**args))

# 7. Unpacking a list or tuple to pass arguments
arguments = [120, 15]
print(calculate_discount(*arguments))

# 8. Using keyword arguments
print(calculate_discount(original_price=90, discount_percentage=12))

# 9. Storing the result in a variable
discounted_price = calculate_discount(200, 20)
print(f"The discounted price is: {discounted_price}")

# 10. Using the function within a loop
prices = [50, 100, 150]
discounts = [10, 20, 30]
for price, discount in zip(prices, discounts):
    print(calculate_discount(price, discount))
