# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 21:14:51 2020

@author: Barrett
"""

import sys
sys.path.append('C:\\Users\\Barrett\\Documents\\League of Legends Stats')

import Champion_Get as cg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

champs = cg.champion_get()

level = np.arange(1,19,1)

tags = []
data = pd.DataFrame(data = [], 
                    index = [], 
                    columns = ['name',
                               'tags',
                               'hp',
                               'mp',
                               'ms',
                               'armor',
                               'mr',
                               'attackrange',
                               'hpregen',
                               'mpregen',
                               'crit',
                               'ad',
                               'attackspeed'])

for champ in champs:
    hp = cg.Stat_Growth(base = champ.stats['hp'],
                        growth = champ.stats['hpperlevel'],
                        max_level = level[-1])
    mp = cg.Stat_Growth(base = champ.stats['mp'], 
                        growth = champ.stats['mpperlevel'],
                        max_level = level[-1])
    ms = cg.Stat_Growth(base = champ.stats['movespeed'], 
                        growth = 0,
                        max_level = level[-1])
    armor = cg.Stat_Growth(base = champ.stats['armor'], 
                        growth = champ.stats['armorperlevel'],
                        max_level = level[-1])
    mr = cg.Stat_Growth(base = champ.stats['spellblock'], 
                        growth = champ.stats['spellblockperlevel'],
                        max_level = level[-1])
    attackrange = cg.Stat_Growth(base = champ.stats['attackrange'], 
                        growth = 0,
                        max_level = level[-1])
    hpregen = cg.Stat_Growth(base = champ.stats['hpregen'], 
                        growth = champ.stats['hpregenperlevel'],
                        max_level = level[-1])
    mpregen = cg.Stat_Growth(base = champ.stats['mpregen'], 
                        growth = champ.stats['mpregenperlevel'],
                        max_level = level[-1])
    crit = cg.Stat_Growth(base = champ.stats['crit'], 
                        growth = champ.stats['critperlevel'],
                        max_level = level[-1])
    ad = cg.Stat_Growth(base = champ.stats['attackdamage'],
                        growth = champ.stats['attackdamageperlevel'],
                        max_level = level[-1])
    attackspeed = cg.Stat_Growth(base = champ.stats['attackspeed'],
                        growth = champ.stats['attackspeedperlevel'],
                        max_level = level[-1])
        
    [tags.append(tag) for tag in champ.tags if tag not in tags]
    data = data.append(pd.DataFrame(data = [[champ.name,
                                       champ.tags,
                                       hp,
                                       mp,
                                       ms,
                                       armor,
                                       mr,
                                       attackrange,
                                       hpregen,
                                       mpregen,
                                       crit,
                                       ad,
                                       attackspeed]], 
                    index = [champ.name], 
                    columns = ['name',
                               'tags',
                               'hp',
                               'mp',
                               'ms',
                               'armor',
                               'mr',
                               'attackrange',
                               'hpregen',
                               'mpregen',
                               'crit',
                               'ad',
                               'attackspeed']))

print(tags)

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
for index, row in data.iterrows():
    if row['name'] == 'Senna':
        pass
    else:
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

marksman_mean = marksman_mean/mmi
mage_mean = mage_mean/mi
support_mean = support_mean/si
fighter_mean = fighter_mean/fi
tank_mean = tank_mean/ti
assassin_mean = assassin_mean/ai

plt.plot(level,marksman_mean,color='gold',label='Marksman')
plt.plot(level,mage_mean,color='blue',label='Mage')
plt.plot(level,support_mean,color='cyan',label='Support')
plt.plot(level,fighter_mean,color='purple',label='Fighter')
plt.plot(level,tank_mean,color='green',label='Tank')
plt.plot(level,assassin_mean,color='red',label='Assassin')
plt.legend()
plt.grid()
plt.xlim(1, 18)
plt.xlabel('Level')
plt.ylabel(stat)
plt.title('For Patch 10.2')
plt.savefig('figure.png')
plt.show()