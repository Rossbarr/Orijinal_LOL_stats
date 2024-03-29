# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:15:55 2020

@author: Barrett
"""
import numpy as np
import matplotlib.pyplot as plt
from modules.Stat_To_Gold_Converter import AD_gold_value, move_speed_gold_value, mana_gold_value

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
        elif i >= 4.0:
            x[q] = 100 + mana_gold_value(100)
        elif i >= 2.0:
            x[q] = 50 + mana_gold_value(50)
        else:
            x[q] = 0
        q += 1
            
    return x

def area(x, dt):
    a = np.zeros_like(x)
    for i in range(len(x)):
        if i == 0:
            pass
        else:
            a[i] = (x[i]*dt + a[i-1])

    return a

deltatime = 0.01
time = np.arange(0.0,50,deltatime)

gold_value_of_GS = AD_gold_value(gathering_storm_AD(time))
gold_value_of_BD = biscuit_delivery_gold_value(time)
gold_value_of_MF = magical_footwear_gold_value(time)
difference = gold_value_of_MF + gold_value_of_BD - gold_value_of_GS
difference_area = area(difference, deltatime)/time

# plt.plot(time, gold_value_of_GS,
#          color = "blue",
#          label = "Gathering Storm")
# plt.plot(time, gold_value_of_BD + gold_value_of_MF,
#          color = "Green",
#          label = "Biscuit Delivery + Magical Footwear")
plt.plot(time, difference,
         color = "Red",
         label = "Difference")
# plt.plot(time, difference_area,
#          color = "Red",
#          label = "Difference Area")
plt.xlabel("Time")
plt.ylabel("(Gold * Time)")
plt.grid()
plt.legend()
# plt.savefig('figures/gathering_storm_vs_biscuits_and_magical_boots')
plt.show()