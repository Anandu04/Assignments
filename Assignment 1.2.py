#!/usr/bin/env python
# coding: utf-8

# In[4]:


#calculator if and fn
def add(x,y):
    return x+y
def sub(x,y):
    return x-y

a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
o=input('Enter the operation(+ or -): ')
if o=='+':
    print(add(a,b))
else:
    print(sub(a,b))


# In[ ]:




