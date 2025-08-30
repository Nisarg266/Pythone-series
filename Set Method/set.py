
#? All Set Mathodes
#! Set Method

# info = {"nisarg", 5, 8, 94, "Harsh"}
# info2 = {"name": "nisarg", "age": 14}
# info3 = {}
# for value in info:
#     print(value)

# print(type(info))
# print(type(info2))
# print(type(info3))

#! set()  union Method

# s1 = {1,2,3,4,5,6,7,8,9}
# s2 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10}

# print(s1.union(s2))
# # s1.update(s2)
# print(s1)
 


#!  Insersection Method 

# s1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# s2 = {"Tokyo", "Seoul", "kabul", "Madrid"}

# s3 = s1.intersection(s2)
# print(s3)

#! Insersection Update Method

# s1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# s2 = {"Tokyo", "Seoul", "kabul", "Madrid"}

# s1.intersection_update(s2)
# print(s1)
# print(s2)


#! symmetric_difference() method

# s1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# s2 = {"Tokyo", "Seoul", "kabul", "Madrid"}

# s3 = s1.symmetric_difference(s2)
# print(s3)
# # print(s2)



#! Symmetric_difference_update Method

# s1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# s2 = {"Tokyo", "Seoul", "kabul", "Madrid"}

# s1.symmetric_difference_update(s2)
# print(s1)
# print(s2)

#! difference method

# s1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# s2 = {"Tokyo", "Seoul", "kabul", "Madrid"}

# s3 = s1.difference(s2)
# print(s3)
# print(s2)
# print(s1)


#!  issuperset() Method

# s1 = {"Tokyo", "Madrid", "Seoul", "kabul"}
# s2 = {"Tokyo", "Seoul", "kabul", "Madrid"}

# s3 = s1.issuperset(s2)
# print(s3)
# print(s2)


#! issubset Method

# s1 = {"Tokyo", "Madrid", "Seoul", "kabul"}
# s2 = {"Tokyo", "Seoul", "kabul", "Madrid"}

# s3 = s1.issuperset(s2)
# s4 = s3.issubset(s1)
# print(s3)   
# print(s4)


#!  set add method

# s1 = {"Tokyo", "Madrid", "Seoul", "kabul"}

# s1.add("nisarg")
# print(s1)

#! set remove()
  
# s1 = {"Tokyo", "Madrid", "Seoul", "kabul"}

# s1.remove("Tokyo")
# print(s1)  

#! set discard Method

# s1 = {"Tokyo", "Madrid", "Seoul", "kabul"}

# s1.discard("Tokyao")
# print(s1)  

#! set pop() method

# s1 = {"Tokyo", "Madrid", "Seoul", "kabul"}

# s2 = s1.pop()
# print(s1)  
# print(s2)   


#! set del() , (delet Method)


# s1 = {"Tokyo", "Madrid", "Seoul", "kabul"}
# s2 = {"Tokyo", "Madrid", "Seoul", "kabul"}
# del s2

# print(s2)  
# print(s1)  


#! set clear methed 


# s1 = {"Tokyo", "Madrid", "Seoul", "kabul"}

# s1.clear()
# print(type(s1))  

