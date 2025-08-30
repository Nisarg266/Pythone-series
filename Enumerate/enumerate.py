
#! Enumerate Function besic 

# fruits = ['apple' , 'banana' , 'paiapple']
# for index , fruit in enumerate(fruits):
#     print(index ,fruit)


#! enumerate start index change number

# fruits = ['apple' , 'banana' , 'paiapple']
# for index , fruit in enumerate(fruits , start = 1):
#     print(index ,fruit)
    

#! using enumerate with string

# word = "nisarg"

# for index , worls in enumerate(word):
#     print( worls)


#! convert enumerate into list or tuple

# fruits = ['apple', 'banana', 'paiapple']

# print(list(enumerate(fruits)))



#!  Real-life use case (Interview friendly)

fruits = ['apple', 'paiapple', 'banana']

for i, val in enumerate(fruits):
    if val == 'apple':
        print("Banana found at index:", i)
    else:
        print(f"{val} is not the name we are looking for")

#! basic metrix method 

# matrix = [
#     [1, 2],
#     [3, 4]
# ]

# for row in matrix:
#     for item in row:
#         print(item)


#! nested Loop with enumerate 

# matrix = [[1,5], [4,8]]
# for i, row in enumerate(matrix):
#     for j, val in enumerate(row):
#         print(f"matrix[{i}][{j}] = {val}")



# matrix = [[1,2], [3,4]]
# for i, row in enumerate(matrix):
#     for j, val in enumerate(row):
#         print(f"matrix[{i}][{j}] = {val}")

