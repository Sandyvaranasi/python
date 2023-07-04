# String is an array of characters ===> immutable in nature generates a copy with every operation on it like uppercase or lowercase

a = "Hello world!"
print(a)

b = ''' I am
a multilined string
using 3 single quotes
'''
print(b)

c = 'I am a string consisting \" a double quote inside using escape charactor'
print(c)

d = 'I am a string consiting double quote " without esacpe character'
print(d)

for char in a:
    print(char)

# length (len(str))
print(len(a))

# Charactor assessing (box notation [])
print(a[0])
print(a[3])

# String slicing

# str[ind1:ind2] including ind1 to ind2-1
print(a[0:4])
print(a[:4])  # [0:4] equal to [:4]

print(a[3:12])
print(a[3:])  # [3:12] equals to [3:]

# negative slicing [neg1:neg2]

print(a[-4:-2])  # will be (a[len(a)-4:len(a)-2])

# String methods
print(a.isupper())  # boolean for upper case
print(a.islower())  # boolean for lower case
print(a.istitle())  # boolena for first letter of each word
print(a.isalnum())  # true for a-z and 0-9
print(a.isalpha())  # true for a-z
print(a.isprintable())  # true for printable string not for escape char like /"
print(a.endswith('!'))  # true if a ends with "!"
print(a.startswith("l"))  # true if a starts with "l"
print(a.isspace())  # true for white spaces
print(a.upper())  # .toUppercase()
print(a.lower())  # .toLowercase()
print(a.capitalize())  # caps first letter of str
print(a.title())  # caps first letter of each word
print(a.swapcase())  # swaps upper to lower case
print(a.rstrip('!'))  # removes all "! from ending"
print(a.replace("Hell", "Heven"))  # replaces all hell with heven
print(a.split(' '))  # convert striung to list seperated by spaces
print(a.center(20))  # shift string 20 - length spaces right
print(a.count("l"))  # gives count of "l" in string
print(a.find('l'))  # gives ibndex of first occurance of "l" give -1 if not found
print(a.index('o')) # same as above but give error in case of not found insted of -1

