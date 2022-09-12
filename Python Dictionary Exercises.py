#!/usr/bin/env python
# coding: utf-8

# # Python Dictionary Exercises

# # Create and print a dictionary:

# In[14]:


dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# # Print the "brand" value of the dictionary:

# In[15]:


dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


# # Using = Operator to Copy Dictionaries

# In[24]:


original = {1:'one', 2:'two'}
new = original


# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)


# # Duplicate values will overwrite existing values:

# In[20]:


dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


# # Make a copy of a dictionary with the copy() method:

# In[21]:


dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


# # Update the "year" of the car by using the update() method:

# In[ ]:


dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


# # The pop() method removes the item with the specified key name:

# In[12]:


dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


# # Adding an item to the dictionary is done by using a new index key and assigning a value to it:

# In[11]:


dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


# # Create a dictionary that contain three dictionaries:

# In[22]:


myfamily = {
  "child1" : {
    "name" : "HAk",
    "year" : 2004
  },
  "child2" : {
    "name" : "Hasan",
    "year" : 2007
  },
  "child3" : {
    "name" : "Nirob",
    "year" : 2011
  }
}


# # Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

# In[27]:


child1 = {
  "name" : "Hasan",
  "year" : 2004
}
child2 = {
  "name" : "Nirob",
  "year" : 2007
}
child3 = {
  "name" : "HAk",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


# # Using copy() to Copy Dictionaries

# In[25]:


original = {1:'one', 2:'two'}
new = original.copy()


# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)


# In[ ]:




