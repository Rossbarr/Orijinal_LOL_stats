# -*- coding: utf-8 -*-
"""
@author: Barrett
"""

import Champion_Get as cg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn import svm
from sklearn.model_selection import train_test_split

champs = cg.champion_get()

level = np.arange(1,19,1)

names = pd.DataFrame(data = [],
                    index = [],
                    columns = ['name'])
tags = pd.DataFrame(data = [],
                    index = [],
                    columns = ['tags'])
data = pd.DataFrame(data = [],
                    index = [],
                    columns = ['hp',
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

i = 0
tag = 0
for champ in champs:
    if 'Marksman' in champ.tags or 'Tank' in champ.tags:
        if 'Marksman' in champ.tags:
          tag = 1
        else:
          tag = 0
        hp = champ.stats['hp']
        hpperlevel = champ.stats['hpperlevel']
        mp = champ.stats['mp']
        mpperlevel = champ.stats['mpperlevel']
        ms = champ.stats['movespeed']
        armor = champ.stats['armor']
        armorperlevel = champ.stats['armorperlevel']
        mr = champ.stats['spellblock']
        mrperlevel = champ.stats['spellblockperlevel']
        attackrange = champ.stats['attackrange']
        hpregen = champ.stats['hpregen']
        hpregenperlevel = champ.stats['hpregenperlevel']
        mpregen = champ.stats['mpregen']
        mpregenperlevel = champ.stats['mpregenperlevel']
        crit = champ.stats['crit']
        critperlevel = champ.stats['critperlevel']
        ad = champ.stats['attackdamage']
        adperlevel = champ.stats['attackdamageperlevel']
        attackspeed = champ.stats['attackspeed']
        attackspeedperlevel = champ.stats['attackspeedperlevel']
            
        names = names.append(pd.DataFrame(data = [[champ.name]],
                                          index = [i],
                                          columns = ['name']))
        tags = tags.append(pd.DataFrame(data = [tag],
                                        index = [i],
                                        columns = ['tags']))
        data = data.append(pd.DataFrame(data = [[
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
                        index = [i],
                        columns = ['hp',
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
        i += 1

data_train, data_test, tags_train, tags_test = train_test_split(data, tags.values.ravel().astype((int)))

clf = svm.SVC()
clf.fit(data_train, tags_train)

clf.predict(data_test)