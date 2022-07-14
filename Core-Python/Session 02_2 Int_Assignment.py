# Name: Arijit Roy Chowdhury
# Email: rc.arijit@gmail.com


################################################################################################################################
# Declare an int value and store it in a variable. Check the type and print the id of the same.
################################################################################################################################

a = 10
print("Variable Type: ", type(a))
print("Variable ID: ", id(a))

################################################################################################################################
# Take one int value between 0 - 256. Assign it to two different variables. Check the id of both the variables. It should come the same. Check why?
################################################################################################################################

a = 20
b = 20
print("ID of First Variable: ", id(a))
print("ID of Second Variable: ", id(b))

################################################################################################################################
# Take one int value either less than -5 or greater than 256. Assign it to two different variables. Check the id of both the variables. 
# It should come different.Check why?
################################################################################################################################

a = -10
b = -10
print("ID of First Variable: ", id(a))
print("ID of Second Variable: ", id(b))
# Reason for different ID's: When we assign a name to an integer between -5 and 256 inclusively, 
# Python assigns predetermined memory locations that contain that integer to the name. 
# Outside this range, Python seems to create a new memory location and fill it with the desired number, before pointing the name to that memory location.


################################################################################################################################
# Arithmetic Operations on integers
# Take two different integer values.
# Store them in two different variables.
# Do below operations on them:-
#      Find sum of both numbers
#      Find difference between them
#      Find the product of both numbers.
#      Find value after dividing first num with second number
#      Find the remainder after dividing first number with second number
#      Find the quotient after dividing first number with second number
#      Find the result of the first num to the power of the second number.
################################################################################################################################

a = 50
b = 12
print("Sum of ", a, " And ", b, " Is: ", a+b)
print("Difference between ", a, " And ", b, " Is: ", a-b)
print("Product of ", a, " And ", b, " Is: ", a*b)
print("Divide ", a, " by ", b, " , Result is: ", a/b)
print("Remainder on Dividing ", a, " by ", b, " : ", a%b)
print("Quotient on Dividing ", a, " by ", b, " : ", a//b)
print("Result of ", a, " raised to the power ", b, " : ", a**b)

################################################################################################################################
# Comparison Operators on integers
# Take two different integer values.
# Store them in two different variables.
# Do below operations on them:-
#      Compare se two numbers with below operator:-
#      Greater than, '>'
#      Smaller than, '<'
#      Greater than or equal to, '>='
#      Less than or equal to, '<='
# Observe their output(return type should be boolean)
################################################################################################################################

a = 200
b = -50
print(a, " Greater Than ", b, " Is ", a>b)
print(a, " Less Than ", b, " Is ", a<b)
print(a, " Greater Than or Equal To ", b, " Is ", a>=b)
print(a, " Is Less Than or Equal To ", b, " Is ", a<=b)

################################################################################################################################
# Equality Operator
# Take two different integer values.
# Store them in two different variables.
# Equate them using equality operators (==, !=)
# Observe the output(return type should be boolean)
################################################################################################################################

a = 125
b = -200
print(a, " Equal To ", b, " Is ", a==b)
print(a, " Not Equal To ", b, " Is ", a!=b)

################################################################################################################################
# Logical operators
# Observe the output of below code
################################################################################################################################

print(10 and 20)
#----------------------------------------->Output is 20
print(0 and 20)
#----------------------------------------->Output is 0
print(20 and 0)
#----------------------------------------->Output is 0
print(0 and 0)
#----------------------------------------->Output is 0
print(10 or 20)
#----------------------------------------->Output is 10
print(0 or 20)
#----------------------------------------->Output is 20
print(20 or 0)
#----------------------------------------->Output is 20
print(0 or 0)
#----------------------------------------->Output is 0
print(not 10)
#----------------------------------------->Output is False
print(not 0)
#----------------------------------------->Output is True

################################################################################################################################
# Bitwise Operators
# Do below operations on the values provided below:-
################################################################################################################################

print(10 & 20)
print(10 | 20)
print(10 ^ 20)
print(~10)
print(10 << 2)
print(10 >> 2)

################################################################################################################################
# What is the output of expression inside print statement. Cross check
# before running the program.
################################################################################################################################

a = 10
b = 10
print(a is b)                   #True
print(a is not b)               #False
a = 1000
b = 1000
print(a is b)                   #False as a and b are greater than 256 and their ID's are different
print(a is not b)               #True as a and b are greater than 256 and their ID's are different

################################################################################################################################
# What is the output of expression inside print statement. Cross check before running the program.
################################################################################################################################

print(10+(10*32)//2**5&20+(~(-10))<<2)

################################################################################################################################
# Membership operation in, not in are two membership operators and it returns boolean value
################################################################################################################################

print('2' in 'Python2.7.8')
print(10 in [10,10.20,10+20j,'Python'])
print(10 in (10,10.20,10+20j,'Python'))
print(2 in {1,2,3})
print(3 in {1:100, 2:200, 3:300})
print(10 in range(20))

################################################################################################################################
# An integer can be represented in binary, octal or hexadecimal form.
# Declare one binary, one octal and one hexadecimal value and store them
# in three different variables.
# Convert 9876 to its binary, octal and hexadecimal equivalent and print
# their corresponding value.
################################################################################################################################

a = 0b101100110
b = 0o10234567
c = 0x9104af
print("Equivalent values of Binary, Octal and Hexadecimal as Integers: ", a, b, c)

d = 9876
db = bin(d)
print("Binary equivalent of ", d, " Is: ", db)
do = oct(eval(db))
print("Binary equivalent of ", d, " Is: ", do)
dh = hex(eval(do))
print("Binary equivalent of ", d, " Is: ", dh)

################################################################################################################################
# What will be the output of following:-
################################################################################################################################

a = 0b1010000
print(a)
b = 0o7436
print(b)
c = 0xfade
print(c)
print(bin(80))
print(oct(3870))
print(hex(64222))
print(bin(0b1010000))
print(bin(0xfade))
print(oct(0xfade))
print(oct(0o7436))
print(hex(0b1010000))
print(hex(0xfade))



























