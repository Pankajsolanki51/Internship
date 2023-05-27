#q1

#Here are a few reasons why one might choose to use triple-single-quotes instead:

#Consistency: If you are working with code that already extensively uses double-quotes for string literals, using triple-single-quotes for multi-line strings helps maintain consistency in your code.

#Readability: In some cases, using triple-single-quotes can improve the readability of your code. For example, if your multi-line string contains a lot of double-quotes within it, using triple-single-quotes avoids the need for excessive escaping or string concatenation.

#Differentiating string types: In Python, strings can be defined using single-quotes ('), double-quotes ("), triple-single-quotes (''')  or triple-double-quotes ("""). 

#q2
name = "Pankaj"
age = 19
message = "Hello, {name}!\nYou are {age} years old."
print(message.format(name=name, age=age))

name = "Rahul"
job = "Engineer"
salary = 50000

message = "Name: {name}\nJob: {job}\nSalary: ${salary:,.2f}"
print(message.format(name=name, job=job, salary=salary))

