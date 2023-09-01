# -*- coding: utf-8 -*-
"""
Reading data
"""
import csv
import pandas as pd


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '01.09.2023'


def read_data(filename):
    players_data = (pd.read_csv(filename, encoding='utf-8')
                      .reset_index(drop=True)
    )

    return players_data


def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
    
    return data


def save_csv(filename, data):
    data.to_csv(filename, index=False)
