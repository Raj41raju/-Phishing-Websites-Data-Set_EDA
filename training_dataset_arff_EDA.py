#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
warnings.filterwarnings("ignore")


# In[3]:


data=pd.read_csv('training_dataset_arff.csv',header=None)


# In[4]:


column_name=['having_IP_Address',
'URL_Length',
'Shortining_Service',
'having_At_Symbol',
'double_slash_redirecting',
'Prefix_Suffix',
'having_Sub_Domain',
'SSLfinal_State',
'Domain_registeration_length',
'Favicon',
'port',
'HTTPS_token',
'Request_URL',
'URL_of_Anchor',
'Links_in_tags',
'SFH',
'Submitting_to_email',
'Abnormal_URL',
'Redirect',
'on_mouseover',
'RightClick',
'popUpWidnow',
'Iframe',
'age_of_domain',
'DNSRecord',
'web_traffic',
'Page_Rank',
'Google_Index',
'Links_pointing_to_page',
'Statistical_report',
'Result'
]


# In[5]:


data.columns=column_name


# In[6]:


data.head()


# In[7]:


data.columns


# In[17]:


data.shape


# In[8]:


data.info()


# In[9]:


data.describe().T


# In[10]:


data.isnull().sum()


# ### Observation
# There is not any null value in dataset

# # Checking the unique values of each features

# In[13]:


data['having_IP_Address'].value_counts()


# In[14]:


data['URL_Length'].value_counts()


# In[16]:


data['Shortining_Service'].value_counts()


# In[18]:


data['having_At_Symbol'].value_counts()


# In[19]:


data['double_slash_redirecting'].value_counts()


# In[20]:


data['Prefix_Suffix'].value_counts()


# In[21]:


data['having_Sub_Domain'].value_counts()


# In[22]:


data['SSLfinal_State'].value_counts()


# In[23]:


data['Domain_registeration_length'].value_counts()


# In[24]:


data['Favicon'].value_counts()


# In[25]:


data['port'].value_counts()


# In[26]:


data['HTTPS_token'].value_counts()


# In[27]:


data['Request_URL'].value_counts()


# In[28]:


data['URL_of_Anchor'].value_counts()


# In[29]:


data['Links_in_tags'].value_counts()


# In[30]:


data['SFH'].value_counts()


# In[31]:


data['Submitting_to_email'].value_counts()


# In[32]:


data['Abnormal_URL'].value_counts()


# In[33]:


data['Redirect'].value_counts()


# In[34]:


data['on_mouseover'].value_counts()


# In[35]:


data['RightClick'].value_counts()


# In[36]:


data['popUpWidnow'].value_counts()


# In[37]:


data['Iframe'].value_counts()


# In[38]:


data['age_of_domain'].value_counts()


# In[39]:


data['DNSRecord'].value_counts()


# In[40]:


data['web_traffic'].value_counts()


# In[41]:


data['Page_Rank'].value_counts()


# In[42]:


data['Google_Index'].value_counts()


# In[43]:


data['Links_pointing_to_page'].value_counts()


# In[44]:


data['Statistical_report'].value_counts()


# In[45]:


data['Result'].value_counts()


# In[15]:


data.columns


# In[ ]:




