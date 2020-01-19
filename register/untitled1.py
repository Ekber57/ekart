# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:08:23 2020

@author: CompMedic
"""
import re
def seria_yoxla(v):
    p="[^a-z]+"
    check = re.search("^[0][5|7][7|5|1|0][0-9]{7}",v)
    if check:
        if len(v) == 13:
            return True
        else:
            return False
    else:
        return False

