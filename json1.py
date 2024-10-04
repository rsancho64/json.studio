#! /usr/bin/python3

# diccionarios python y marshalling a json



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

if __name__ == "__main__":

  persona = {}
      
  persona["name"] = "John Doe"
  persona["age"] = 30
  persona["email"] = "john.doe@example.com"
  persona["is_employee"] = True
  # print(persona)

  hobbies = [
      "reading",
      "playing soccer",
      "traveling"
  ],

  persona["hobbies"] = hobbies
  # print(persona)

  address = {
      "street": "123 Main Street",
      "city": "New York",
      "state": "NY",
      "zip": "10001"
  }

  # persona["address"] = address
  # print(persona)
  print(type(persona))
  print()

  import json

  # dump ~ coding
  serializedPersona = json.dumps(persona)
  print(serializedPersona)
  print(type(serializedPersona))

  serializedPersona = json.dumps(persona, sort_keys=True, indent=3)
  print(serializedPersona)

  # load ~ decoding

# see https://www.bairesdev.com/tools/json2yaml/
# yaml-equivalente =