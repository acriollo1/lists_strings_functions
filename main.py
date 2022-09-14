#!/usr/bin/env python
# coding: utf-8

# # Objectives Week 4



# string manipulation 
text = "ABCDEFJHIJKLMNOPQR"
#substring??
fragment = text[::3]
print(fragment.lower())

#splitting strings
text2 = "we are learning about splitting strings"
print(len(text2))
#split allows us split strings into different characters or words
print(text2.split())
splitText = text2.split()
print(splitText[4])








# 1. Understand lists in python programming, 
# 2. list functions, 
# 3. tuples, 
# 4. methods and functions,
# 5. if statements and comparisons in **python** **bold text**
# 6. by the end of the week, you will learn to develop a text parser, a program that the user will enter any kind of text and the code will give them any information about that text: you will have to learn the index method, extracting sub-strings, methods and properties of string.
# ## copy this to your own drive

# # First lets go over simpler index methods
# 

# In[ ]:


#we know the traditional way. You might find this way annoying. 
#There are several other ways you can format or insert variables into string texts
#lets take a look at indexing in python again


# ![image.png](attachment:image.png)

# In[3]:


#print your result


# In[7]:


#lets take a look at substrings


# In[ ]:





# # Lists

# In[ ]:


#Lists allow you to store multiple items in one variable instead of separate items
#now you are entering the world of data structures
#lists are known as arrays in other programs
#python calls arrays lists --> they are like a book shelf of items
#List are ordered sequences that can hold a variety of object types
#They use [] brackets and commas to separate objects in a the list
#[1,2,3,4,5]
#List support indexing and slicing. Lists can be nested and also have a variety of useful methods that can be called off of them.#


# In[ ]:


apples = 3
oranges = 4
grapes = 50
mangos = 5
#list
groceries = [apples, oranges, grapes, mangos]
print(groceries)
print(groceries[-1])


# In[1]:


#CREATE  A LIST OF FRIENDS AND print out the 1st and last friend
friends = []

#lists are mutable -- means I can change it


# In[2]:


birthday_guests = ["femi", "will", "luis"]
Christmas_guests =["hou", "jessie","Tom"]

#joins my list 
#concatenation
newList = birthday_guests + Christmas_guests
print(newList)
#remove
print(newList.remove("Tom"))
print(newList)
newList.append("rebecca")
newList.append("jose")
newList.append("james")
print(newList)
print(newList.sort())
print(len(newList))


# birthday_guests[0] ="charlie"


# add

#sort


#.remove(), .append(), sort(), .len() are list functions
newList = ["num1, num2, num3, num4"]
oldList = ["num5, num6, num7, num 8"]
print(newList)
print(oldList)



# In[3]:


#also we can define N dimensional list not just 1 dimensional
#1 dimensional means only one item per comma
avengers = ["hawkeye", "hulk", "iron man", "shang chi", "black panther", "capAmer"]
multiDimen = [[3, 5], [7, 6], [6, 3], [8, 9]]
print(multiDimen[0][0])
#multidimensional arrays are more than just a single list of items


# In[ ]:





# In[ ]:


#create a list that contains at least one string, one integer and one float
#for example: [1, "two", 3.14566]
#Note that the order and number of items doesnt matter


# # List functions

# In[ ]:

avengers = ["hawkeye", "hulk", "iron man", "shang chi", "black panther", "capAmer"]
guardiansOfGalaxy = ["drax", "rocket", "groot", "starlord", "gamora"]
newList = avengers + guardiansOfGalaxy
print(newList)
newList.append("Tom")
newList.append("Mini")
print(newList)
newList.reverse() 
print(newList)
newList.remove("gamora")
print(newList)
print(newList.index("drax"))


# #Tuples

# In[ ]:


# exactly the same thing as an array only it is immutable, once you define the tuple, you cannot change it


# In[1]:


#you define a tuple with () instead of [] like you would in lists
#once you define it, you cannot change it
#example
coordinates = (4,5)


# #Functions and methods

# In[ ]:





# #return statement

# In[ ]:





# #if statements

# ![image.png](attachment:image.png)

# #if statements and comparisons

# In[ ]:





# In[ ]:





# # #challenge --- building a better calculator

# In[ ]:





# In[ ]:





# 
