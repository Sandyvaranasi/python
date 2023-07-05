# For Loops used to iterate iterable dtattypes in python

str = "Hello world"
for i in str:
    print(i,end=',')

lis = ["hello", "123", "world"]
for i in lis:
    print(i)
    for j in i:
        print(j,end=",")

# range(start, stop, step) by default start is 0
for k in range(5): # only stop
    print(k)
for k in range(3,10): # start and stop
    print(k)
for k in range(5,20,4): # start stop and range
    print(k)

# Table of 15
for i in range(1,11):
    print(15*i)
for i in range(15,151,15):
    print(i)

# While loops

i = int(input("enter your number " ))
while(i<=50):
    print(i)
    i = int(input("enter your number " ))
print(i, "is greater than 50")

# Reverse counting
i = 100
while(i>=80):
    print(i)
    i = i-1
else:
    print(i, "is less than 80")

# Break and continue
arr = [1,2,3,4,5,6,7,8,9,10]
for i in arr:
    if(i==5):
        print("skipped")
        continue
    elif(i==9):
        print("reached 9")
        break
    else:
        print(i)

# do while loop emulation
i = 1
while True:
    print(i)
    i = i+1
    if(i%100==0):
        print("reached 100")
        break