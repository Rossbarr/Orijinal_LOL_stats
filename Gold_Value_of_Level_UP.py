# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 21:14:51 2020

@author: Barrett

This file sets out to answer the question of:
"How much is the gold value of a level up? How much does this change between levels (is it more valuable to level up from 1 to 2 or 17 to 18)?"

TO-DO: make currently displayed graph show level up not AS per level up!
TO-DO: rework to make work with new modules.champion_get function!
"""

import modules.Champion_Get as cg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# from sklearn import datasets, linear_model
# from sklearn.metrics import mean_squared_error, r2_score

champs = cg.champion_get('data/champion.json')

level = np.arange(1,19,1)

tags = []

support_mean = np.zeros(18)
si = 0
marksman_mean = np.zeros(18)
mmi = 0
mage_mean = np.zeros(18)
mi = 0
tank_mean = np.zeros(18)
ti = 0
fighter_mean = np.zeros(18)
fi = 0
assassin_mean = np.zeros(18)
ai = 0

stat = 'attackspeed'
for index, row in champs.iterrows():
    if index == 'Senna':
        pass
    else:
        [tags.append(tag) for tag in row['tags'] if tag not in tags]

        hp = cg.Stat_Growth(base = row['hp'],
                    growth = row['hpperlevel'],
                    max_level = level[-1])
        mp = cg.Stat_Growth(base = row['mp'], 
                            growth = row['mpperlevel'],
                            max_level = level[-1])
        ms = cg.Stat_Growth(base = row['movespeed'], 
                            growth = 0,
                            max_level = level[-1])
        armor = cg.Stat_Growth(base = row['armor'], 
                            growth = row['armorperlevel'],
                            max_level = level[-1])
        mr = cg.Stat_Growth(base = row['spellblock'], 
                            growth = row['spellblockperlevel'],
                            max_level = level[-1])
        attackrange = cg.Stat_Growth(base = row['attackrange'], 
                            growth = 0,
                            max_level = level[-1])
        hpregen = cg.Stat_Growth(base = row['hpregen'], 
                            growth = row['hpregenperlevel'],
                            max_level = level[-1])
        mpregen = cg.Stat_Growth(base = row['mpregen'], 
                            growth = row['mpregenperlevel'],
                            max_level = level[-1])
        crit = cg.Stat_Growth(base = row['crit'], 
                            growth = row['critperlevel'],
                            max_level = level[-1])
        ad = cg.Stat_Growth(base = row['attackdamage'],
                            growth = row['attackdamageperlevel'],
                            max_level = level[-1])
        attackspeed = cg.Stat_Growth(base = row['attackspeed'],
                            growth = row['attackspeedperlevel'],
                            max_level = level[-1])

        for tag in row['tags']:
            if tag == 'Marksman':
                marksman_mean += np.array(row[stat])
                mmi += 1
            if tag == 'Mage':
                mage_mean += np.array(row[stat])
                mi += 1
            if tag == 'Support':
                support_mean += np.array(row[stat])
                si += 1
            if tag == 'Fighter':
                fighter_mean += np.array(row[stat])
                fi += 1
            if tag == 'Tank':
                tank_mean += np.array(row[stat])
                ti += 1
            if tag == 'Assassin':
                assassin_mean += np.array(row[stat])
                ai += 1

# marksman_mean = marksman_mean/mmi
# mage_mean = mage_mean/mi
# support_mean = support_mean/si
# fighter_mean = fighter_mean/fi
# tank_mean = tank_mean/ti
# assassin_mean = assassin_mean/ai

# plt.plot(level,marksman_mean,color='gold',label='Marksman')
# plt.plot(level,mage_mean,color='blue',label='Mage')
# plt.plot(level,support_mean,color='cyan',label='Support')
# plt.plot(level,fighter_mean,color='purple',label='Fighter')
# plt.plot(level,tank_mean,color='green',label='Tank')
# plt.plot(level,assassin_mean,color='red',label='Assassin')
# plt.legend()
# plt.grid()
# plt.xlim(1, 18)
# plt.xlabel('Level')
# plt.ylabel(stat)
# plt.title('For Patch 10.2')
# plt.savefig('figures/gold_value_of_level_up.png')
# print("Saved file 'ADC_stat_growth.png' under figures/gold_value_of_level_up.png")
# plt.show()