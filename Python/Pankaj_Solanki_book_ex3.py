print("I will now count my chickens:") #simply printing the statement given
print("Hens", 25 + 30 / 6) #first print word then perform calc first divide 30 by 6 then add 5 to ans
print("Roosters", 100 - 25 * 3 % 4) #first print word then first modulus then multiply then minus 
print("Now I will count the eggs:") 
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)# performing thecalc according to the bodmas priority of operator
print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7) # 5 is greater than -2 hence print false
print("What is 3 + 2?", 3 + 2) # will print sum to 3+2 = 5
print("What is 5 - 7?", 5 - 7)# will print sum to 5 - 7  = -2
print("Oh, that's why it's False.")
print("How about some more.")
print("Is it greater?", 5 > -2) #print true
print("Is it greater or equal?", 5 >= -2)#print True because one condition is satisfied (5>-2)
print("Is it less or equal?", 5 <= -2)# 5 is not <= to 2 hence print false



#q2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2


print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)
