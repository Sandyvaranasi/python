print("Hello world!")
import hashlib
print(17*12)
print("Twinkle twinkle little star.\n How I wonder what you are.\n Up above the world so high.\n Like a diamond in the sky!")# \n newline charactor
# Single line comment
print("comments can be written after a line") # Like this.
'''
This is a process of writing 
Multiline comments in python
'''

print("We are learning about \n \"escape sequence charactors\"", 4, 7, 23, sep="-", end="last\n")
print('Done')

'''
Escape sequence charactors
\n for line break.
\"  \" for double quotes inside string.
sep="anything" to join multiple elements of print functions using anything. (optional)
end="anything" to end print statement with anything. (optional)
'''

# Variables and datatypes
a = 12
b = "Hello"
c = True
d = None
e = 1.1
f = complex(8, 2)
g = [1,2,"hello", True, None, [5,6]]
h = (1,2,"hello", True, None, [5,6], (7,"good"))
i = {"name":"sandeep","number":27,"able":True}
print(a, b, c, d, e, f, g, h, i)
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i),)

# operators 
print("add",15+6, "sub",15-6, "mul",15*6, "div",15/6, "floor div",15//6, "modulo",15%6, "exp",15**6)

# calculator
a = 15
b = 6
print("The value of",a,"+",b,"is",a+b)
print("The value of",a,"-",b,"is",a-b)
print("The value of",a,"*",b,"is",a*b)
print("The value of",a,"/",b,"is",a/b)

# TYPECASTING (converting one datatype to other)
'''
Explicit conversion (done by programmer using functions like int(), str(), float(), etc)
Implicit conversion (donr br progrmm itself)
'''
a = "1"
b = 2
c = 0
print(type(a), type(b), type(c))
print(type(int(a)), type(str(b)), type(bool(c)))
print(int(a), str(b), bool(c))

# Taking input from user
a = input("First number : " )
b = input("Second number : " )

print(a+b)
print(float(a)+float(b))

#calculator again
num1 = float(input("Enter first number : " ))
num2 = float(input("Enter second number : " ))

print("The sum of", num1,"and", num2, "is", num1+num2)
print("The difference of", num1,"and", num2, "is", num1-num2)
print("The product of", num1,"and", num2, "is", num1*num2)
print("The quotient of", num1,"and", num2, "is", num1/num2)