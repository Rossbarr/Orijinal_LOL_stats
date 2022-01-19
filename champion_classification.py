# -*- coding: utf-8 -*-
"""
@author: Barrett
"""

import modules.Champion_Get as cg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve, accuracy_score

data = cg.champion_get('data/champion.json')


# data_train, data_test, tags_train, tags_test = train_test_split(data, tags.values.ravel().astype((int)))

# clf = svm.SVC()
# clf.fit(data_train, tags_train)

# tags_pred = clf.predict(data_test)

# score = accuracy_score(tags_test, tags_pred)

# print("Predicted champion's class (tank or marksman) with an accuracy of ", score)