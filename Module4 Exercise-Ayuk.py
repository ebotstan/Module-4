#!/usr/bin/env python
# coding: utf-8

# ### Module 4 Exercise

# 1. How many occurences of "row" is in "Row, row, row your boat. Gently down the stream. Merrily, merrily, merrily, merrily. Life is but a dream. Row, row, row your boat. Gently up the creek." 

# In[2]:


message = "Row, row, row your boat. Gently down the stream. Merrily, merrily, merrily, merrily. Life is but a dream. Row, row, row your boat. Gently up the creek."
print(message.count("row"))


# 2. Ask a user for a name, color, and an animal.  <br>
# Then using string format method per each line, show following:<br>
# <b><i>name</i></b> had a little <b><i>animal</i></b>. <br>
# It was <b><i>color</i></b> as snow. <br>
# And everywhere that <b><i>name</i></b> went, the <b><i>animal</i></b> was sure to go.

# In[3]:


name = input("What is your name?: ")
color = input("state your favorite color: ")
animal = input("name an animal: ")
print(f"{name} had a little {animal}")
print(f"It was {color} as snow")
print(f"And everywhere that {name} went, the {animal} was sure to go.")


# In[ ]:





# 3. Print 3.14159 in a scientific number notation 

# In[14]:


print(f"{3.14159:e}")


# 4. Print 3.1559 in 3 decimal places

# In[13]:


print(f"{3.1559:.3f}")


# 5. Print 1589.92341 in a scientific number notation to the power of 3

# In[16]:


print(f"{1589.92341:3e}")


# 6. Convert 39 to a binary number using floor division and mod operators. Then, compare your answer using bin() and int() functions.

# In[30]:


39//2
39%2


# In[31]:


19//2
19%2


# In[32]:


9//2
9%2


# In[33]:


4//2
4%2


# In[34]:


2//2
2%2


# In[35]:


1//2
1%2


# In[26]:


bin(39)


# In[29]:


int(0b100111)


# 7. Convert 39 to an octal number using floor division and mod operators. Then, compare your answer using oct() and int() functions.

# In[41]:


39//8 
39%8


# In[42]:


4//8
4%8


# In[38]:


oct(39)


# In[40]:


int(0o47)


# 8. Convert 39 to a hexadecimal number using floor division and mod operators. Then, compare your answer using hex() and int() functions.

# In[47]:


39//16
39%16


# In[48]:


2//16
2%16


# In[45]:


hex(39)


# In[46]:


int(0x27)


# 9. Ask a user for an amount and a tax rate in percentage. Then, display the amount, rate in percentage, calculated tax amount, and the total (amount + tax amount) in one <b>nice</b> formmated print statement.

# In[51]:


amount = int(input("enter an amount in $: "))
tax_rate = float(input("enter a tax rate in %: "))
print(f"The price is ${amount}, the tax is {tax_rate}, the tax amount is ${amount * tax_rate} and the total is ${amount + amount * tax_rate}.")


# In[ ]:





# In[ ]:




