""" use key value pairs"""

store = {
    "name": "ram",
    "age": 25,
    'sex': 'male',
    'height': 6.0
}

store['height']
store['country'] = 'India'
del store['age']
print(store)

