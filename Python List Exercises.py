#!/usr/bin/env python
# coding: utf-8

# # Python List Exercises

# # Generate all permutations of a list in Python

# In[11]:


import itertools
print(list(itertools.permutations([1,2,3])))


# # Write a Python program to sum all the items in a list.

# In[3]:


def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,4,3,5,]))


# # Write a Python program to check a list is empty or not.

# In[10]:


l = []
if not l:
  print("List is empty")
  


# # Write a Python program to multiply all the items in a list. 

# In[ ]:


# def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,8,-4]))


# # Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']

# In[9]:


def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))


# # Write a Python program to remove duplicates from a list.

# In[8]:


a = [1,2,3,2,1,5,6,4,8,5,4]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)


# # Difference between the two lists

# In[12]:


list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)


# # Generate all sublists of a list

# In[13]:


from itertools import combinations
def sub_lists(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs


l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
print("Original list:")
print(l1)
print("S")
print(sub_lists(l1))
print("Sublists of the said list:")
print(sub_lists(l1))
print("\nOriginal list:")
print(l2)
print("Sublists of the said list:")
print(sub_lists(l2))


# # Get variable unique identification number or string

# In[14]:


x = 100
print(format(id(x), 'x'))
s = 'w3resource'
print(format(id(s), 'x')) 


# # Move all zero digits to end of a given list of numbers

# In[15]:


def test(lst):
    result = sorted(lst, key=lambda x: not x) 
    return result
nums = [3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1]
print("\nOriginal list:")
print(nums)
print("\nMove all zero digits to end of the said list of numbers:")
print(test(nums)) 


# # Convert a given number (integer) to a list of digits

# In[16]:


def digitize(n):
  return list(map(int, str(n)))
print(digitize(123))
print(digitize(1347823)) 


# In[ ]:




