# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:41:54 2020

@author: Barrett
"""

import pandas as pd
import numpy as np

def champion_get():
    champions = pd.read_json('C:/Users/Barrett/Documents/League of Legends Stats/dragontail-10.2.1/dragontail-10.2.1/10.2.1/data/en_US/champion.json').drop(columns=['type','version','format'])
    print('THIS IS FOR PATCH 10.2.1')
    champs = []
    for champ_name, row in champions.iterrows():
        globals()[champ_name] = champion()
        globals()[champ_name].get_stats(champ_name, champions)
        champs.append(globals()[champ_name])

    return champs

class champion():
    def get_stats(self, champ_name, champions):
        self.name = champ_name
        self.key = champions.loc[champ_name]['data']['key']
        self.stats = champions.loc[champ_name]['data']['stats']
        self.tags = champions.loc[champ_name]['data']['tags']
        self.partype = champions.loc[champ_name]['data']['partype']
        
def Stat_Growth(base, growth, max_level = 18):
    stat = np.zeros(max_level)
    i = 0
    for level in range(max_level):
        stat[i] = base + growth*(level)*(0.7025+0.0175*(level))
        i += 1
    return stat

if __name__ == '__main__':
    champs = champion_get()