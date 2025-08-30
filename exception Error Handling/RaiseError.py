
#! raise Error in python

def check_age(age):
    if age < 18:
        raise ValueError("your must be 18 or older")
    return "your can vate."
try:
    print(check_age(15))
except ValueError as e:
    print("Error :-",e)
