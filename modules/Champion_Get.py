# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:41:54 2020

@author: Barrett
"""

import pandas as pd
import numpy as np

def champion_get(fn):
    """
    Accepts a champion json file (fn)
    And turns the relevant information about each champion into a class

    Returns a list of champion classes
    """
    champions = pd.read_json(fn).drop(columns=['type','version','format'])

    data = pd.DataFrame(data = [],
                    index = [],
                    columns = ['tags',
                               'hp',
                               'hpperlevel',
                               'mp',
                               'mpperlevel',
                               'ms',
                               'armor',
                               'armorperlevel',
                               'mr',
                               'mrperlevel',
                               'attackrange',
                               'hpregen',
                               'hpregenperlevel',
                               'mpregen',
                               'mpregenperlevel',
                               'crit',
                               'critperlevel',
                               'ad',
                               'adperlevel',
                               'attackspeed',
                               'attackspeedperlevel'])

    for champ_name, row in champions.iterrows():
        tags = champions.loc[champ_name]['data']['tags']
        hp = champions.loc[champ_name]['data']['stats']['hp']
        hpperlevel = champions.loc[champ_name]['data']['stats']['hpperlevel']
        mp = champions.loc[champ_name]['data']['stats']['mp']
        mpperlevel = champions.loc[champ_name]['data']['stats']['mpperlevel']
        ms = champions.loc[champ_name]['data']['stats']['movespeed']
        armor = champions.loc[champ_name]['data']['stats']['armor']
        armorperlevel = champions.loc[champ_name]['data']['stats']['armorperlevel']
        mr = champions.loc[champ_name]['data']['stats']['spellblock']
        mrperlevel = champions.loc[champ_name]['data']['stats']['spellblockperlevel']
        attackrange = champions.loc[champ_name]['data']['stats']['attackrange']
        hpregen = champions.loc[champ_name]['data']['stats']['hpregen']
        hpregenperlevel = champions.loc[champ_name]['data']['stats']['hpregenperlevel']
        mpregen = champions.loc[champ_name]['data']['stats']['mpregen']
        mpregenperlevel = champions.loc[champ_name]['data']['stats']['mpregenperlevel']
        crit = champions.loc[champ_name]['data']['stats']['crit']
        critperlevel = champions.loc[champ_name]['data']['stats']['critperlevel']
        ad = champions.loc[champ_name]['data']['stats']['attackdamage']
        adperlevel = champions.loc[champ_name]['data']['stats']['attackdamageperlevel']
        attackspeed = champions.loc[champ_name]['data']['stats']['attackspeed']
        attackspeedperlevel = champions.loc[champ_name]['data']['stats']['attackspeedperlevel']

        data = data.append(pd.DataFrame(data = [[
            tags,
            hp,
            hpperlevel,
            mp,
            mpperlevel,
            ms,
            armor,
            armorperlevel,
            mr,
            mrperlevel,
            attackrange,
            hpregen,
            hpregenperlevel,
            mpregen,
            mpregenperlevel,
            crit,
            critperlevel,
            ad,
            adperlevel,
            attackspeed,
            attackspeedperlevel]],
                index = [champ_name],
                columns = ['tags',
                    'hp',
                    'hpperlevel',
                    'mp',
                    'mpperlevel',
                    'ms',
                    'armor',
                    'armorperlevel',
                    'mr',
                    'mrperlevel',
                    'attackrange',
                    'hpregen',
                    'hpregenperlevel',
                    'mpregen',
                    'mpregenperlevel',
                    'crit',
                    'critperlevel',
                    'ad',
                    'adperlevel',
                    'attackspeed',
                    'attackspeedperlevel']))

    return data
        
def Stat_Growth(base, growth, max_level = 18):
    stat = np.zeros(max_level)
    i = 0
    for level in range(max_level):
        stat[i] = base + growth*(level)*(0.7025+0.0175*(level))
        i += 1
    return stat

if __name__ == '__main__':
    champs = champion_get('../data/champion.json')