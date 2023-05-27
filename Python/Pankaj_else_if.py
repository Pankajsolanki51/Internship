#q1
'''will be executed, and it will print "We should take the cars."
If the above condition is not true and the number of cars is less than the number of people (cars < people), the code block under the elif statement will be executed, and it will print "We should not take the cars."
If both of the above conditions are false, the code block under the else statement will be executed, and it will print "We can't decide."'''

#q2 q3 
people = 30  # Set the value of 'people' to 30
cars = 40  # Set the value of 'cars' to 40
trucks = 15  # Set the value of 'trucks' to 15

if cars > people:  # If the number of cars is greater than the number of people
    print("We should take the cars.")  # Print the message "We should take the cars."
elif cars < people:  # If the number of cars is less than the number of people
    print("We should not take the cars.")  # Print the message "We should not take the cars."
else:  # If none of the above conditions are true
    print("We can't decide.")  # Print the message "We can't decide."

if trucks > cars:  # If the number of trucks is greater than the number of cars
    print("That's too many trucks.")  # Print the message "That's too many trucks."
elif trucks < cars:  # If the number of trucks is less than the number of cars
    print("Maybe we could take the trucks.")  # Print the message "Maybe we could take the trucks."
else:  # If none of the above conditions are true
    print("We still can't decide.")  # Print the message "We still can't decide."

if people > trucks:  # If the number of people is greater than the number of trucks
    print("Alright, let's just take the trucks.")  # Print the message "Alright, let's just take the trucks."
else:  # If the number of people is not greater than the number of trucks
    print("Fine, let's stay home then.")  # Print the message "Fine, let's stay home then."
