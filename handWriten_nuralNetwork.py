#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[2]:


(X_train, y_train) , (X_test, y_test) = keras. datasets.mnist. load_data ()


# In[3]:


len(X_train)


# In[4]:


X_train[0]


# In[5]:


plt.matshow(X_train[0])


# In[10]:


y_train[0]


# In[6]:


plt.matshow(X_train[9])


# In[7]:


y_train[9]


# In[8]:


plt.matshow(X_train[23])


# In[9]:


y_train[23]


# In[11]:


plt.matshow(X_train[50])


# In[13]:


y_train[50]


# In[ ]:




