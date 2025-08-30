
#! List Function

# fruits = ["Apple", "Banana", "Cherry"]

# ? Gujarati explanation:
# ? અહીં square brackets []માં 3 string items છે.
# ? દરેક item comma(,)થી અલગ છે.

# print(fruits)

# * Output: ['Apple', 'Banana', 'Cherry']


#! 2. Indexing

# fruits = ["Apple","mabgo", "Banana", "Cherry"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[-1])


#! 3. Slicing

# nums = [10, 20, 30, 40, 50, 60]
# print(nums[1:4])    # [20, 30, 40]   (index 1 થી 3)
# print(nums[:3])     # [10, 20, 30]   (શરૂઆતથી index 0થી 2)
# print(nums[3:])     # [40, 50, 60]   (index 3થી 끝)
# print(nums[::2])    # [10, 30, 50]   (step size 2)


#! 4. Mutable Nature: add, change, remove


# colors = ["red" , "blue" , "green" , "white" , "black"]

# colors.append("Yellow")        #? ["Red", "Green", "Blue", "Yellow"]
# colors.insert(1, "Orange")     #? index 1 પર Orange add
# colors[2] = "Purple"           #? index 2 ને update
# removed = colors.pop()         #? last item remove કરે છે ('Yellow')
# colors.remove("Purple")         #? value દ્વારા remove
# # colors.clear()                 #?  list ખાલી કરે

# print(colors)


#!  5. utility Methods

# data = [1,2,3,4,5,6,7,8,9,1,2,8,5,]
# # print(data.count(1))
# # print(data.index(9))
# data.sort()
# data.reverse()
# data_copy = data.copy()
# print(data_copy.append(1513))


# print(data)

#!  6. Iteration (Loop)

# fruits = ["apple" , "banana" , "Charry"]
# for fruit in fruits:
#     print(fruit)
# Output:
# Apple
# Banana
# Cherry


#! 7. Nested list (list of list)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# # print(matrix[1][2])

# for row in matrix:
#     for val in row:
#         print(val , end =" ")
#     print()


# num = " "

# # for nums in range(5):
# #     for col in range(nums):
# #         print(col)
# #     print()
    

#!  8. extend() method

# name1 = ["nisarg" , "rahul" ,"chetan" , "ravi"]
# name2 = ["ramesh" , "naitik", "pintu" , "jaivik"]
# print(name1+name2)