questions = [
    ["Which language is primarily used for Android app development?", "Python", "Java", "C#", "PHP", "None", 2],

    ["What does HTML stand for?", "HyperText Markup Language", "HighText Machine Language", "Hyperlink and Text Markup Language", "Home Tool Markup Language", "None", 1],

    ["Which company developed the Java programming language?", "Microsoft", "Apple", "Sun Microsystems", "Google", "None", 3],
    
    ["What is the extension of Python files?", ".java", ".py", ".txt", ".cpp", "None", 2],

    ["Which language is used for web development and is known for its frameworks like Django and Flask?", "Python", "Ruby", "JavaScript", "PHP", "None", 1],

    ["Which programming language is known as the backbone of web development?", "Python", "JavaScript", "C++", "Ruby", "None", 2],

    ["Which database is a NoSQL database?", "MySQL", "PostgreSQL", "MongoDB", "SQLite", "None", 3],

    ["Which language is used for iOS app development?", "Swift", "Kotlin", "Java", "C#", "None", 1],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

money = 0

for i in range(0 , len(questions)):
    questionss = questions[i]
    print(f"\n\nQuestion of Rs. {levels[i]}\n")
    print(f"Q. {questionss[0]}\n")
    print(f" a.{questionss[1]}      b.{questionss[2]}\n")
    print(f" c.{questionss[3]}      d.{questionss[4]}\n")
    reply = int(input(" Enter you answer in( 1-4 ) or 0 to quit :- \n" ))
    
    if (reply == 0):
        money = levels[i-1]
        break
    if(reply == questionss[-1]):
        print(f"Correct answer , your won Rs . {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif( i == 14):
            money = 1000000
    else:
        print("wrong answer !")
        break
print(f"  Your tack home money is {money}")
 