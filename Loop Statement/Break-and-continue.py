
#! break in python

# for i in range(12): 
#     if(i == 10):
#         print("skip the iteration")
#         continue
#     print("5 X" , i , "=" , 5 * i)
    
    

#! break practic program


# for i in range(1 , 10):
#     if i == 5 :
#         break
#     print(i)
    
#! continue intaretion

# print("continue")

# for i in range(1 , 10):
#     if i % 2 == 0:
#         continue
#     print(i)
        

# for i in range(1 , 10):
#     for j in range(1,10):
#         print(f"i={i} , j ={j}")
        
        

# matrix = [
#     [1 ,2 ,3],
#     [4 ,5 ,6],
#     [7 ,8 ,9]
# ]

# for row in matrix:
#     for val in row:
#         print(val , end=" ")
#     print()

# enumerate: તમે index સાથે element મેળવો
colors = ['red', 'green', 'blue']
for idx, color in enumerate(colors, start=1):
    print(idx, color)

# zip: બે iterable સાથે એકસાથે loop
names = ['A', 'B', 'C']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
