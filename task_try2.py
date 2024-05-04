#!/usr/bin/env python
# coding: utf-8

# # Task_try1

# In[ ]:


# Trying with list comprehension


# In[1]:


import time

start_time = time.time()
numbers = [print(i) for i in range(1, 100000000)    #creating list comprehnsion 
           if time.time() - start_time < 20]


# In[ ]:




