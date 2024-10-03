#! /usr/bin/python3

# diccionarios python studio

target = '''
{
  "name": "John Doe",
  "age": 30,
  "email": "john.doe@example.com",
  "is_employee": true,
  "hobbies": [
    "reading",
    "playing soccer",
    "traveling"
  ],
  "address": {
    "street": "123 Main Street",
    "city": "New York",
    "state": "NY",
    "zip": "10001"
  }
}
'''

persona = {}
      
persona["name"] = "John Doe"
persona["age"] = 30
persona["email"] = "john.doe@example.com"
persona["is_employee"] = True
print(persona)

hobbies = [
    "reading",
    "playing soccer",
    "traveling"
],

persona["hobbies"] = hobbies
print(persona)

address = {
    "street": "123 Main Street",
    "city": "New York",
    "state": "NY",
    "zip": "10001"
}

persona["address"] = address
print(persona)


#  see https://www.bairesdev.com/tools/json2yaml/

yaml-equivalente =
'''
---
name: John Doe
age: 30
email: john.doe@example.com
is_employee: true
hobbies:
- reading
- playing soccer
- traveling
address:
  street: 123 Main Street
  city: New York
  state: NY
  zip: '10001'
'''

