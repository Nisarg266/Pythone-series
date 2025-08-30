
#!  Time-based Greeting Program

import time

user = input("enter your name :- ")

timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
# hour = 7-00-00
print(hour)

if hour >= 6 and hour < 12:
    print("Good morning" , user)
elif hour >= 12 and hour < 17:
    print("Good afternoon Sir!", user)
else:
    print("Good night Sir!", user)

