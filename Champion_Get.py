# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:41:54 2020

@author: Barrett
"""

import pandas as pd
import numpy as np

def champion_get():
    """
    Reads the local champion.json file
    And turns the relevant information about each champion into a class

    Returns a list of champion classes for each class
    """
    champions = pd.read_json('champion.json').drop(columns=['type','version','format'])
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