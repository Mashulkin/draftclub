# -*- coding: utf-8 -*-
"""
Calculating data
"""
import pandas as pd

from simple_settings import settings


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '01.09.2023'


def calculate(players, teams):
    df = pd.DataFrame()
    for item in range(len(teams)):
        couch = teams[item][-1]
        couch_points = players.loc[(players['Abbr'] == couch) & (players['st'] == 0) \
                                   & (players['min'] > 0), 'points'].sum()
        couch_game = len(players.loc[(players['Abbr'] == couch) & (players['st'] > 0)])
        if couch_game == 0:
            couch_game = '+ couch'
        else:
            couch_game = ''

        players_no_games = len(players.loc[players['id'].isin(teams[item][0:-2]) \
                    & (players['st'] == 0) & (players['min'] == 0) & (players['Pos'] != 'GK')])
        if players_no_games == 0:
            player_points = players.loc[players['id'].isin(teams[item][0:-2]), 'points'].sum() \
                + couch_points
        else:
            player_points = players.loc[players['id'].isin(teams[item][0:-1]), 'points'].sum() \
                + couch_points
        
        count_players_in = len(players.loc[players['id'].isin(teams[item][0:-2]) \
                    & (players['min'] > 0)])

        df_temp = pd.DataFrame([[teams[item][0], int(player_points), 11-int(count_players_in), \
                    couch_game]], columns=settings.COLUMNS)
        df = pd.concat([df, df_temp], ignore_index=True)
    df = df.sort_values(by=['points'], ascending=False)
    
    return df
