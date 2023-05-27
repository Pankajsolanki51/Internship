#q1
'''ten_things.split(' ') - This splits the string ten_things into a list of items using the delimiter ' ' (space). It can be translated as split(ten_things, ' ').

more_stuff.pop() - This removes and returns the last item from the list more_stuff. It can be translated as pop(more_stuff).

stuff.append(next_one) - This adds the value of next_one to the end of the list stuff. It can be translated as append(stuff, next_one).

len(stuff) - This returns the length of the list stuff. It can be translated as len(stuff).

stuff.pop() - This removes and returns the last item from the list stuff. It can be translated as pop(stuff).

' '.join(stuff) - This joins the items in the list stuff into a single string, with each item separated by a space. It can be translated as ' '.join(stuff).

'#'.join(stuff[3:5]) - This joins the items at indices 3 and 4 in the list stuff into a single string, with '#' as the separator. It can be translated as '#'.join(stuff[3:5]).'''

#q2
'''
more_stuff.pop(): This reads as "Call the pop() method on more_stuff." It means that we are invoking the pop() function as a method on the more_stuff list object.

pop(more_stuff): This reads as "Call the pop() function with the argument more_stuff." It means that we are calling the pop() function and passing more_stuff as an argument to the function
'''

#q3
'''
In object-oriented programming (OOP), a class is a blueprint or template for creating objects. It defines the common characteristics (attributes) and behaviors (methods) that objects of a certain type will have'''

#q4
'''Fruits: ["Apple", "Orange", "Banana", "Mango", "Strawberry"]
Colors: ["Red", "Blue", "Green", "Yellow", "Purple"]
Countries: ["United States", "China", "India", "Brazil", "Russia"]
Animals: ["Dog", "Cat", "Elephant", "Lion", "Giraffe"]
Sports: ["Football", "Basketball", "Tennis", "Soccer", "Golf"]
Books: ["To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Great Gatsby", "Harry Potter"]
Programming Languages: ["Python", "Java", "C++", "JavaScript", "Ruby"]
Car Brands: ["Toyota", "Honda", "Ford", "BMW", "Mercedes-Benz"]
Musical Instruments: ["Guitar", "Piano", "Violin", "Drums", "Trumpet"]
Planets: ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]'''

fruits = ["Apple", "Orange", "Banana", "Mango", "Strawberry"]
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]

# Accessing elements in a list
print(fruits[0])  # Output: Apple
print(colors[2])  # Output: Green

# Modifying list elements
fruits[3] = "Pineapple"
print(fruits)  # Output: ["Apple", "Orange", "Banana", "Pineapple", "Strawberry"]

# Adding elements to a list
fruits.append("Grapes")
print(fruits)  # Output: ["Apple", "Orange", "Banana", "Pineapple", "Strawberry", "Grapes"]

# Removing elements from a list
removed_fruit = fruits.pop(1)
print(removed_fruit)  # Output: Orange
print(fruits)  # Output: ["Apple", "Banana", "Pineapple", "Strawberry", "Grapes"]

# Combining two lists
combined_list = fruits + colors
print(combined_list)  # Output: ["Apple", "Banana", "Pineapple", "Strawberry", "Grapes", "Red", "Blue", "Green", "Yellow", "Purple"]

# Iterating over a list
for fruit in fruits:
    print(fruit)

# Checking if an element is in a list
if "Mango" in fruits:
    print("Mango is in the list!")
