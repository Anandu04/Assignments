#!/usr/bin/env python
# coding: utf-8

# # 1 Dictionary

# In[1]:


#Dictionary

#clear()
d1={'vehicle':'bike','brand':'Honda','Price':150000}
print(d1)
d1.clear()
print(d1)

#copy()
car={"brand":"MARUTI","model":"DZIRE","year":2009}
c=car.copy()
print(c)

#fromkeys()
k1=('key1','key2','key3')
v1=13
thisdict=dict.fromkeys(k1,v1)
print(thisdict)

#get()
car={"brand":"MARUTI","model":"DZIRE","year":2009}
g=car.get("model")
print(g)

#items()
car={"brand":"MARUTI","model":"DZIRE","year":2009}
i=car.items()
print(i)

#keys()
car={"brand":"MARUTI","model":"DZIRE","year":2009}
k=car.keys()
print(k)

#pop()
car={"brand":"MARUTI","model":"DZIRE","year":2009}
car.pop('year')
print(car)

#popitem()
car={"brand":"MARUTI","model":"DZIRE","year":2009}
car.popitem()
print(car)

#setdefault
car={"brand":"MARUTI","model":"DZIRE","year":2009}
car.setdefault('brand','swift')
print(car)
car.setdefault('price',1500000)
print(car)

#update()
car={"brand":"MARUTI","model":"DZIRE","year":2009}
car.update({'price':900000})
print(car)

#values()
car={'brand': 'MARUTI', 'model': 'DZIRE', 'year': 2009, 'price': 1500000}
v=car.values()
print(v)


# # 2 STRING

# In[2]:


#String

x=("hello world")
print(x)

#capitalize()
print(x.capitalize())

#casefold()
print(x.casefold())

#center()
x=("hello world")
y=x.center(20)
print(y)

#index()
print(x.index("world"))

#count()
x=('hello world! World is innovative! hello guys')
print(x.count("hello"))

#encode()
x=("hello world")
print(x.encode())

#endswith()
x=("hello world")
print(x.endswith("."))

#find()
print(x.find("world"))

#format()
x="I am studying {here}"
print(x.format(here="python"))

#isalnum()
print(x.isalnum())

#isalpha
x=("helloworld")
print(x.isalpha())

#isdecimal()
print(x.isdecimal())

#isdigit()
x="567"
x.isdigit()

#isidentifier
x='i'
x.isidentifier()

#islower()
x='hi hello hi'
x.islower()

#istitle
x=("Hello World")
print(x.istitle())

#isupper
x=("HELLO")
print(x.isupper())

#lower()
x=("HELLO")
print(x.lower())

#strip()
x='Hello World'
x.strip()

#lstrip()
txt="   maths"
x=txt.lstrip()
print("of all subjects", x, "is my favorite")

#maketrans()
x=("hello world")
y=x.maketrans("h","d")
print(x.translate(y))

#partition()
x=("i study python")
print(x.partition("study"))

#replace()
print(x.replace("python","mathematics"))
print(x)

#rfind()
x=("i study python")
print(x.rfind("python"))
#rindex()
print(x.rindex("python"))

#upper
print(x.upper())

#title()
print(x.title())

#zfill()
x='10'
print(x.zfill(10))

#swapcase()
x=("Hello World")
print(x.swapcase())

#startswith()
print(x.startswith("Hello"))

#splitlines()
x=("hi there/how are you")
print(x.splitlines())


#split()
x=("hi there ")
print(x.split())

#rsplit()
print(x.rsplit())
print(x)

#rjust()
x='hi'
y=x.rjust(10)
print(y,"how are you")


# # 3 Lists and Dictionary

# In[3]:


#dictonary inside a list
l=[{1:'a','b':2},55,1.0,{'mydict':5,'dict':'d2'},100,'a']
print(l[3]['mydict'])
print(l[1])
print(l[0]['b'])


# In[4]:


#list inside a dictionary
d={'a':100,'b':'a','l':[1,2,3,4,5],'l2':[544,644,555,888]}
print(d['l'][1])
print(d['l'][0])
print(d['a'])
print(d['l2'][2])


# # 4 TUPLE

# In[5]:


#tuple
t=(1,2,'a','b',100.1,'car')
print(t)
l=list(t)
l.append('addedd')
t=tuple(l)
print(t)


# # 5 Pattern

# In[6]:


#using For
for i in range(5,0,-1):
    for j in range(0,5-i):
        print(end=" ")
    for k in range(0,i):
        print("*", end=" ")
    print()
for a in range(2,6):
    for b in range(5-a,0,-1):
        print(end=" ")
    for c in range(0,a):
        print("*", end=" ")
    print()


# In[7]:


#using While
i=5
while i>1:
    print(" "*(5-i)+"* "*i)
    i-=1
j=1
while j<=5:
    print(" "*(5-j)+"* " *j)
    j+=1


# In[ ]:




