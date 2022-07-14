

######################################################################################################################################
#Write a Python program to find the sum of all elements in a list using loop.
#Input:- [10,20,30,40]
#Output:- 100
######################################################################################################################################

lst = eval(input("Enter a List: "))
print(lst)
s = 0
for item in lst:
    s = s + item
print("Sum is: ", s)
    
######################################################################################################################################
#Write a Python program to find the multiplication of all elements in a list using loop.
#Input:- [10,20,30,40]
#Output:- 240000
######################################################################################################################################

lst = eval(input("Enter a List: "))
print(lst)
m = 1
for item in lst:
    m = m * item
print("Product is: ", m)

######################################################################################################################################
#Write a Python program to find the largest number from a list using loop.
#Input:- [10,100,2321, 1,200,2]
#Output:- 2321
######################################################################################################################################

lst = eval(input("Enter a List: "))
print(lst)
m = lst[0]
for item in lst:
    if item > m:
        m = item
print("Largest Number is: ", m)

######################################################################################################################################
#Write a Python program to find the smallest number from a list using loop.
#Input:- [10,100,2321, 1,200,2]
#Output:- 1
######################################################################################################################################

lst = eval(input("Enter a List: "))
print(lst)
m = lst[0]
for item in lst:
    if item < m:
        m = item
print("Smallest Number is: ", m)

######################################################################################################################################
#Write a Python program to count the number of strings having length more than 2 and are palindrome in a list using loop.
#Input:- ['ab', 'abc', 'aba', 'xyz', '1991']
#Output:- 2
######################################################################################################################################

lst = eval(input("Enter a List: "))
print(lst)
n = 0
for item in lst:
    flag = 0
    if len(item) > 2:
        for i in range(len(item)):
            if item[i] == item[len(item) -1 - i]:
                continue
            else:
                flag = 1
                break
        if flag == 0:
            n = n + 1
print(n)
            
######################################################################################################################################
#Write a Python program to sort a list in ascending order using loop.
#Input:- [100,10,1,298,65,483,49876,2,80,9,9213]
#Output:- [1,2,9,10,65,80,100,298,483,9213,49876]
######################################################################################################################################

lst = eval(input("Enter a List: "))
print(lst)
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] < lst[j]:
            lst[i] = lst[i] + lst[j]
            lst[j] = lst[i] - lst[j]
            lst[i] = lst[i] - lst[j]
print(lst)

######################################################################################################################################
#Write a Python program to get a sorted list in increasing order of last element in each tuple in a given list using loop.
#Input:- [(5,4),(9,1),(2,3),(5,9),(7,6),(5,5)]
#output:- [(9,1),(2,3),(5,4),(5,5),(7,6),(5,9)]
######################################################################################################################################

lst = eval(input("Enter a List: "))
print(lst)
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i][1] < lst[j][1]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp            
print(lst)

######################################################################################################################################
#Write a Python program to remove fuplicate element from a list using loop.
#Input:- [10,1,11,1,29,876,768,10,11,1,92,29,876]
#Output:- [10,1,11,29,876,768,92]
######################################################################################################################################

lst = eval(input("Enter a List: "))
print(lst)
new_lst = []

for item in lst:
    if item not in new_lst:
        new_lst.append(item)
print(new_lst)

######################################################################################################################################
#Write a Python program to check a list is empty or not?
#Input:- []
#Output:- List is empty
#Input:- [10,20,30]
#Output:- List is not empty
######################################################################################################################################
        
lst = eval(input("Enter a List: "))
print(lst)
c = 0
for item in lst:
    c = c + 1
if c == 0:
    print("List is Empty")
else:
    print("List is Not Empty")
    

######################################################################################################################################
#Write a Python program to copy a list using loop.
#inp_lst = [10,10.20,10+20j, 'Python', [10,20], (10,20)]
#out_lst = [10,10.20,10+20j, 'Python', [10,20], (10,20)]
######################################################################################################################################

inp_lst = eval(input("Enter a List: "))
print("Input List: ", inp_lst)
op_lst = []
for item in inp_lst:
    op_lst.append(item)
print("Output List: ", op_lst)


######################################################################################################################################
#Write a Python program to find the list of words that are longer than or equal to 4 from a given string.
#Input:- 'How much wood would a woodchuck chuck if a woodchuck could chuck wood'
#Output:- ['much', 'wood', 'would', 'woodchuck', 'chuck', 'could']
#Note:- Duplicate should be avoided.
######################################################################################################################################

string = str(input("Enter a String: "))
print("Input String: ", string)
no_of_words = 1
for character in string:
    if character.isspace() is True:
        no_of_words = no_of_words + 1
lst = string.split(" ", no_of_words-1)
op_lst = []
for item in lst:
    if len(item) >= 4:
        if item not in op_lst:
            op_lst.append(item)
print("Output List: ", op_lst)
        
######################################################################################################################################
#Write a Python program which takes two list as input and returns True if they have at least 3 common elements.
#inp_lst1 = [10,20,'Python', 10.20, 10+20j, [10,20,30], (10,20,30)]
#inp_lst2 = [(10,20,30),1,20+3j,100.2, 10+20j, [10,20,30],'Python']
#Output:- True
######################################################################################################################################

lst1 = eval(input("Enter First List: "))
lst2 = eval(input("Enter Second List: "))
c = 0
for item1 in lst1:
    for item2 in lst2:
        if item1 == item2:
            c = c + 1
            break
if c >= 3:
    print("True")
    print("Number of Common elements found: ", c)
else:
    print("False")
            
            
######################################################################################################################################
#Write a Python program to create a 4X4 2D matrix with below elements using loop and list comprehension both.
#Output:- [[0,0,0,0],[0,1,2,3],[0,2,4,6],[0,3,6,9]]
######################################################################################################################################        

lst = [[0]*4, [a for a in range(0, 4, 1)], [b for b in range(0, 8, 2)], [c for c in range(0, 12, 3)]]
print("Output List: ", lst)

######################################################################################################################################
#Write a Python program to create a 3X4X6 3D matrix wiith below elements using loop
#Output:- 
# [
#     [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
#     [[0,0,0,0,0,0],[1,1,1,1,1,1],[2,2,2,2,2,2],[3,3,3,3,3,3]],
#     [[0,0,0,0,0,0],[2,2,2,2,2,2],[4,4,4,4,4,4],[6,6,6,6,6,6]]
# ]
######################################################################################################################################   

lst = []
for i in range(3):
    lst.append([])    
    for j in range(4):
        lst[i].append([])     
        for k in range(6):           
            lst[i][j].append(0)

for i in range(3):
    lst[i][0][0] = 0   
    for j in range(4):        
        for k in range(6):            
            lst[1][j][k] = j
            lst[2][j][k] = j*2        
print(lst)   
        
######################################################################################################################################
#Write a Python program which takes a list of numbers as input and prints a new list after removing even numbers from it.
#Input:- [10,21,22,98,87,45,33,1,2,100]
#Output:- [21,87,45,33,1]
######################################################################################################################################         

lst = eval(input("Enter a List: "))
print(lst)
new_lst = []
for item in lst:
    if item % 2 != 0:
        new_lst.append(item)
print(new_lst)

######################################################################################################################################
#Write a Python program which takes a list from the user and prints it after reshuffling the elements of the list.
#Input:- [10,21,22,98,87,45,33,1,2,100]
#Output:- [1,87,21,10,33,2,100,45,98,22] (It may be any randon list but with same elements)
######################################################################################################################################   

import random
lst = eval(input("Enter a List: "))
random.shuffle(lst)
print("Shuffled List: ", lst)








