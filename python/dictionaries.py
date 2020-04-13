# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    'first_name': 'ravi',
    'last_name': 'goswami',
    'age': 30
}


# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '8439291909'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Agra'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Himanshu', 'age': 25},
    {'name': 'Tanay', 'age': 25}
]

print(people[1]['name'])
