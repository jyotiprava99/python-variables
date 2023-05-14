#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


print("I am a Girl")


# In[4]:


a=10
b=20
print("The sum of the two no :", a+b)


# In[5]:


a= 45
print("Remainder of the no :", a%2)


# In[6]:


a= int(input("enter a no:"))
print(a)
print(type(a))


# In[7]:


#find the avg the number
a=int(input("Enter a 1st number:"))
b=int(input("Enter a 2nd number"))
Avg = (a+b)/2
print(Avg)


# In[9]:


a=int(input("Enter a no:"))
sq=a*a
print("Square of a number :", sq)


# In[10]:


a=34
b="Jyoti"
print(a,b)
print(type(b))


# In[11]:


#string slicing
greeting = "Good Morning"
name= "jyoti"
print(type(name))
print(greeting + name)


# In[16]:


name = "jyoti"
print(name[0])
print(name[2])
print(name[0:3])
print(name[1:4])


# In[29]:


story="once upon a time\nthere was a girl"
print(story[0:9])
print(len(story))
print(story.endswith("notes"))
print (story.count("e"))
print(story.capitalize())
print(story.find("kiki"))
print(story.replace("girl", "kiki"))
print(story)


# In[32]:


a=input("Enter your name:\n")
b="Good afternoon,"
print(b+a)


# In[38]:


letter= "Dear <name>\nYou are selected !\n Congratulations\n date:<date>"
name=input("Enter your name:")
date= int(input("Enter date:"))
print(letter.replace("<name>",name))
print(letter.replace("<date>", date))


# In[ ]:




