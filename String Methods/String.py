# String Methods in Python - Examples and Notes

#! string Lenght Method 

# str = "Hello  my name is nisarg"
# print(len(str))    

#! string 

#! 1 capitalize ()

# text = "hello world"
# print(text.capitalize())


#! 2 casefold()

# text = "NISARG PaNcHaL"
# print(text.casefold())

#! 3 center(width , fillchar)

# text = "hello world"
# print(text.center(30 , "*"))

#! 4 count(substring)

# text = "hello world"
# print(text.count("l"))


#! 5 encode()

# text = "hello world"
# print(text.encode())

#! 6 endswith(suffix)

# text = "hello world "
# print(text.endswith("world"))

#! 7 expandtabs(tabsize)

# text = "a\tb\tc\td"
# print(text.expandtabs(10))
# print(len(text))

# txt = "a\tb\tc"
# print(txt.expandtabs(4))

#! 8 find(substring)

# text = "hello world"
# print(text.find("w"))


#! 9 format()

# name = "nisarg"
# age = 18
# print("my name is {n} my age is {a}".format(n=name,a=age))
# print(f"m y name is {name} my age is {age}")


#! 10 format_map()

# data = {
#     'name':'Nisarg',
#     'age': '18'
#     }
# print("my name is {name} is age {age}".format_map(data))


#! 11 titel()

# text = "hello world"
# print(text.title())

#! 12 swapcase()

# text = "nisarg panchal HARSHAD"
# print(text.swapcase())

#! 13 zfill(width)

# text = "42"
# print(text.zfill(8))

#! ********* Serching methods ***************

#!  15 isalnum() Method 

# text = "user123"
# print(text.isalnum())

#! 16 isalpha() 

# text = "nisarg"
# print(text.isalpha())
# ! 17  isdigit()

# print("123".isdigit())  # True
# print("12a".isdigit())  # False


#! 18 isdecimal()

# print("123".isdecimal())   # True
# print("²".isdecimal())     # False


#! 4. isdecimal()
# 👉 Checks: માત્ર decimal numbers (no fractions/superscript).
# print("123".isdecimal())   # True
# print("²".isdecimal())     # False
# 📌 Use: અખંડાક રૂપમાં check કરવા માટે.


#! 5. isnumeric()
# 👉 Checks: number (including fractions, unicode digits)
# print("123".isnumeric())  # True
# print("½".isnumeric())    # True
# 📌 Use: math symbol ના inputs પણ accept કરવા માટે.


#! 6. islower()
# 👉 Checks: બધાં letters lowercase છે કે નહિ.
# print("hello".islower())  # True
# print("Hello".islower())  # False
# 📌 Use: input consistent format રાખવા.


#! 7. isupper()
# 👉 Checks: બધાં uppercase છે કે નહિ.
# print("HELLO".isupper())  # True
# print("HeLLo".isupper())  # False


#! 8. isspace()
# 👉 Checks: stringમાં ફક્ત space/tab/newline છે કે નહિ.
# print("   ".isspace())    # True
# print(" a ".isspace())    # False
# 📌 Use: ખાલી input detect કરવા.


#! 9. istitle()
# 👉 Checks: દરેક શબ્દની પહેલી અક્ષર capital છે કે નહિ.
# print("Hello World".istitle())  # True
# print("hello world".istitle())  # False
# 📌 Use: titles format check માટે.


#! 10. isascii() (Python 3.7+)
# 👉 Checks: stringમાં બધાં ASCII characters છે કે નહિ. (a–z, A–Z, 0–9, punctuation)
# print("hello123".isascii())   # True
# print("હેલો".isascii())       # False
# 📌 Use: system compatibility માટે.



# 🔹 Part 5: Replace, Split, and Join Methods



#! 11. replace(old, new)
# 👉 Substring ને બદલવા માટે.
text = "hello world"
# print(text.replace("world", "Nisarg"))  # hello Nisarg
# 📌 Use: string modify કરવા.



#! 12. split(sep)
# 👉 String → List. Default space.
text = "a,b,c"
# print(text.split(","))  # ['a', 'b', 'c']
# 📌 Use: CSV, logs, inputs ટુકડા કરવા.



#! 13. rsplit(sep, max)
# 👉 Right side થી split કરે છે.
# text = "a,b,c,d,e,f,g,i,j,k,l,m,o,p,q,r"
# print(text.rsplit(",", 3))  # ['a,b', 'c']
# print(text)
# 📌 Use: last value અલગ કરવાની જરૂર હોય ત્યારે.



# ! 14. splitlines()
# 👉 newline character પર split કરે છે.
text = "line1\nline2"
# print(text.splitlines())  # ['line1', 'line2']
# 📌 Use: files read કરવા.


 
# ! 15. join(iterable)
# 👉 List → String
words = ["my", "name", "is", "Nisarg"]
# print(" ".join(words))  # my name is Nisarg
# 📌 Use: words ને sentenceમાં ફેરવવા.



# 🔹 Part 6: Strip Methods



# ! 16. strip()
# 👉 આગળ અને પાછળ whitespace દૂર કરે છે.
text = "  hello  "
# print(text.strip())  # "hello"



# ! 17. lstrip()
# 👉 Left space દૂર કરે છે.
# print("   hello".lstrip())  # "hello"



# ! 18. rstrip()
# 👉 Right space દૂર કરે છે.
# print("hello   ".rstrip())  # "hello"
# 📌 Use: clean inputs before save.



# 🔹 Part 7: Formatting Methods



# ! 19. format()
# 👉 {} માં variable values મૂકે છે.
name = "Nisarg"
# print("My name is {}".format(name))  # My name is Nisarg



# ! 20. format_map(dict)
# 👉 Dictionary values મુકે છે.
data = {'name': 'Nisarg'}
# print("Hello {name}".format_map(data))  # Hello Nisarg



# ! 21. f-string (Python 3.6+)
# 👉 Easiest way to format
name = "Nisarg"
# print(f"My name is {name}")  # My name is Nisarg
# 📌 Use: Modern Python – fast and clean.



# 🔹 Part 8: Partition Methods



# ! 22. partition(sep)
# 👉 First match પર split: (before, sep, after)
text = "a-b-c"
# print(text.partition("-"))  # ('a', '-', 'b-c')



# ! 23. rpartition(sep)
# 👉 Right sideથી split.
text = "a-b-c"
# print(text.rpartition("-"))  # ('a-b', '-', 'c')



# 🔹 Part 9: Remove Prefix/Suffix (Python 3.9+)



# ! 24. removeprefix(prefix)
# 👉 String માંથી શરૂઆતનું word કાઢે.
text = "unhappy"
# print(text.removeprefix("un"))  # happy



# ! 25. removesuffix(suffix)
# 👉 String ના અંતથી word કાઢે.
text = "file.txt"
# print(text.removesuffix(".txt"))  # file

#! 26 f-string number Methods .2F 

# price = 488.56525
# print(f"this is price {price:.2f}")

