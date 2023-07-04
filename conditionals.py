# Conditionals in python

# operators (<,>,<=,>=,==,!=)
a = int(input("give number " ))
print(a>18, a<18, a==18, a!=18)

if (a<18):
    print("you cannot drive")
else:
    print("You can drive") 

# Nested
num = int(input("enter the number " ))

if(num>0):
    print(num,"is positive")
elif(num==0):
    print(num,"is neither positive nor negative")
else:
    print(num,"is negative")

import time

timeStamps = time.strftime("%H:%M:%S")
print(timeStamps)

hour = int(time.strftime("%H"))
min = int(time.strftime("%M"))
sec = int(time.strftime("%S"))

if(hour==00):
    if(min==00):
        if(sec==0):
            print("midnight")
        else:
            print("Morning")
    else:
        print("Morning")
elif(hour<12):
    print("morning")
elif(hour==12):
    if(min==0):
        if(sec==0):
            print("Noon")
        else:
            print("After noon")
    else:
        print("After noon")
else:
    print("evening")

# Match Case statement

a = int(input("number here " ))

match a:
    case 10:
        print(a, "is equal to ten")
    case 20:
        print(a,"is equal to twnenty")
    case _ if a<10:
        print(a, "is less than ten")
    case _ if a<20:
        print(a, "is betrween ten and twenty")
    case _:
        print(a,"is greater than twenty")
