
#! Function Argument 
'''  there are three argument in the functuon
    1. Default Argument
    2. Keyword Arument
    3. varible Lenght Arument
    4. required Argumane 
'''

#!  1. Default Argumant 
#? jyare koi argument na  aap vama aave to te default value laile chhe

# def name( Fname , name = "nisarg" , age = 19 ):
#     print("hello" , Fname , name ,"age is", age);
    
# name("panchal" , "harshadbhai" , 45)


#! 2. KeyWord Argument 
#? argument ne  key = value  thi aap to te positive par aadhar nathi aetle koi pan kamma aapi sakay

#** example 

# def name(fname , mname, lname ):
#     print(fname , mname,lname)

# name(mname = "niasarg" , fname = "panchal" , lname= "harshadbhai")

#! 3. Required Arguments
#? jo Argument ma jaruri value na aapo to te error batave chhe
#! ❌
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill")

#? ✅
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Ego", "Quill")


#! 4. Variable-length Arguments 
#? જ્યારે exact argument કેટલાં રહેશે એ નક્કી ન હોય ત્યારે વાપરાય છે.

#*  (A) *Arbitrary Arguments

# def name(*name):
#     print("hello", name[0], name[1], name[2])
    
# name("nisarg", "ramesh", "rahul")


#* (B) Keyword Arbitrary Arguments

# def name(**name):
#     print("hello" , name["fname"] , name["mname"] , name["lname"])

# name(fname = "nisarg" , mname ="panchal" , lname = "harshadBhai")

    
#! 5. return Statement 
#? Function કંઈક result પાછું આપે છે calling function (જ્યાંથી બોલાવ્યું) ને.

# def name(fname , mname, lname):
#     return "hello ,"  + fname + " "  + mname + " "  + lname 


# print(name("nisarg" , "panchal" , "harshadBhai"))


'''
        ✅ Summary in Gujarati
Default Arguments	        Argument માટે default value આપવી
Keyword Arguments	        key = value રૂપે arguments આપવાં
Required Arguments	        ચોક્કસ ક્રમ અને સંખ્યા જરૂરી
*Variable Length (args)	    વધારે arguments tuple તરીકે
**Variable Length (kwargs)	key:value arguments dictionary તરીકે
return Statement	        function value પાછું આપે છે
'''
