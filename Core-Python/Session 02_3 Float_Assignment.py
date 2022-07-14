# Name: Arijit Roy Chowdhury
# Email: rc.arijit@gmail.com


################################################################################################################################
# Declare a float value and store it in a variable. Check the type and print the id of the same.
################################################################################################################################

a = 10.2030
print("Variable Type: ", type(a))
print("Variable ID: ", id(a))

################################################################################################################################
# Arithmetic Operations on float
# Take two different float values.
# Store them in two different variables.
# Do below operations on them:-
#     Find sum of both numbers
#     Find difference between them
#     Find the product of both numbers.
#     Find value after dividing first num with second number
#     Find the remainder after dividing first number with second number
#     Find the quotient after dividing first number with second number
#     Find the result of the first num to the power of the second number.
################################################################################################################################

a = 65.55
b = 23.22287
print("Sum of ", a, " And ", b, " Is: ", a+b)
print("Difference between ", a, " And ", b, " Is: ", a-b)
print("Product of ", a, " And ", b, " Is: ", a*b)
print("Divide ", a, " by ", b, " , Result is: ", a/b)
print("Remainder on Dividing ", a, " by ", b, " : ", a%b)
print("Quotient on Dividing ", a, " by ", b, " : ", a//b)
print("Result of ", a, " raised to the power ", b, " : ", a**b)

################################################################################################################################
# Comparison Operators on float
# Take two different float values.
# Store them in two different variables.
# Do below operations on them:-
#     Compare these two numbers with below operator:-
#         Greater than, '>'
#         Smaller than, '<'
#         Greater than or equal to, '>='
#         Less than or equal to, '<='
#         Observe their output(return type should be boolean)
################################################################################################################################

a = 12.563
b = -23.258
print(a, " Greater Than ", b, " Is ", a>b)
print(a, " Less Than ", b, " Is ", a<b)
print(a, " Greater Than or Equal To ", b, " Is ", a>=b)
print(a, " Is Less Than or Equal To ", b, " Is ", a<=b)

################################################################################################################################
# Equality Operator
# Take two different float values.
# Store them in two different variables.
# Equate them using equality operators (==, !=)
# Observe the output(return type should be boolean)
################################################################################################################################

a = 45.65
b = 45.65
print(a, " Equal To ", b, " Is ", a==b)
print(a, " Not Equal To ", b, " Is ", a!=b)

################################################################################################################################
# Logical operators
# Observe the output of below code
# Cross check the output manually
################################################################################################################################

print(10.20 and 20.30)              #both are true and second value taken >Output is 20.3
print(0.0 and 20.30)                #First is false so first value taken >Output is 0.0
print(20.30 and 0.0)                #Goes to till second and second value is false so second is taken >Output is 0.0
print(0.0 and 0.0)                  #First is false so first value is taken >Output is 0.0
print(10.20 or 20.30)               #First is True so first value is taken >Output is 10.2
print(0.0 or 20.30)                 #Goes to till second and second is true second value is taken >Output is 20.3
print(20.30 or 0.0)                 #First is True so first value is taken >Output is 20.3
print(0.0 or 0.0)                   #Goes to till second and second is also false and second value is taken >Output is 0.0
print(not 10.20)                    #Not of true is false->Output is False
print(not 0.0)                      #Not of false is True>Output is True

################################################################################################################################
# Logical operators
# Observe the output of below code
# Cross check the output manually

# Why the Id of float values are different when the same value is
# assigned to two different variables
# ex: a = 10.5 b=10.5. but id will be same if I assign the variable
# having float i.e. a=c then both a and c's Id are same
################################################################################################################################

a = 10.20
b - 10.20
print(a is b)                       #True or False? True 10.20<256
print(a is not b)                   #True or False? False

################################################################################################################################
# Membership operation
# in, not in are two membership operators and it returns boolean value
################################################################################################################################

print('2.7' in 'Python2.7.8')                       # True
print(10.20 in [10,10.20,10+20j,'Python'])          # True
print(10.20 in (10,10.20,10+20j,'Python'))          # True
print(20.30 in {1,20.30,30+40j})                    # True
print(2.3 in {1:100, 2.3:200, 30+40j:300})          # True
print(10 in range(20))                              # True








