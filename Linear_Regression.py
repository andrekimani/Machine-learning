#!/usr/bin/env python
# coding: utf-8

# In[95]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(color_codes=True)


# In[96]:


data= pd.read_csv(r"C:\Users\LENOVO i5\Downloads\Real estate.csv")
data.head()


# In[97]:


data[['X3 distance to the nearest MRT station','Y house price of unit area']].head(20)


# In[108]:


data[['X2 house age','Y house price of unit area']].head(20)


# In[110]:


data[['X4 number of convenience stores','Y house price of unit area']].head(20)


# In[104]:


data.sort_values(by='X3 distance to the nearest MRT station', ascending=True).head(50)


# In[103]:


sns.scatterplot(data['X3 distance to the nearest MRT station'],data['Y house price of unit area'])


# In[121]:


data[['X3 distance to the nearest MRT station','Y house price of unit area']].tail(10)


# In[119]:


Distance=[289,131,372,2409,2176,4082,90,391,105,90]
House_price=[41.2,37.2,40.5,22.3,28.1,15.4,50.0,40.6,52.5,63.9]
print("DISTANCE MEAN:",np.mean(Distance))
print("HOUSE PRICE MEAN:",np.mean(House_price))


# In[134]:


data_x_train =data.X3_distance_to_the_nearest_MRT_station[404:410]
data_x_test = data.X3_distance_to_the_nearest_MRT_station[410:413]

data_y_train=data.Y_house_price_of_unit_area[404:410]
data_y_test=data.Y_house_price_of_unit_area[410:413]


# In[ ]:





# In[ ]:





# In[ ]:




