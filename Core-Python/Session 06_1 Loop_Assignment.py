# Name: Arijit Roy Chowdhury
# Email: rc.arijit@gmail.com

######################################################################################################################################
# Q. W. A P. which takes one number from 0 to 9 from the user and prints
# it in the word. And if the word is not from 0 to 9 then
# it should print that number is outside of the range and program should
# exit.
# For exapmple:-
# input = 1
# output = one
######################################################################################################################################

num = int(input("ENter a number between 0 - 9: "))
word = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
flag = 0
for i in range(10):
    if i == num:
        print("The number entered by you is: ", word[i])
        flag = 1
if flag == 0:
    print("Number entered by you is outside the given range")
    
######################################################################################################################################
# Q. W. A P. to implement calculator but the operation to be done and two
# numbers will be taken as input from user:-
# Operation console should show below:-
# Please select any one operation from below:-
# * To add enter 1
# * to subtract enter 2
# * To multiply enter 3
# * To divide enter 4
# * To divide and find quotient enter 5
# * To divide and find remainder enter 6
# * To divide and find num1 to the power of num2 enter 7
# * To Come out of the program enter 8
######################################################################################################################################

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("""\nPlease select any one operation from below:-\n
* To add enter 1\n
* to subtract enter 2\n
* To multiply enter 3\n
* To divide enter 4\n
* To divide and find quotient enter 5\n
* To divide and find remainder enter 6\n
* To divide and find num1 to the power of num2 enter 7\n
* To Come out of the program enter 8\n""")

choice = int(input("Enter Choice: "))

if choice == 1:
    print("Sum is: ", num1+num2)

elif choice == 2:
    print("Difference is: ", num1-num2)
    
elif choice == 3:
    print("Product is: ", num1*num2)
    
elif choice == 4:
    print("Division Result is: ", num1/num2)
    
elif choice == 5:
    print("Quotient on Division is: ", num1//num2)
    
elif choice == 6:
    print("Remainder on Division is: ", num1%num2)
    
elif choice == 7:
    print("num1 to the power of num2 is: ", num1**num2)
    
elif choice == 8:
    exit()
    
else:
    print("Invalid Choice")


######################################################################################################################################
# Q. W A P to check whether a year entered by user is an leap year or not?
# Check with below input:-
# leap year:- 2012, 1968, 2004, 1200, 1600,2400
# Non-lear year:- 1971, 2006, 1700,1800,1900
######################################################################################################################################

yr = int(input("Enter a Year: "))

if yr%4 == 0:
    
    if yr%100 != 0 and yr%400 != 0:
        print("It is a Leap Year")
        
    elif yr%100 == 0:        
        
        if yr%400 == 0:
            print("It is a Leap Year")
            
        else:
            print("It is not a Leap Year")
        
else:
    print("It is not a Leap Year")
    

######################################################################################################################################
# Q. W A P which takes one number from the user and checks whether it is
# an even or odd number?, If it even then prints number is
# even number else prints that number is odd number.
######################################################################################################################################

num = int(input("Enter a number: "))

if num%2 == 0:
    print("Number is Even")
    
else:
    print("Number is Odd")


######################################################################################################################################
# Q. W A P which takes two numbers from the user and prints below output:-
# 1. num1 is greater than num2 if num1 is greater than num2
# 2. num1 is smaller than num2 if num1 is smaller than num2
# 3. num1 is equal to num2 if num1 and num2 are equal
# Note:- 1. Do this problem using if - else
# 2. Do this using ternary operator
######################################################################################################################################

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if num1>num2:
    print("num1 is greater than num2")
    
elif num1<num2:
    print("num1 is smaller than num2")
    
else:
    print("num1 is equal to num2")
    

print ("num1 is equal to num2" if num1 == num2 else "num1 is greater than num2" if num1 > num2 else "num1 is smaller than num2")

######################################################################################################################################
# Q. W A P which takes three numbers from the user and prints below
# output:-
# 1. num1 is greater than num2 and num3 if num1 is greater than num2
# and num3
# 2. num2 is greater than num1 and num3 if num2 is greater than num1
# and num3

# 3. num3 is greater than num1 and num2 if num3 is greater than num1
# and num2
# Note:- 1. Do this problem using if - elif - else
# 2. Do this using ternary operator
# a = a if a>b else b
######################################################################################################################################

n1 = float(input("Enter First Number: "))
n2 = float(input("Enter Second Number: "))
n3 = float(input("Enter Third Number: "))

if n1>n2 and n1>n3:
    print("num1 is greater than num2 and num3")
    
elif n2>n1 and n2>n3:
    print("num2 is greater than num1 and num3")
    
elif n3>n1 and n3>n2:
    print("num3 is greater than num1 and num2")
    
else:
    print("At lease 2 or more numbers are equal")

print("num1 is greater than num2 and num3" if (n1>n2 and n2>n3) else "num2 is greater than num1 and num3" if (n2>n1 and n2>n3) 
      else "num3 is greater than num1 and num2" if (n3>n1 and n3>n2) else "At lease 2 or more numbers are equal")


######################################################################################################################################
# Q. Write a Python program to find the length of the my_str using loop:-
# Input:- 'Write a Python program to find the length of the my_str'
# Output:- 55
######################################################################################################################################

my_str = 'Write a Python program to find the length of the my_str'
c = 0
for i in my_str:
    c = c + 1
print(c)

######################################################################################################################################
# Q. Write a Python program to find the total number of times letter 'p'
# is appeared in the below string using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.\n'
# Output:- 9
######################################################################################################################################

my_str = 'peter piper picked a peck of pickled peppers.\n'
c = 0
for i in my_str:
    if i == 'p':
        c = c + 1
print(c)

######################################################################################################################################
# Q. Write a Python Program, to print all the indexes of all occurences of
# letter 'p' appeared in the string using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:-
# 0
# 6
# 8
# 12
# 21
# 29
# 37
# 39
# 40
######################################################################################################################################

my_str = 'peter piper picked a peck of pickled peppers.'
c = 0
for i in my_str:
    if i == 'p':
        print(c)
    c = c + 1

######################################################################################################################################
# Q. Write a python program to find below output using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers']
######################################################################################################################################

my_str = 'peter piper picked a peck of pickled peppers.'
temp = ''
new_str = []
for i in my_str:
    if i.isalnum() is True:
        temp = temp + i
        
    else:
        new_str.append(temp)
        temp = ''
     
print(new_str)

######################################################################################################################################
# Q. Write a python program to find below output using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- 'peppers pickled of peck a picked piper peter'
######################################################################################################################################

my_str = 'peter piper picked a peck of pickled peppers.'
temp = ''
new_str = []
for i in my_str:
    if i.isalnum() is True:
        temp = temp + i
        
    else:
        new_str.append(temp)
        temp = ''

# Method 1: Using join:      
print(' '.join(new_str[::-1]))

# Method 2: Using Loop:
new_str2 = ''
for i in range(len(new_str)-1, -1, -1):    
    new_str2 = new_str2 + (new_str[i]) + ' '
    
print(new_str2)
    
######################################################################################################################################
# Q. Write a python program to find below output using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- '.sreppep delkcip fo kcep a dekcip repip retep'
######################################################################################################################################

my_str = 'peter piper picked a peck of pickled peppers.'
my_str = my_str.rjust(len(my_str) + 1)
temp = ''
new_str = []

for i in range(len(my_str)-1, -1, -1):
   
    if my_str[i].isspace() is False:
        temp = temp + my_str[i]
        
    else:
        new_str.append(temp)
        temp = ''
        
print(' '.join(new_str))


######################################################################################################################################
# Q. Write a python program to find below output using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- 'retep repip dekcip a kcep fo delkcip sreppep'
######################################################################################################################################

my_str = 'peter piper picked a peck of pickled peppers.'
temp = ''
new_str = []
for i in my_str:
    if i.isalnum() is True:
        temp = temp + i
        
    else:
        new_str.append(temp)
        temp = ''

c = 0 
temp = ''    
for word in new_str:
    print(word)
    print(word[0])
    
    for i in range(len(word)-1, -1, -1):
        temp = temp + word[i]        
    new_str[c] = temp
    temp = ''
    c = c + 1
    
print(' '.join(new_str))
        

######################################################################################################################################
# Q. Write a python program to find below output using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- 'Peter Piper Picked A Peck Of Pickled Peppers'
######################################################################################################################################

my_str = 'peter piper picked a peck of pickled peppers.'
my_str = my_str.rjust(len(my_str) + 1)
new_str = ''

for i in range(len(my_str)):
    if my_str[i-1].isspace() is True:      
        new_str = new_str + my_str[i].upper()
        
    elif my_str[i].isalnum() is True or my_str[i].isspace() is True:
        new_str = new_str + my_str[i]
        
print(new_str.strip())
    
######################################################################################################################################
# Q. Write a python program to find below output using loop:-
# Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.'
# Output:- 'Peter piper picked a peck of pickled peppers'
######################################################################################################################################    

my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
new_str = ''

for i in range(len(my_str)):
    if my_str[i-1].isspace() is True:      
        new_str = new_str + my_str[i].lower()
        
    elif my_str[i].isalnum() is True or my_str[i].isspace() is True:
        new_str = new_str + my_str[i]
        
print(new_str)


######################################################################################################################################
# Q. Write a python program to implement index method using loop. If
# sub_str is found in my_str then it will print the index
# of first occurrence of first character of matching string in my_str:-
# Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.',
# sub_str = 'Pickl'
# Output:- 29
######################################################################################################################################  

my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Pickl'
flag = 0
for i in range(len(my_str)):
    if my_str[i] == sub_str[0]:
        for j in range(len(sub_str)):
            if my_str[i+j] == sub_str[j]:                
                continue
            else:
                flag = 1
                break
            
        if flag == 0:
            print(i)
            break
        
    flag = 0
            

######################################################################################################################################
# Q. Write a python program to implement replace method using loop. If
# sub_str is found in my_str then it will replace the first
# occurrence of sub_str with new_str else it will will print sub_str not
# found:-
# Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.',
# sub_str = 'Peck', new_str = 'Pack'
# Output:- 'Peter Piper Picked A Pack Of Pickled Peppers.'
######################################################################################################################################  

my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'
new_str = 'Pack'
output_str = ''
index = 0
flag = 0
i = 0
while i <= (len(my_str)-1):
    if my_str[i] == sub_str[0]:
        for j in range(len(sub_str)):
            if my_str[i+j] == sub_str[j]:                
                continue
            else:
                flag = 1
                output_str = output_str + my_str[i]
                break
            
        if flag == 0:
            index = i
            for k in range(i, i+len(sub_str)):
                output_str = output_str + new_str[k-i-(len(sub_str))]
            i = i+3
    else:
        output_str = output_str + my_str[i]
        
    flag = 0
    i = i+1

print(output_str)

######################################################################################################################################
# Q. Write a python program to find below output (implements rjust and
# ljust) using loop:-
# Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str =
# 'Peck',
# Output:- '*********************Peck********************'
######################################################################################################################################  


my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'
output_str = ''
index = 0
flag = 0
i = 0
while i <= (len(my_str)-1):
    if my_str[i] == sub_str[0]:
        for j in range(len(sub_str)):
            if my_str[i+j] == sub_str[j]:                
                continue
            else:
                flag = 1
                output_str = output_str + '*'
                break
            
        if flag == 0:
            index = i
            for k in range(i, i+len(sub_str)):
                output_str = output_str + sub_str[k-i-(len(sub_str))]
            i = i+3
    else:
        output_str = output_str + '*'
        
    flag = 0
    i = i+1

print(output_str)

######################################################################################################################################
# Q. Write a python program to find below output using loop:-
# Input:- 'This is Python class', sep = ' is',
# Output:- ['This', 'is', 'Python class']
######################################################################################################################################  

my_str = 'This is Python class'
my_str = my_str.ljust(len(my_str) + 1)
sep = ' is'
temp = ''
new_str = []
for i in my_str:
    if i.isalnum() is True:
        temp = temp + i        
    else:
        new_str.append(temp)
        temp = ''
print(new_str)     
output_str = []
c = 0
for word in new_str:
    if word == sep.strip():        
        for j in range(c+1, len(new_str)):
            temp = temp + ' '+ new_str[j]
            temp = temp.strip()
        output_str.append(sep.strip())
        output_str.append(temp)
        break
    else:
        output_str.append(word)
    c = c + 1    
print(output_str)



















