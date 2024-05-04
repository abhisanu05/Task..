#!/usr/bin/env python
# coding: utf-8

# # Task_try3

# In[ ]:


#Trying with making chunk size


# In[ ]:


import time

start_time = time.time()

chunk_size = 1000    # Defining the chunk size

# Print numbers in chunks
for i in range(1, 100000000, chunk_size):
    for j in range(i, min(i + chunk_size, 100000000)):
        print(j)

    if time.time() - start_time >= 20:    # If 20 seconds have elapsed, break the loop
        break

