# Write a Python function that takes two arguments (a and b) and returns their sum 
def add_nums(a,b):
    sum=a+b
    return sum
print(add_nums(10,20))

# Write a Python function that takes a string as input and returns the string reversed.

def name(word):
    return word[::-1]
print(name("cat"))    

# Write a Python function that takes a list of integers as input and returns the sum of all the integers in the list.
def list_integers(nums):
    sum=0
    for num in nums:
        sum +=num
    return sum
print(list_integers([1,2,3,4,5,6]))  

# Write a Python function that takes a list of integers as input and returns
#  a new list with all the even numbers removed.
def rem_even(num):
    new=[]
    for i in num:
        if i %2!=0:
             new.append(i)
    return new              
print(rem_even([1,2,3,4,5,6,7,8,9]))         
# Write a Python function that takes a list of integers as input and returns the highest value in the list.
def highest_value(value):
    highest=max(value)
    return highest
print(highest_value([1,2,3,4,5,6,7,8,9 ]))

# Write a Python function that takes a list of strings as input and returns
#  a new list with all the strings capitalized.
def list_capitalize(name):
    capitalize=name.upper()
    return capitalize
print(list_capitalize("hopperlab"))    









 