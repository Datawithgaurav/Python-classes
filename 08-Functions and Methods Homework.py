#!/usr/bin/env python
# coding: utf-8

# # Functions and Methods Homework 
# 
# Complete the following questions:
# ____
# **Write a function that computes the volume of a sphere given its radius.**
# <p>The volume of a sphere is given as $$\frac{4}{3} πr^3$$</p>

# In[17]:


def vol(rad):
    print((4*3.14*rad**3)/3)
    pass


# In[18]:


# Check
# how with pass
vol(2)


# ___
# **Write a function that checks whether a number is in a given range (inclusive of high and low)**

# In[17]:


def ran_check(num,low,high):
    if num>low and num<high:
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('not in range')
        pass


# In[19]:


# Check
ran_check(10,3,20)


# If you only wanted to return a boolean:

# In[40]:


def ran_bool(num,low,high):
    a=num in range(low,high)
    return a


# In[39]:


ran_bool(11,1,10)


# ____
# **Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**
# 
#     Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#     Expected Output : 
#     No. of Upper case characters : 4
#     No. of Lower case Characters : 33
# 
# HINT: Two string methods that might prove useful: **.isupper()** and **.islower()**
# 
# If you feel ambitious, explore the Collections module to solve this problem!

# In[62]:


def up_low(s):
    cl=cu=0
    for i in s:
        if i.isupper():
            cu+=1
        elif i.islower():
            cl+=1
        else:
            pass
    print('No. of Upper case characters : ',cu)
    print('No. of Lower case characters : ',cl)       


# In[63]:


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# ____
# **Write a Python function that takes a list and returns a new list with unique elements of the first list.**
# 
#     Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#     Unique List : [1, 2, 3, 4, 5]

# In[72]:


def unique_list(lst):
    #l=set(lst)
    print(list(set(lst)))
    pass


# In[73]:


unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


# ____
# **Write a Python function to multiply all the numbers in a list.**
# 
#     Sample List : [1, 2, 3, -4]
#     Expected Output : -24

# In[76]:


def multiply(numbers):
    mul=1
    for i in numbers:
        mul*=i
    print(mul)
    pass


# In[79]:


multiply([1,2,3,-4])


# ____
# **Write a Python function that checks whether a passed in string is palindrome or not.**
# 
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

# In[83]:


def palindrome(s):
    l=s[::-1]
    check=s==l
    print(check)
    pass


# In[86]:


palindrome('helleh')


# ____
# #### Hard:
# 
# **Write a Python function to check whether a string is pangram or not.**
# 
#     Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#     For example : "The quick brown fox jumps over the lazy dog"
# 
# Hint: Look at the string module

# In[15]:


import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    pass


# In[93]:


ispangram("The quick brown fox jumps over the lazy dog")


# In[17]:


string.ascii_lowercase


# #### Great Job!
