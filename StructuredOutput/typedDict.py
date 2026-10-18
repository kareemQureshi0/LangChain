from typing import TypedDict

class Person(TypedDict):
    
    name : str
    age : int
    
new_person : Person = {'name' : 'Abdul Kareem','age':50}

print(new_person)