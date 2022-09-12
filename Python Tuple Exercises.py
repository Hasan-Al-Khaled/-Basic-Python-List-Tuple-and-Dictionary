#!/usr/bin/env python
# coding: utf-8

# # Python Tuple Exercises

# # One item tuple, remember the comma:

# In[1]:


thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


# # Tuple items can be of any data type:

# In[19]:


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


# # This example returns the items from "cherry" and to the end:

# In[18]:


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


# # In the above methods, we use the positive index to access the value in Python, and here we will use -ve index within [].

# In[17]:


var = ("Learn", "for", "Carrier")

print("Value in Var[0] = ", var[0])
print("Value in Var[1] = ", var[1])
print("Value in Var[2] = ", var[2])


# # Using square brackets we can get the values from tuples in Python

# In[16]:


var = ("Learn", "for", "Carrier")

print("Value in Var[0] = ", var[0])
print("Value in Var[1] = ", var[1])
print("Value in Var[2] = ", var[2])


# # Slicing Tuples in Python

# In[9]:


# code to test slicing

tuple1 = (0 ,1, 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])


# # python code for creating tuples in a loop

# In[14]:


tup = ('Hasan AL khaled',)
n = 5 # Number of time loop runs
for i in range(int(n)):
 tup = (tup,)
 print(tup)


# In[ ]:





# In[ ]:





# In[ ]:




