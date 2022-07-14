# Name: Arijit Roy Chowdhury
# Email: rc.arijit@gmail.com


############################################################################################################################
# Which are valid/invalid strings
############################################################################################################################

# 1. 'This is Python class'
# valid

# 2. "This is Python class"
# valid

# 3. '''This is Python class'''
# valid

# 4. """This is Python class"""
# valid

# 5. 'This is Python's class'
# invalid

# 6. "Volvo provides "Java", "Python" classes"
# invalid

# 7. "Volvo provides 'Java', 'Python' classes"
# valid

# 8. "This is Python's class"
# valid

# 9. """Volvo provides "Java", "Python" classes"""
# valid

# 10. '''Volvo provides "Java", "Python" classes'''
# valid

# 11. '''Volvo provides
# "Java", "Python" 
# classes'''
# valid

# 12. 'This is
# Python 
# class'
# invalid

############################################################################################################################
# Write the code to get the output mentioned below print statement
# my_str = "Although that way may not be obvious at first unless you're Dutch."
# my_str1 = "Although that way may not be obvious at first unless you're Dutch."

# #output:- The length of my_str is 66

# #output:- id of my_str and my_str1 is same? - True

# #output:- Type of my_str is: str
############################################################################################################################

my_str  = "Although that way may not be obvious at first unless you're Dutch."
my_str1 = "Although that way may not be obvious at first unless you're Dutch."

print("The length of my_str is ", len(my_str))

my_str = my_str1
print("id of my_str and my_str1 is same? -  ", id(my_str) == id(my_str1))

t = str(type(my_str))
print("Type of my_str is: ", t[8:11])

############################################################################################################################
# Indexing
# my_str = "Although 8 that way may not be obvious at first unless you're Dutch"
# Write the code to get the output,instructions are mentioned below print statement. use indexing

# output:- The first character in my_str is: A
# Note:- Use positive indexing

# output:- The first character in my_str is: h
# Note:- Use len() function.

# output:- The character at index 10 in my_str is: ' '
# Note:- Use positive indexing

# output:- The last character in my_str is: h
# Note:- Use negative indexing.

# output:- The last character in my_str is: h
# Note:- Use len() function.

# output:- The character in my_str is: 8
# Note:- Use positive index
############################################################################################################################

my_str = "Although 8 that way may not be obvious at first unless you're Dutch"

print("The first character in my_str is: ", my_str[0])
print("The last character in my_str is: ", my_str[len(my_str)-1])
print("The character at index 10 in my_str is: '", my_str[10], "'")
print("The last character in my_str is: ", my_str[-1])
print("The last character in my_str is: ", my_str[len(my_str)-1])
i = 0
for s in my_str:    
    if s.isnumeric() is True:
        pos = i    
    i = i + 1            
print("The character in my_str is: ", my_str[pos])

############################################################################################################################
# Slicing
# my_str = "Although that way may not be obvious at first unless you're Dutch."

# Write the code to get the output,instructions are mentioned below print statement. use slicing
# output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.Without begin, end and step
# output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.with begin as 0 end using len and without step
# output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.without begin and end but using step
# output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.With begin, end and step
# output:- You have sliced:   .with using begin and end using postive values and step as negative values.
# Slicing command should print empty string.
# output:- You have sliced: Atog htwymyntb biu tfrtuls o'eDth
# output:- You have sliced: Ahgttam tebo  r lsorDc
# output:- You have sliced: .hctuD er'uoy sselnu tsrif ta suoivbo eb ton yam yaw taht hguohtlA. Use only step
# output:- You have sliced: .hctuD er'uoy sselnu tsrif ta suoivbo eb ton yam yaw taht hguohtlA. Use begin end and step.
# output:- You have sliced: .cu ruysen si asovoe o a a athuhl. use only step
# output:- You have sliced: .cu ruysen si asovoe o a a athuhl. use begin, end and step.
# print(my_str[10:17:-1])
# What will be the output?
# output:- You have sliced: yaw ta, Using begin, end and step.
# output:- You have sliced: ess you. Using begin, end and step.
############################################################################################################################
        
my_str = "Although that way may not be obvious at first unless you're Dutch."

print(len(my_str))        
print("You have sliced: ", my_str, "Without begin, end and step")
print("You have sliced: ", my_str[0:len(my_str)+1], "with begin as 0 end using len and without step")
print("You have sliced: ", my_str[::1], "without begin and end but using step")
print("You have sliced: ", my_str[0:len(my_str)+1:1], "With begin, end and step")
print("You have sliced: ", my_str[65:65:-1], ".with using begin and end using postive values and step as negative values")
print("You have sliced: ", my_str[::2])
print("You have sliced: ", my_str[::3])
print("You have sliced: ", my_str[::-1], ". Use only step")
print("You have sliced: ", my_str[-1:-67:-1], ". Use begin end and step.")
print("You have sliced: ", my_str[::-2], ". use only step")
print("You have sliced: ", my_str[-1:-67:-2], ". use begin, end and step.")
print(my_str[10:17:-1])       # Prints empty string as start index is less than end index for negative step
print("You have sliced: ", my_str[-49:-53:-1], my_str[-27:-30:-1], ", Using begin, end and step.")
print("You have sliced: ", my_str[49:56:1], ". Using begin, end and step.")

############################################################################################################################
#Basic operation on string
#Write the code to get the output,instructions are mentioned below.

#Output is: Volvo Python

#Error: TypeError: can only concatenate str (not "int") to str

#Error: TypeError: can only concatenate str (not "float") to str

#Find below Output
#Output is: VolvoVolvoVolvo

#Error: TypeError: can't multiply sequence by non-int of type 'float'

#Error: TypeError: can't multiply sequence by non-int of type 'str'
############################################################################################################################

str1 = 'Volvo'
str2 = 'Python'

print(str1 + " " + str2)
print(str1 + " " + str2 + 3)            #Error: TypeError: can only concatenate str (not "int") to str
print(str1 + " " + str2 + 3.9)          #Error: TypeError: can only concatenate str (not "float") to str
print(str1*3)
print(str1*3.5)                         #Error: TypeError: can't multiply sequence by non-int of type 'float'
print(str1*str2)                        #Error: TypeError: can't multiply sequence by non-int of type 'str'

############################################################################################################################
#Find below Output

#print True by using identity operator between str1 and str2
#print False by using identity operator between str1 and str3
#print False by using identity operator between str4 and str3
#Check if P is available in str1 and print True by using membership operator
#Check if $ is available in str3 and print True by using membership operator
#Check if N is available in str3 and print False by using membership operator
############################################################################################################################

str1 = 'Python'
str2 = 'Python'
str3 = 'Python$'
str4 = 'Python$'

print(str1 == str2)
print(str1 == str3)
print(str4 == str3)
print("P" in str1)
print("$" in str3)
print("N" in str3)

############################################################################################################################
#Complete the below code
#str1 = 'This is Python class'
#write the code to replace 'Python' with 'Java' and you should get below error.
#TypeError: 'str' object does not support item assignment.
############################################################################################################################

str1 = 'This is Python class'
str2 = ""
j = 0
for i in str1:
    str2[j] = i
    j = j + 1
print(str2)   
str1 = str1.split(' ')    
str1[2] = "Java"
str2 = str1[0] + str1[1] + str1[2] + str1[3]
print(str2)

############################################################################################################################
# str1 = 'A'
# str2 = 'A'
#Compare str1 and str2 and print True using comparison operator
#Compare str1 and str2 and print True using equality operator
#Compare str1 and str2 and print False using equality operator
#Compare str1 and str2 and print False using comparison operator
############################################################################################################################

str1 = 'A'
str2 = 'A'

print(str1 >= str2)
print(str1 == str2)
print(str1 != str2)
print(str1 > str2)

############################################################################################################################
# str1 = 'A'
# str2 = 'a'
#Compare str1 and str2 and print True using comparison operator
#Compare str1 and str2 and print True using equality operator
#Compare str1 and str2 and print False using equality operator
#Compare str1 and str2 and print False using comparison operator
############################################################################################################################

str1 = 'A'
str2 = 'a'

print(str1 <= str2)
print(str1 != str2)
print(str1 == str2)
print(str1 >= str2)

############################################################################################################################
# str1 = 'A'
# str2 = '65'
#Compare str1 and str2 using comparison operator and it should give below error.
#Error: TypeError: '>=' not supported between instances of 'str' and 'int'
#Compare str1 and str2 and print True using equality operator
#Compare str1 and str2 and print False using equality operator
############################################################################################################################

str1 = 'A'
str2 = '65'

print(str1 == chr(int(str2)))
print(str1 == str2)
print(str1 >= int(str2))

############################################################################################################################
#Compare str1 and str2 and print True using comparison operator
#Compare str1 and str2 and print True using equality operator
#Compare str1 and str2 and print False using equality operator
#Compare str1 and str2 and print False using comparison operator
############################################################################################################################

str1 = 'Python'
str2 = 'Python'

print(str1 >= str2)
print(str1 == str2)
print(str1 != str2)
print(str1 > str2)

############################################################################################################################
#Compare str1 and str2 and print True using comparison operator
#Compare str1 and str2 and print True using equality operator
#Compare str1 and str2 and print False using equality operator
#Compare str1 and str2 and print False using comparison operator
############################################################################################################################

str1 = 'Python'
str2 = 'python'

print(str1 >= str2.capitalize())
print(str1 == str2.capitalize())
print(str1 == str2)
print(str1 >= str2)

############################################################################################################################
#Apply logical opereators (and, or & not) on above string values and observe the output.
############################################################################################################################

a = 'Python'
b = ''

print(a and b)                    # Blank output as b is null
print(a or b)                     # 'Python' as b is null
print(b and a)                    # Blank output as b is null
print(b or a)                     # 'Python' as b is null
print(not b)                      # True as b is null
print(not a)                      # False as a is not null

############################################################################################################################
#Apply logical opereators (and, or & not) on above string values and observe the output.
############################################################################################################################

a = ''
b = ''

print(a and b)                    # Blank output as a and b are null
print(a or b)                     # Blank output as a and b are null
print(not b)                      # True as b is null
print(not a)                      # True as a is null

############################################################################################################################
#Apply logical opereators (and, or & not) on above string values and observe the output.
############################################################################################################################

a = 'Python'
b = 'Volvo'

print(a and b)                    # Volvo as a is True, hence it outputs the value of b
print(a or b)                     # Python as a is true, hence it outputs the value of a
print(not b)                      # False as b is not null

############################################################################################################################
#Write the code to get the total count of 't' in above string. Use find() and index() method.
#Write the code to get the index of '8' in my_str. Use find() and index() method.
#What will be the output of below code?
    # print(my_str.find('the')) 
    # print(my_str.index('the'))
    # print(my_str.find('t', 9, 15))
    # print(my_str.rfind('u'))
    # print(my_str.rindex('u'))
############################################################################################################################

my_str = "Although 8 that way may not be obvious at first unless you're Dutch"

c = 0
for s in my_str:
    if s.find('t') != -1:
        c = c + 1
print("Number of occurances of 't' using find() method: ", c)

c = 0
for s in my_str:
    try:
        if s.index('t') == 0:
            c = c + 1
    except:
        pass
print("Number of occurances of 't' using index() method: ", c)

print("index of '8' using find() method: ", my_str.find('8'))

print("index of '8' using index() method: ", my_str.index('8'))

print(my_str.find('the'))                       # Output: -1 as 'the' is not present in the input string
try:
    print(my_str.index('the'))
except ValueError as e:
    print(e)                                    # Output: 'substring not found'
print(my_str.find('t', 9, 15))                  # Output: 11
print(my_str.rfind('u'))                        # Output: 63
print(my_str.rindex('u'))                       # Output: 63
        
############################################################################################################################
#W A P which applies strip() method if any string, which will be taken from user, starts and ends with space, or applies 
#rrstrip() method if that string only ends with space or applies lstrip() method if that string only starts with a space.

#For example:-
#input:- '    Python   '
#output:- 'Python'

#input:- '    Python'
#output:- 'Python'

#input:- 'Python   '
#output:- 'Python'
############################################################################################################################

s1 = str(input("Enter a String: "))
print("Input String: '" + s1 + "'")

if s1.startswith(' ') and s1.endswith(' '):
    print("After Strip: '" + s1.strip() + "'")
if s1.startswith(' ') and s1.endswith(' ') is False:
    print("After Left Strip: '" + s1.lstrip() + "'")    
if s1.endswith(' ') and s1.startswith(' ') is False:
    print("After Right Strip: '" + s1.rstrip() + "'")
    

############################################################################################################################
#Write the code to convert all alphabets in my_str into upper case.
#Write the code to convert all alphabets in my_str into lower case.
#Write the code to swap the cases of all alphabets in my_str.(lower to upper and upper to lower)
############################################################################################################################

my_str = "Although 8 that way may not be obvious at first unless you're Dutch"
print("Input String: ", my_str)

print("String in Upper Case: ", my_str.upper())
print("String in Lower Case: ", my_str.lower())
print("String after swapping it's case using swapcase() method: ", my_str.swapcase())

############################################################################################################################
#Write the code which takes one string from user and if it starts with small case letter then convert it to corresponding 
#capital letter otherwise if starts with capital letters then convert first character of every word in that string into capital.
############################################################################################################################

s1 = str(input("Enter a String: "))
print("Input String: '" + s1 + "'")

if s1[0].islower() is True:
    print("String after Capitalizing: ", s1.capitalize())
    
elif s1[0].isupper() is True:
    print("String after converting to title case: ", s1.title())
    
############################################################################################################################
#Take a string from user and check if it is:-
#     1. alphanumeric
#     2. alphabets
#     3. digit
#     4. all letters are in lower case
#     5. all letters are in upper case
#     6. in title case
#     7. a space character
#     8. numeric
#     9. all number elements in string are decimal
############################################################################################################################

s1 = str(input("Enter a String: "))
print("Input String: '" + s1 + "'")

print("All Alphanumeric: ", s1.isalnum())
print("All Alphabetic: ", s1.isalpha())
print("All Digits: ", s1.isdigit())
print("All Lower Case: ", s1.islower())
print("All upper Case: ", s1.isupper())
print("All title Case: ", s1.istitle())
print("At least one Space character: ", any(map(str.isspace, s1)))
print("All Numeric: ", s1.isnumeric())
print("All Decimal: ", s1.isdecimal())
print("At least one Decimal: ", any(map(str.isdigit, s1)))

############################################################################################################################
#W A P which takes a string as an input and prints True if the string is valid identifier else returns False.
#Sample Input:- 'abc', 'abc1', 'ab1c', '1abc', 'abc$', '_abc', 'if'
############################################################################################################################

s1 = str(input("Enter a String: "))
print("Input String: '" + s1 + "'")

print(s1, " is Identifier: ", s1.isidentifier())

############################################################################################################################
#What will be output of below code?
############################################################################################################################

s = chr(65) + chr(97)
print(s.isprintable())             # True

s = chr(27) + chr(97)
print(s.isprintable())             # False

s = '\n'
print(s.isprintable())             # False

s = ''
print(s.isprintable())             # True

############################################################################################################################
#What will be output of below code?
############################################################################################################################

my_string = '  '
print(my_string.isascii())          # True

my_string = 'Studytonight'
print(my_string.isascii())          # True

my_string = 'Study tonight'
print(my_string.isascii())          # True

my_string = 'Studytonight@123'
print(my_string.isascii())          # True

my_string = '°'
print(my_string.isascii())          # False

my_string = 'ö'
print(my_string.isascii())          # False

############################################################################################################################
#What will be output of below code?
############################################################################################################################

firstString = "der Fluß"
secondString = "der Fluss"

if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')

# Output: The strings are equal

############################################################################################################################
#Write the code to get below output
#O/P 1:- python** (using ljust method)

#Write the code to get below output
#O/P 1:- **python (using rjust method)

#Write the code to get below output
#O/P 1:- **python** (using rjust method)
############################################################################################################################

str1 = "python"
print(str1.ljust(8,'*'))
print(str1.rjust(8,'*'))
print(str1.rjust(8,'*').ljust(10, '*'))

############################################################################################################################
#Write a Python program to find the length of the my_str:-
############################################################################################################################

my_str = 'Write a Python program to find the length of the my_str'
print("Length of my_str: ", len(my_str))

############################################################################################################################
#Write a Python program to find the total number of times letter 'p' is appeared in the below string:-
############################################################################################################################

my_str = 'peter piper picked a peck of pickled peppers.'
print("Occurance of 'p': ", my_str.count('p'))

############################################################################################################################
#Write a Python Program, to print all the indexes of all occurences of letter 'p' appeared in the string:-
############################################################################################################################

my_str = 'peter piper picked a peck of pickled peppers.'

for i in range(len(my_str)):
    if my_str[i] == 'p':
        print("# ", i)
        
############################################################################################################################
#Write a python program to find below output:-
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers.']
############################################################################################################################
    
my_str = 'peter piper picked a peck of pickled peppers.'
print(my_str.split(' '))

############################################################################################################################
#Write a python program to find below output:-
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'peppers. pickled of peck a picked piper peter'
############################################################################################################################

my_str = 'peter piper picked a peck of pickled peppers.'
print(' '.join(my_str.split(' ')[::-1]))

############################################################################################################################
#Write a python program to find below output:-
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- '.sreppep delkcip fo kcep a dekcip repip retep'
############################################################################################################################

my_str = 'peter piper picked a peck of pickled peppers.'
my_str = my_str.split(' ')[::-1]
my_str1 = []
for s in my_str:
    my_str1.append(s[::-1])
print(' '.join(my_str1))
    
############################################################################################################################
#Write a python program to find below output:-
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'retep repip dekcip a kcep fo delkcip .sreppep'
############################################################################################################################
    
my_str = 'peter piper picked a peck of pickled peppers.'
my_str = my_str.split(' ')

my_str1 = []
for s in my_str:
    my_str1.append(s[::-1])
print(' '.join(my_str1))

############################################################################################################################
#Write a python program to find below output:-
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'Peter Piper Picked A Peck Of Pickled Peppers.'
############################################################################################################################
    
my_str = 'peter piper picked a peck of pickled peppers.'
print(my_str.title())

############################################################################################################################
#Write a python program to find below output:-
#Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.'
#Output:- 'Peter piper picked a peck of pickled peppers.'
############################################################################################################################

my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
print(my_str.capitalize())

############################################################################################################################
#Write a python program to implement index method. If sub_str is found in my_str then it will print the index
# of first occurrence of first character of matching string in my_str:-
#Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Pickl'
#Output:- 29
############################################################################################################################

my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Pickl'
print(my_str.find(sub_str))

############################################################################################################################
#Write a python program to implement replace method. If sub_str is found in my_str then it will replace the first 
#occurrence of sub_str with new_str else it will will print sub_str not found:-
#Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Peck', new_str = 'Pack'
#Output:- 'Peter Piper Picked A Pack Of Pickled Peppers.'
############################################################################################################################

my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'
new_str = 'Pack'
if sub_str in my_str:
    my_str.replace(sub_str, new_str)
    print("New String after replacing: ", my_str)
else:
    print(sub_str, " Not Found")
    
############################################################################################################################
#Write a python program to find below output (implements rjust and ljust):-
#Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Peck', 
#Output:- '*********************Peck********************'
############################################################################################################################

my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'
l1 = len(my_str)
l2 = len(sub_str)

sub_str = sub_str.ljust(int(round((l1+l2)/2)), '*').rjust(l1, '*')
print(sub_str)







