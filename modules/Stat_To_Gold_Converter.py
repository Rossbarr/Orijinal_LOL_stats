# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:28:04 2020

@author: Barrett

Has a multitude of functions to convert different stats into their gold equivalent value.
"""

def AD_gold_value(ad_amount):
    return ad_amount*35

def AP_gold_value(ap):
    return ap*21.75

def armor_gold_value(armor):
    return armor*20

def MR_gold_value(mr):
    return mr*1

def AS_gold_value(as_amount):
    return as_amount*25

def crit_gold_value(crit_amount):
    return crit_amount*32

def move_speed_gold_value(ms):
    return ms*12

def mana_gold_value(mana):
    return mana*1.4
