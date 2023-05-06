#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[107]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# # Loading the dataset

# In[104]:


df1 = pd.read_csv('Test.csv')
df2 = pd.read_csv('Train.csv')


# # Exploratort Data Analysis and Data Cleaning

# In[106]:


# Basic Data Exploration- Now in this step,we will perform the below operations to check what the data set comprises of.
df1.head()



# In[6]:


df2.head()


# In[7]:


df1.tail()


# In[8]:


df2.tail()


# In[9]:


#Let us see how many rows and columns are present in our data set.
df1.shape


# In[10]:


#Let us see how many rows and columns are present in our data set.
df2.shape


# # Loading the data set,we will loading the EDA Item_Type using pandas
# 

# In[54]:


df2.boxplot(column=["Item_Outlet_Sales"])
plt.show


# In[55]:


df1.boxplot(column=["Item_MRP"])
plt.show


# In[11]:


# Let us see the columns in dataset.
df1.columns


# In[ ]:


# Let us see the columns in dataset.


# In[12]:


df2.columns


# In[13]:


# Now we check the datatypes
df1.info()


# In[14]:


# Now we check the datatypes
df2.info()


# In[21]:


df1.nunique() # check unique values in each column


# In[22]:


df2.nunique() # check unique values in each column


# In[25]:


# described method will help here to see how the data has been spread for numerical values. We can clearly see the minimum value, mean values, different percentile values, and maximum values.
df1.describe()


# In[26]:


# described method will help here to see how the data has been spread for numerical values. We can clearly see the minimum value, mean values, different percentile values, and maximum values.
df2.describe()


# # Handling the missing values

# In[23]:


df1.isnull().sum() 


# In[24]:


df2.isnull().sum()


# In[63]:


# Here we remove the columns of missing values and if chages any dataframe then will use here inplace.
df1.drop(['Item_Weight', 'Outlet_Size'], axis = 1, inplace = True)
df1.dropna(inplace = True)


# In[64]:


df1.isnull().sum()


# In[65]:


df2.drop(['Item_Weight', 'Outlet_Size'], axis = 1, inplace = True)
df2.dropna(inplace = True)


# In[66]:


df2.isnull().sum()


# In[67]:


df1.describe()


# In[27]:


df1.head()


# In[34]:


df1.duplicated().sum() # check duplicate values


# In[35]:


df2.duplicated().sum() # check duplicate values


# # Handling check the duplicates record of big mart items products.

# In[59]:


duplicate = df1.duplicated()
print(duplicate.sum())
df1[duplicate]


# In[36]:


# here some data type is objects data type that is categorical culumns so lets we check here how many uniques values are in  categorical column.
df1.describe(include = 'object')


# In[37]:


# here some data type is objects data type that is categorical culumns so lets we check here how many uniques values are in  categorical column.
df2.describe(include = 'object')


# # Data Analysis and visualizations

# # Here we predict the  items outlet sales  data as per given sheet.  so we merge here both train and test data in EDA

# In[77]:


df1['source'] = 'train'
df1['source'] = 'test'
df1['Item_Outlet_Sales'] = 0
data = pd.concat([df1, df2], sort = False)
print(df1.shape, df2.shape, data.shape)


# In[78]:


data['Item_Outlet_Sales'].describe()


# In[79]:


data['Item_MRP'].describe()


# In[81]:


import seaborn as sns


# In[82]:


sns.distplot(data['Item_Outlet_Sales'])


# In[83]:


data.dtypes


# In[89]:


data['Outlet_Establishment_Year'].value_counts()


# # To check the missing values in the given dataset

# In[93]:


data.apply(lambda x: sum(x.isnull()))


# In[94]:


data.apply(lambda x : len(x.unique()))


#  # determine the years of opeation of sales in a store. 

# In[96]:


data['Outlet_Years'] = 2009 - data['Outlet_Establishment_Year']
data['Outlet_Years'].describe()


# In[97]:


data.groupby('Outlet_Establishment_Year')['Item_Outlet_Sales'].mean().plot.bar()


# In[98]:


df1.head()


# In[99]:


temp_data = data.loc[data['Outlet_Establishment_Year'] == 1998]


# In[100]:


temp_data['Outlet_Type'].value_counts()


# In[102]:


test_temp_data = df1.loc[df1['Outlet_Establishment_Year'] == 1998]
test_temp_data['Outlet_Type'].value_counts()


# # Now the entire process has been done of bigmart sales data of different 10 stores in differenr city of  1559 product. This is just a trial asumption from my end with some help from other websites. In this summaery i have tried to look out all the assumtion of given data. The deeply aanlysis has been shown here and few steps are not covered.
# 

# In[ ]:




