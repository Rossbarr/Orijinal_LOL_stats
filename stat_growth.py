# -*- coding: utf-8 -*-
"""
This file originally dealt with the question of:
"How do champion's stats grow compared to one another? Who scales better than others?"

TO-DO: Refactor to use modules.champion_get function
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from modules.Champion_Get import champion_get, Stat_Growth

champs = champion_get('data/champion.json')

level = np.arange(1,19,1)

champions = ['Xayah','Darius','Sett','Kalista','Aphelios'] #Enter champion names to see other champions
# Showing all champions is impossible to read
mask = True
# set to false to show all champions

for index, row in champs.iterrows():
    if index in champions and mask:
        stat = Stat_Growth(row['ad'],
                        row['adperlevel'])
    
        plt.plot(level, stat, label = index)
    
plt.legend()
plt.grid()
plt.title("Comparison of Champion's Attack Damage")
plt.xlabel('Level')
plt.ylabel('Attack Damage')
plt.xlim(1,18)
plt.ylim(0,150)
# plt.figure(figsize = [10,8])
plt.savefig('figures/stat_growth.png')
plt.show()
print("Saved file under figures/stat_growth.png")