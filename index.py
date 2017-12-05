
# coding: utf-8

# In[1]:

from skafossdk import *

ska = Skafos()


# In[4]:

ska.engine.create_view(
    "power_datum", 
    {"keyspace": "power", "table": "hist_load"}, 
    DataSourceType.Cassandra).result()


# In[5]:

power = ska.engine.query("SELECT * from power_datum limit 10").result()['data']


# In[9]:

power


# In[12]:

import pandas as pd


# In[8]:

pd.DataFrame.from_dict(power)

