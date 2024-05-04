#!/usr/bin/env python
# coding: utf-8

# # Task_try2

# In[ ]:


#Trying with multithreading having time module and having chunks also


# In[ ]:


import threading
import time

# Function to print numbers
def print_numbers(start, end):
    for i in range(start, end):
        print(i)

# Define the range and chunk size
start_number = 1
end_number = 100000000
chunk_size = 100000

# Calculate the number of chunks
num_chunks = (end_number - start_number) // chunk_size

# Start time
start_time = time.time()

# Create threads for printing chunks of numbers
threads = []
for i in range(num_chunks):
    start = start_number + i * chunk_size
    end = min(start_number + (i + 1) * chunk_size, end_number)
    t = threading.Thread(target=print_numbers, args=(start, end))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Print elapsed time
print("Elapsed time:", time.time() - start_time) 

