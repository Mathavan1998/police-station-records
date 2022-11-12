#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv('D:/New folder/archive/3. Police Data.csv')


# In[4]:


data.head(2)


# In[5]:


data.isnull().sum()


# In[7]:


data.drop( columns='country_name',inplace=True)


# In[8]:


data.head(2)


# In[14]:


data[(data['violation_raw']=='Speeding')]['driver_gender'].value_counts()


# In[15]:


data.head(2)


# In[17]:


data.groupby('driver_gender')['search_conducted'].sum()


# In[18]:


data['search_conducted'].value_counts()


# In[19]:


data.head(2)


# In[22]:


data.stop_duration.value_counts()


# In[23]:


data['stop_duration']=data['stop_duration'].map({'0-15 min':7.5,'16-30 Min':24,'30+ Min':45})


# In[27]:


data.head(50)


# In[28]:


data['stop_duration'].mean()


# In[29]:


data.head(2)


# In[31]:


data.groupby('violation').driver_age.describe()


# In[ ]:




