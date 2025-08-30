
#! Tuples method

num = {
    'nisarg': "panchal",
    'nisarg': "panchal",
    'nisarg': "panchal",    
    }
# num = (1,2,34,5,6,8,1,3,1)
print(type(num))

# #* type of tuples in methods


#? Tuples Methods

#! tuple created Examples

# t1 = (1, 2, 3)
# t2 = ("apple", "banana", "cherry")
# t3 = (1, "hello", 3.14)
# t4 = ()               # Empty tuple
# t5 = (5,)             # Single element tuple (Note the comma)


#! Accessing Elements

# t = (10, 20, 30, 40)
# print(t[0])      # 10
# print(t[-1])     # 40 (last element)

#! type of tuples methds

# t = (1,2,3,4,5,2,3,5,1,3,2,6,7,8,9)
# print(t.count(2))
# print(t.index(2))


#! tuples Operations
#? concatenation 

# t1 = (1,2,3,4)
# t2 = (3,2,8,6)
# print(t1 + t2)


#? Repetiton 

# print(t1 * 2)

#? Membership 

# print(3 in t1)
# print(9 in t1)


#? slicing 
# print(t1[0:2])


#?  Unpacking 
#*  અહીં tuple (1, 2) પાસે 2 values છે અને left side પણ 2 variables છે, એટલે perfectly unpack થાય છે.
#? ✅ Correct Unpacking Example:
# t2 = (1,6)
# a, b, = t2
# print(a, b)

#? ❌ Incorrect Unpacking Example:
# t1 = (1, 2, 3)
# a, b = t1

#! advanced tuples concept

#? 1. Tuple Packing and Unpacking

# # Packing
# student = ("Alice", 20, "IT")

# # Unpacking
# name, age, branch = student
# print(name, age, branch)

# ? nested of tuples

# nested = ((1, 2), ([3], 4), (5, 6))
# print(nested[1][0][0])   # 3


# #?  tuples Loop
# for item in ("apple", "banana" , "coffe"):
#     print(item)



# t = ([1, 2], 3)
# t[0].append(4)       # Valid! Tuple is immutable, but list inside is not


# students = (
#     ("Alice", 70),
#     ("Bob", 85),
#     ("Charlie", 60),
#     ("David", 90),
# )

# def top_students(data):
#     avg = sum([x[1] for x in data]) / len(data)
#     return tuple(s for s in data if s[1] > avg)

# print(top_students(students))




