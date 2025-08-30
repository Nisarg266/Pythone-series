
# a = input("enter your name :-")
# print(f"multiplication table of {a} is")

# try:
#     for i in range(11):
#         print(f"{int(a)} X {i} = {int(a) * i}")
    
# except:
#     print("hello kay kar rahe ho ?? sahise dalo")

#! method 1

# try:
#     x = int("2")
# except ValueError:
#     print("Value Error occurred.")
# except TypeError:
#     print("Type Error occurred.")



#! method 2

# try:
#     x = int("hello")
# except ValueError:
#     print("Value Error occurred.")
# except TypeError:
#     print("Type Error occurred.")



#! mehtod 3

# try:
#     x = int(1,2,3,)
# except ValueError:
#     print("Value Error occurred.")
# except TypeError:
#     print("Type Error occurred.")


#! ZeroDivisionError Method 
 
# try:
#     x = 10 / 0
#     print(f"your answer is {x}")
# except ZeroDivisionError:
#     print("cannot divide by Zero")


#! try ,except and elseto three method use 

# try:
#     file = open("data.txt")
# except FileNotFoundError:
#     print("File not found!")
# finally:
#     print("This always runs.")



#! 📚 Common Exception Types in Python:
#*   Exception           Description
#*   ZeroDivisionError   Attempting to divide by zero
#*   ValueError          Providing an invalid value
#*   IndexError          Accessing an invalid index
#*   KeyError            Accessing a non-existent key in a dictionary
#*   TypeError           Performing an operation on incompatible data types
#*   FileNotFoundError   File not found during an operation
#*   ImportError         Failure to import a module


#!  multiple except blocks :- 

# try:
#     x = int(1,2,3)
# except ValueError:
#     print("value Error occurret.")
# except TypeError:
#     print("Type error Occurret.")


#! Hendling All Exception (Not recommendent but usefull in testing) 

# try:
#     x = 10 / 0
# except Exception as e:
#     print("Error occurred:", e)


#? age programe

# def check_age(age):
#     if age < 18:
#         raise ValueError("your must be 18 or older")
#     return "your can vate."
# try:
#     print(check_age(15))
# except ValueError as e:
#     print("Error :-",e)



#! finally method to error 
def func1():
    try:
        l = [1,2,3,4,5]
        i = int(input("enter your value :-"))
        print(l[i])
        return 1
    except:
        print("some error occurred")
        return 0
    finally:
        print("your code is succesfully !")
    # print("your code is succesfully !")

func1()