#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Can not devide by zero!')
    return x / y


# In[4]:


"""x  =5
y = 5
divide(5, 5)
add(x, y)
subtract(x, y)
multiply(x, y)
"""


# In[ ]:




