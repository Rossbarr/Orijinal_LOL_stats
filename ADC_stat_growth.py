# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Champion_Get import Stat_Growth

stats = pd.read_csv("Marksmen_Stats.csv")

level = np.arange(1,19,1)

#champions = stats['Champion']
champions = ['Xayah','Darius','Sett','Kalista','Aphelios']

for champion in champions:
    AD = Stat_Growth(stats['Attack Damage'][stats['Champion'] == champion],
                     stats['Attack Damage Growth'][stats['Champion'] == champion])
    
    plt.plot(level,AD,label = champion)
    
plt.legend()
plt.grid()
plt.title("Comparison of Champion's Attack Damage")
plt.xlabel('Level')
plt.ylabel('Attack Damage')
plt.xlim(1,18)
plt.ylim(0,150)
# plt.figure(figsize = [10,8])
plt.savefig('ADC_stat_growth.png')
print("Saved file 'ADC_stat_growth.png' to this directory")