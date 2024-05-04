#!/usr/bin/env python
# coding: utf-8

# # Task_try4

# In[ ]:


#Trying with normal for loop with imorting time module


# In[1]:


import time

start_time = time.time()

for i in range(1, 100000000):
    print(i)
    if time.time() - start_time >= 20:
        break


# In[2]:


import time

print(1)
time.sleep(5)
print(2)
time.sleep(5)
for i in range(8):
    print(9)
    time.sleep(2)


# In[ ]:




