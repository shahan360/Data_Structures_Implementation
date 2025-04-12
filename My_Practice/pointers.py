num1 = 11
num2 = 11
print("Before num2 value is updated:")
print("num1:", num1)
print("num2:", num2)
print("num1 points to:", id(num1))
print("num2 points to:", id(num2))
print("\n")
num2 = 22
print("After num2 value is updated:")
print("num1:", num1)
print("num2:", num2)
print("num1 points to:", id(num1))
print("num2 points to:", id(num2))

#Dictionary pointers concept

# if we are creating two dictionary with same key and value, they will point to the same memory location as shown below
dict1 = {'key1': 11}
dict2 = dict1
print("\n")
print("Before dict2 value is updated:")
print("dict1:", dict1)
print("dict2:", dict2)
print("dict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
print("\n")

# if we are updating the value of dict2, it will not affect dict1 and both will point to same memory location
dict1['key1'] = 22
dict2['key1'] = 22
print("After dict2 value is updated:")
print("dict1:", dict1)
print("dict2:", dict2)
print("dict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))