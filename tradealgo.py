#!/usr/bin/env python
# coding: utf-8

# In[1]:


API = "api-fxpractice.oanda.com/"
STREAM_API = "stream-fxpractice.oanda.com/"


# In[2]:


import requests
import json
import numpy as np
import pandas as pd
from json.decoder import JSONDecodeError
import datetime as date
import time


# In[3]:


class create:
    
    def __init__(self, instrument, ltp):
        self.instrument = instrument
        self.ltp = ltp
        
        dictionary = {
            instrument : ltp
        }
        
        with open("ltp.json", 'r+') as file:
            try:  
                old_data = json.load(file)
                old_data.update(dictionary)
                json.dump(old_data,file)
            except JSONDecodeError:
                json.dump(dictionary, file)


# In[4]:


def json_to_pandas(json):
    json_file = json.json()
    price_json = json_file["candles"]
    times = []
    
    close_price,high_price,low_price,open_price =[], [], [], []
    for candle in price_json:
        times.append(candle["time"])
        close_price.append(float(candle["mid"]["c"]))
        high_price.append(float(candle["mid"]["h"]))
        low_price.append(float(candle["mid"]["l"]))
        open_price.append(float(candle["mid"]["o"]))
    
    dataframe = pd.DataFrame({"close":close_price, "high": high_price, "low": low_price, "open":open_price})
    dataframe.index  =pd.to_datetime(times)
    return dataframe
        


# In[5]:


pricingPath = "v3/accounts/ENTER ACCOUNT ID/pricing"


# In[6]:


#Europe/US

query = {"instruments": "EUR_USD"}
headers = {"Authorization": "Bearer " +  "INSERT KEY"}


# In[7]:


response = requests.get("https://"+API+pricingPath, headers=headers,params=query)


# In[8]:


response.json()


# In[9]:


json_response = response.json()
instrument = json_response["prices"][0]["instrument"]
prices = json_response["prices"][0]["asks"][0]["price"]
prices = float(prices)
ltp1=create(instrument,prices)


# In[ ]:





# In[10]:


#Creating ORB

from_time = time.mktime(pd.to_datetime("4/23/2021").timetuple())
to_time = time.mktime(pd.to_datetime("4/24/2021").timetuple())


# In[11]:


query = {"from":str(from_time), "to":str(to_time), "granularity":"M15"}


# In[12]:


candlesPath = "v3/accounts/ENTER ACCOUNT ID/instruments/"


# In[13]:


response = requests.get("https://"+API+candlesPath+instrument+"/candles", headers=headers,params=query)


# In[14]:


response.json()


# In[15]:


EURUSD_df = json_to_pandas(response)


# In[16]:


EURUSD_df.head()


# In[17]:


EURUSD_df["close"].plot()


# In[18]:


#Australia/US

query = {"instruments": "AUD_USD"}
headers = {"Authorization": "Bearer " +  "INSERT KEY"}


# In[19]:


response = requests.get("https://"+API+pricingPath, headers=headers,params=query)


# In[20]:


response.json()


# In[21]:


json_response_temp = response.json()
instrumentTemp = json_response_temp["prices"][0]["instrument"]
pricesTemp = json_response_temp["prices"][0]["asks"][0]["price"]
pricesTemp = float(pricesTemp)
ltpTemp=create(instrumentTemp,pricesTemp)


# In[ ]:





# In[ ]:





# In[22]:


#US/Japan

query = {"instruments": "USD_JPY"}
headers = {"Authorization": "Bearer " +  "INSERT KEY"}


# In[23]:


response = requests.get("https://"+API+pricingPath, headers=headers,params=query)


# In[24]:


response.json()


# In[25]:


json_response2 = response.json()
instrument2 = json_response2["prices"][0]["instrument"]
prices2 = json_response2["prices"][0]["asks"][0]["price"]
prices2 = float(prices2)
ltp2=create(instrument2,prices2)


# In[ ]:





# In[26]:


#Creating ORB

from_time = time.mktime(pd.to_datetime("4/23/2021").timetuple())
to_time = time.mktime(pd.to_datetime("4/24/2021").timetuple())


# In[27]:


query = {"from":str(from_time), "to":str(to_time), "granularity":"M15"}


# In[28]:


response = requests.get("https://"+API+candlesPath+instrument2+"/candles", headers=headers,params=query)


# In[29]:


response.json()


# In[30]:


JPYUSD_df = json_to_pandas(response)


# In[31]:


JPYUSD_df.head()


# In[32]:


JPYUSD_df["close"].plot()


# In[ ]:





# In[33]:


#Europe/Japan

query = {"instruments": "EUR_JPY"}
headers = {"Authorization": "Bearer " +  "INSERT KEY"}


# In[34]:


response = requests.get("https://"+API+pricingPath, headers=headers,params=query)


# In[35]:


response.json()


# In[36]:


json_response3 = response.json()
instrument3 = json_response3["prices"][0]["instrument"]
prices3 = json_response3["prices"][0]["asks"][0]["price"]
prices3 = float(prices3)
ltp3=create(instrument3,prices3)


# In[ ]:





# In[37]:


#Creating ORB

from_time = time.mktime(pd.to_datetime("4/23/2021").timetuple())
to_time = time.mktime(pd.to_datetime("4/24/2021").timetuple())


# In[38]:


query = {"from":str(from_time), "to":str(to_time), "granularity":"M15"}


# In[39]:


response = requests.get("https://"+API+candlesPath+instrument3+"/candles", headers=headers,params=query)


# In[40]:


response.json()


# In[41]:


EURJPY_df = json_to_pandas(response)


# In[42]:


EURJPY_df.head()


# In[43]:


EURJPY_df["close"].plot()

