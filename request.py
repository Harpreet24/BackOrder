#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json

url = 'http://localhost:5000/predict_api'
data= {'radius_mean':2, 'texture_mean':1, 'smoothness_se':4,'concavity_se':5,'perimeter_worst':1,'smoothness_worst':3}
data=json.dumps(data)
r = requests.post(url,json=data)

print(r.json())

