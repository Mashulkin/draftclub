# -*- coding: utf-8 -*-
"""
Calculating data
"""
import pandas as pd

from simple_settings import settings


__author__ = 'Vadim Arsenev'
__version__ = '1.0.3'
__date__ = '03.09.2023'


def calculate(players, teams):
    df = pd.DataFrame()
    for item in range(len(teams)):
        # points for coach
        coach_team = teams[item][-1]
        coach_points = players.loc[(players['Abbr'] == coach_team) & (players['st'] == 0) \
                                    & (players['min'] > 0), 'points'].sum()
        coach_played = len(players.loc[(players['Abbr'] == coach_team) & (players['st'] > 0)])
        coach_finished = len(players.loc[(players['Abbr'] == coach_team) & (players['st'] == 1) \
                                    & (players['min'] == 90)])
        if coach_played == 0:
            coach_status = f'+ {coach_team}'
        elif coach_finished > 3:
            coach_status = ''
        else:
            coach_status = f'{coach_points}*'

        # point for sub
        team_points = players.loc[players['id'].isin(teams[item][0:-2]), 'points'].sum() \
            + coach_points
        sub_points = players.loc[players['id'] == teams[item][-2], 'points'].sum()
        sub_position = players[players['id'] == teams[item][-2]].iloc[0]['Pos']
        sub_team = players[players['id'] == teams[item][-2]].iloc[0]['Abbr']
        sub_team_finished = len(players.loc[(players['Abbr'] == sub_team) \
                                & (players['st'] == 1) & (players['min'] == 90)])

        # count_def = len(players.loc[players['id'].isin(teams[item][0:-2]) \
        #             & (players['Pos'] == 'D')])
        # count_mid = len(players.loc[players['id'].isin(teams[item][0:-2]) \
        #             & (players['Pos'] == 'M')])
        # count_for = len(players.loc[players['id'].isin(teams[item][0:-2]) \
        #             & (players['Pos'] == 'F')])
        # print(f'{count_def}-{count_mid}-{count_for}')

        players_no_finished = len(players.loc[players['id'].isin(teams[item][0:-2]) \
                    & (players['min'] == 0) & (players['Pos'] != 'GK')])
        # no_finished_def = len(players.loc[players['id'].isin(teams[item][0:-2]) \
        #             & (players['min'] == 0) & (players['Pos'] == 'D')])
        # no_finished_mid = len(players.loc[players['id'].isin(teams[item][0:-2]) \
        #             & (players['min'] == 0) & (players['Pos'] == 'M')])
        # no_finished_for = len(players.loc[players['id'].isin(teams[item][0:-2]) \
        #             & (players['min'] == 0) & (players['Pos'] == 'F')])
        
        if players_no_finished == 0:
            sub_points = ''
        elif sub_team_finished > 3:
            sub_points = sub_points
        else:
            sub_points = '+'
        
        bonus = players.loc[players['id'].isin(teams[item][0:-2]), 'bonus'].sum()

        # counting finished, active and remaining players
        count_not_played, count_in_play, count_finished = [0] * 3       
        for id in teams[item][1:-2]:
            try:
                player_team = players[players['id'] == id].iloc[0]['Abbr']
            except IndexError:
                continue
            player_played = len(players.loc[(players['Abbr'] == player_team) & (players['st'] > 0)])
            player_team_finished = len(players.loc[(players['Abbr'] == player_team) \
                                    & (players['st'] == 1) & (players['min'] == 90)])
            if player_played == 0:
                count_not_played += 1
            elif player_team_finished > 3:
                count_finished += 1
            else:
                count_in_play += 1

        df_temp = pd.DataFrame([[teams[item][0], int(team_points), count_finished, count_in_play, \
                    count_not_played, coach_status, sub_points, bonus]], columns=settings.COLUMNS)
        df = pd.concat([df, df_temp], ignore_index=True)
    df = df.sort_values(by=['Points'], ascending=False)
    
    return df
