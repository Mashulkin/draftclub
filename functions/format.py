# -*- coding: utf-8 -*-
"""
Formating data
"""
__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__date__ = '30.08.2023'


def change_type(data):
    new_data = []
    for item in range(len(data)):
        temp = []
        for i in data[item]:
            try:
                temp.append(int(i))
            except ValueError:
                temp.append(i)
        new_data.append(temp)
    
    return new_data
