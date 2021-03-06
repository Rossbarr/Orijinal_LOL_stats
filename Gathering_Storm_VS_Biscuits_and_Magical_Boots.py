# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:15:55 2020

@author: Barrett
"""
import numpy as np
import matplotlib.pyplot as plt

# Basic Stats Gold Value
def AD_gold_value(ad_amount):
    return ad_amount*35

def AS_gold_value(as_amount):
    return as_amount*25

def crit_gold_value(crit_amount):
    return crit_amount*32

def move_speed_gold_value(ms):
    return ms*12

def mana_gold_value(mana):
    return mana*1.4

#Gathering Storm
def gathering_storm_AD(time):
    x = np.zeros_like(time)
    q = 0
    
    for i in time:
        x[q] = 1 + int(i/10)
        q += 1

    return 4.8*x*(x-1)/2

#Slightly Magical Boots
def magical_footwear_gold_value(time):
    x = np.zeros_like(time)
    q = 0
    
    for i in time:
        if i >= 12:
            x[q] = move_speed_gold_value(25+10)
            q += 1
        else:
            x[q] = 0
            q += 1
    
    return x

#Biscuit Delivery
def biscuit_delivery_gold_value(time):
    x = np.zeros_like(time) 
    q = 0
    
    for i in time:
        if i >= 6.0:
            x[q] = 150 + mana_gold_value(150)
            q += 1
        elif i >= 4.0:
            x[q] = 100 + mana_gold_value(100)
            q += 1
        elif i >= 2.0:
            x[q] = 50 + mana_gold_value(50)
            q += 1
        else:
            x[q] = 0
            q += 1
            
    return x

time = np.arange(0.0,41.0,0.1)

ad_from_gathering_storm = gathering_storm_AD(time)

gold_value_of_GS = AD_gold_value(ad_from_gathering_storm)

plt.plot(time,gold_value_of_GS,
         color="blue",
         label = "Gathering Storm")
plt.plot(time,biscuit_delivery_gold_value(time) + magical_footwear_gold_value(time),
         color = "Green",
         label = "Biscuit Delivery + Magical Footwear")
plt.xlabel("Time")
plt.ylabel("Gold Value")
plt.grid()
plt.legend()
plt.show()