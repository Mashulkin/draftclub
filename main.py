# -*- coding: utf-8 -*-
"""
Getting price players on gaffr
"""
import addpath
from simple_settings import settings

from common_modules.my_remove import remove_file

from functions.teams import calculate
from functions.files import read_data, read_csv, save_csv
from functions.format import change_type


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '01.09.2023'


def main():
    """
    General request
    """
    players = read_data(settings.ONLINE_PLAYERS)
    teams = change_type(read_csv(settings.FANTASY_TEAMS))
    onlineTable = calculate(players, teams)
    save_csv(settings.ONLINE_TABLE, onlineTable)


if __name__ == '__main__':
    main()
