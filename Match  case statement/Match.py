
#!  python Match Statment aa ma switch jevu hoy chhe statement jevu hoy chhe 

x = int(input())

match x: 
    case 0:
        print("your num is zero" ,x)
    case 4:
        print("your num is four" , x)
    case _ if x!=90: 
        print("your num is 90 greatrthen")
    case _ if x!=80:
        print("your num is 80 greaterthene ")
    case _ :
        print("your num is not match")
        
        