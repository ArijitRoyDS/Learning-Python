# Name: Arijit Roy Chowdhury
# Email: rc.arijit@gmail.com


################################################################################################################################
# Declare a boolean value and store it in a variable. Check the type and print the id of the same.
################################################################################################################################

a = 0b10111000111
print(a)
print(type(a))
print(id(a))

################################################################################################################################
# Take one boolean value between 0 - 256. Assign it to two different variables. Check the id of both the variables. It should come the same. Check why?
################################################################################################################################

a = 0b110111
b = 0b110111
print(a)
print(id(a))
print(id(b))

################################################################################################################################
# Arithmetic Operations on boolean data:
# Take two different boolean values. Store them in two different variables.
# Do below operations on them:-
#     Find sum of both values
#     Find difference between them
#     Find the product of both.
#     Find value after dividing first value with second value
#     Find the remainder after dividing first value with second value
#     Find the quotient after dividing first value with second value
#     Find the result of first value to the power of second value.
################################################################################################################################

a = 0b110100
b = 0b100101
print("Sum of ", a, " And ", b, " Is: ", bin(a+b))
print("Difference between ", a, " And ", b, " Is: ", bin(a-b))
print("Product of ", a, " And ", b, " Is: ", bin(a*b))
#print("Divide ", a, " by ", b, " , Result is: ", bin(a/b))                     # Type Error due to float value
print("Remainder on Dividing ", a, " by ", b, " : ", bin(a%b))
print("Quotient on Dividing ", a, " by ", b, " : ", bin(a//b))
print("Result of ", a, " raised to the power ", b, " : ", bin(a**b))

################################################################################################################################
# Comparison Operators on boolean values
# Take two different boolean values.
# Store them in two different variables.
# Do below operations on them:-
#     Compare these two values with below operator:-
#     Greater than, '>'
#     less than, '<'
#     Greater than or equal to, '>='
#     Less than or equal to, '<='
#     Observe their output(return type should be boolean)
################################################################################################################################

a = 0b11101011
b = 0b11001100
print(a, " Greater Than ", b, " Is ", a>b)
print(a, " Less Than ", b, " Is ", a<b)
print(a, " Greater Than or Equal To ", b, " Is ", a>=b)
print(a, " Is Less Than or Equal To ", b, " Is ", a<=b)

################################################################################################################################
# Equality Operator
# Take two different boolean values.
# Store them in two different variables.
# Equate them using equality operators (==, !=)
# Observe the output(return type should be boolean)
################################################################################################################################

a = 0b11110101
b = 0b111101011
print(a, " Equal To ", b, " Is ", a==b)
print(a, " Not Equal To ", b, " Is ", a!=b)

################################################################################################################################
# Logical operators
# Observe the output of below code
# Cross check the output manually
################################################################################################################################

print(True and True)
#----------------------------------------->Output is True
print(False and True)
#----------------------------------------->Output is False
print(True and False)
#----------------------------------------->Output is False
print(False and False)
#----------------------------------------->Output is False
print(True or True)
#----------------------------------------->Output is True
print(False or True)
#----------------------------------------->Output is True
print(True or False)
#----------------------------------------->Output is True
print(False or False)
#----------------------------------------->Output is False
print(not True)
#----------------------------------------->Output is False
print(not False)
#----------------------------------------->Output is True

################################################################################################################################
# Bitwise Operators
# Do below operations on the values provided below:-
################################################################################################################################

print(True & True)
print(True | False)
print(True ^ False)
print(~True)
print(True << 2)
print(True >> 2)

################################################################################################################################
# What is the output of expression inside print statement. Cross check before running the program.
################################################################################################################################

a = True
b = True
print(a is b)                   #True
print(a is not b)               #False
a = False
b = False
print(a is b)                   #True
print(a is not b)               #False

################################################################################################################################
# Membership operation in, not in are two membership operators and it returns boolean value
################################################################################################################################

print(True in [10,10.20,10+20j,'Python', True])
print(False in (10,10.20,10+20j,'Python', False))
print(True in {1,2,3, True})
print(True in {True:100, False:200, True:300})
print(False in {True:100, False:200, True:300})













