
# def welcome():
#     print("Welcome from the second module!")
    
# welcome()

#? if __name__=="__main__" 
#? this method to This method is such that if the output in the first file’s print is the same, then it prints it only once.

# print(__name__)
# if __name__=="__main__":
#     welcome()

#! example 
def total_marks(marks):
    return sum(marks)

def average_marks(marks):
    return sum(marks) / len(marks)

print("marks_utils loaded successfully!")

if __name__ == "__main__":
    # Testing purpose
    print("Testing functions...")
    sample = [80, 90, 70]
    print("Total:", total_marks(sample))     # Output: 240
    print("Average:", average_marks(sample)) # Output: 80.0
