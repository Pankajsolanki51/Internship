#q1

states = {
    'Maharashtra': 'MH',
    'Karnataka': 'KA',
    'Tamil Nadu': 'TN',
    'Uttar Pradesh': 'UP',
    'Gujarat': 'GJ'
}

cities = {
    'MH': 'Mumbai',
    'KA': 'Bengaluru',
    'TN': 'Chennai',
    'UP': 'Lucknow',
    'GJ': 'Ahmedabad'
}

# Add more cities and states if desired
cities['MH'] = 'Pune'
cities['KA'] = 'Mysuru'

# Print some cities
print('-' * 10)
print("MH State has: ", cities['MH'])
print("TN State has: ", cities['TN'])

# Print some states
print('-' * 10)
print("Uttar Pradesh's abbreviation is: ", states['Uttar Pradesh'])
print("Gujarat's abbreviation is: ", states['Gujarat'])

# Print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# Print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# Perform both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev} and has city {cities[abbrev]}")


#q2
'''
Dictionaries do not guarantee the order of key-value pairs.
Keys must be unique and immutable.
Dictionaries are not index-based.
Key lookup is case-sensitive.
Dictionaries cannot be sorted directly.
No built-in method for direct value lookup.
'''