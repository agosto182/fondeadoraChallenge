## Author: Ivan Agosto
## Date: 3 January 2023
##
## Description:
## The function plain_deep_int_array can plain any deep int array.
##
## To try the function with your values. Please uncomment the line 40
## 
## Unit test are available in the option in left bellow button.
## 

import json

def plain_deep_int_array(int_array: list):
  result = []

  for val in int_array:
    if(type(val) == list):
      result.extend(plain_deep_int_array(val))
    elif(type(val) == int or val.isnumeric()):
      result.append(int(val))
    else:
      raise Exception("Only number values are accepted")

  return result

def tryPlain():
  print("Plain your own array")
  val = input("Enter here your array please: ")
  try:
    array_to_test = json.loads(val)
    res = plain_deep_int_array(array_to_test)
    print("Your result is")
    print(res)
  except Exception as err:
    print('Please enter a valid array:')
    print(err)

## Uncomment the next line to make your own test
tryPlain()