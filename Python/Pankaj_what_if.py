#q1
'''In Python, the if statement is a conditional statement that allows you to control the flow of your code based on a certain condition. The code under the if statement is called the "if block" or "if clause".'''

#q2
'''By indenting the code under the if statement, we clearly define which statements are part of the if block and should be executed conditionally. The consistent indentation ensures code readability and helps 
Python determine the correct grouping of statements.'''
#q3
'''If the code under the if statement is not indented, it will result in a syntax error in Python'''

#q4
'''changing the initial values for people, cats, and dogs, if you modify these values, the behavior of the code will change based on the new values'''

#q5
people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

if cats == dogs and people != dogs:
    print("Cats are equal to dogs, but people are not.")

if people > 10 and dogs < 20:
    print("There are many people, but not many dogs.")

if cats > 20 or dogs > 20:
    print("Either there are many cats or many dogs.")

if not (people == 0 and cats == 0 and dogs == 0):
    print("At least one of the variables is not zero.")
