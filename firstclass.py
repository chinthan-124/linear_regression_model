
''' 
DATA TYPES
integer- all numbers including negative nubers
floats- all decimals number
strings- combination of alphabets and numbers including special characters
 
 PYTHON OPERATORS
 Arithmatic operators
 addition
 substraction
 mult
 div
 exponential
 floor division (gives division answer in integer)
 percentage (finds the remainder)
 '''

# x=2
# y=4
# z= x ** y
# print(z)

# f = open("file.txt", "r")
# print(f.readline())
# f.close()
# f=open("first.python","r")
# print(f.readline())

f=open("file.txt","a")
print(f.write("now the file has more content"))
f.close()
f=open("file.txt","r")
print(f.read())