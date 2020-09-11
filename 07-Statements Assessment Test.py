#!/usr/bin/env python
# coding: utf-8

# # Statements Assessment Test
# Let's test your knowledge!

# _____
# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

# In[1]:


st = 'Print only the words that start with s in this sentence Said Ronney'


# In[9]:


st = 'Print only the words that start with s in this sentence Said Ronney'
for i in st.split():
    if i.startswith('s'):
        print(i)


# ______
# **Use range() to print all the even numbers from 0 to 10.**

# In[10]:


#Code Here
for i in range(10):
    if i%2==0:
        print(i)


# ___
# **Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# In[4]:


#Code in this cell
l=[i for i in range(1,50) if i%3==0]
l


# _____
# **Go through the string below and if the length of a word is even print "even!"**

# In[ ]:


st = 'Print every word in this sentence that has an even number of letters'


# In[13]:


#Code in this cell
st = 'Print every word in this sentence that has an even number of letters'
for i in st.split():
    if len(i)%2==0:
        print('EVEN')
    else:
        print('odd')


# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# In[15]:


#Code in this cell
for i in range(1,100):
    if i%3==0 and i%5==0:
        print(i,"FizzBuzz")
    elif i%3==0:
        print(i,"Fizz")
    elif i%5==0:
        print(i,"Buzz")


# ____
# **Use List Comprehension to create a list of the first letters of every word in the string below:**

# In[ ]:


st = 'Create a list of the first letters of every word in this string'


# In[42]:


#Code in this cell
st = 'Create a list of the first letters of every word in this string'
l=[j[0] for j in [i for i in st.split()]]
l


# ### Great Job!
