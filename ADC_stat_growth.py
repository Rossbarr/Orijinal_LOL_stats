# -*- coding: utf-8 -*-
"""
This file originally dealt with the question of:
"How do champion's stats grow compared to one another? Who scales better than others?"

TO-DO: Refactor to use modules.champion_get function
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from modules.Champion_Get import Stat_Growth

stats = pd.read_csv("data/Marksmen_Stats.csv")

level = np.arange(1,19,1)

#champions = stats['Champion'] # Sees all champions (mostly useless, hard to read)
champions = ['Xayah','Darius','Sett','Kalista','Aphelios'] #Enter champion names to see other champions

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
plt.savefig('figures/ADC_stat_growth.png')
print("Saved file 'ADC_stat_growth.png' under figures/ADC_stat_growth.png")