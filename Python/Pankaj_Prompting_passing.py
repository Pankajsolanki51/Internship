from sys import argv

script, user_name = argv
new_prompt = '>>> '  # New prompt value

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(new_prompt)

print(f"Where do you live {user_name}?")
lives = input(new_prompt)

print("What kind of computer do you have?")
computer = input(new_prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")


#q2
from sys import argv

script, user_name, additional_argument = argv
new_prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(new_prompt)

print(f"Where do you live {user_name}?")
lives = input(new_prompt)

print("What kind of computer do you have?")
computer = input(new_prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
The additional argument you provided is: {additional_argument}
""")
