#!/usr/bin/env python
# coding: utf-8

# In[28]:


#Lists
l1=[1,2,3,'a','r']
print(l1)

#append()
l1.append('hi')
print(l1)

#clear()
l2=[1,2,3,'a','r','h','14',1.1]
print(l2)
l2.clear()
print(l2)

#copy()
l3=['car','bike','cycle']
print(l3)
copy=l3.copy()
print(copy)

#count()
l4=[1,2,3,3,4,5,9,9,9,1,3,4,33,3]
print(l4)
print(l4.count(3))

#extend()
l5=[1,2,3,4,5,6]
print(l5)
le=['a','b','c','d']
print(le)
l5.extend(le)
print(l5)

#index()
l6=['5',5,4,18,99,25,100]
print(l6.index(99))

#insert()
l7=[6,12,18,24,30,42,48]
print(l7)
l7.insert(5,36)
print(l7)

#pop()
l8=[5,6,7,8,9,99,88]
print(l8)
l8.pop()
print(l8)

#remove()
l9=['mustang','chervolet','maruti','mercedes']
print(l9)
l9.remove('maruti')
print(l9)

#reverse()
l0=[9,8,7,6,5,4,3,2,1,0]
print(l0)
l0.reverse()
print(l0)

#sort()
l=['banana','apple','zebra','elephant']
print(l)
l.sort()
print(l)


# In[ ]:




