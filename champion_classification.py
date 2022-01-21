# -*- coding: utf-8 -*-
"""
@author: Barrett

SVM classifier that classifies champions as either 'Marksman' or not.

TO-DO: update classifier to identify multiple classes, instead of just 2
"""

import modules.Champion_Get as cg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve, accuracy_score

champs = cg.champion_get('data/champion.json')

data = champs.reset_index().drop(columns = ['index', 'tags'])
champ_tags = champs['tags'].reset_index().drop(columns = ['index'])
tags = []

for list_of_tags in champ_tags['tags']:
  if 'Marksman' in list_of_tags:
    tags.append(1)
  else:
    tags.append(0)

data_train, data_test, tags_train, tags_test = train_test_split(data, tags)

clf = svm.SVC()
clf.fit(data_train, tags_train)

tags_pred = clf.predict(data_test)

score = accuracy_score(tags_test, tags_pred)

print("Predicted champion's class (marksman or not) with an accuracy of ", score)