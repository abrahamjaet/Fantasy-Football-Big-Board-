import numpy as np 
import nfl_data_py as NFL 
import pandas as pd 
import warnings
from QB import QB
import pickle 


warnings.filterwarnings("ignore") 


year = [2022]

# get seasonal data and rosters
data = NFL.import_seasonal_data(year)
rosters = NFL.import_rosters(year)


# ids of players who achieved a stat in 2021 season 
playerID = data.player_id
rosters = rosters[rosters['player_id'].isin(playerID)]
data.set_index('player_id',inplace=True)
rosters = rosters[['season','team','position','status',
'player_name','height','weight','college','player_id','years_exp','headshot_url']]


################## groupby position ##################

## QB ## 
qbs = rosters.groupby("position").get_group('QB')
qbs.set_index('player_id',inplace = True) # get QBs from roster
qbs.sort_index(axis=0)
qbID = qbs.index # QB player ID from rosters 
qbsData = data[data.index.isin(qbID)] # get qb stats from data 
qbsData.sort_index(axis=0)
qbsData = qbsData[qbsData.passing_yards > 2000] # only qbs with more than 2000 passing yards 
qbs = qbs[qbs.index.isin(qbsData.index)]

listQB  = []

for ind in qbs.index: 
    
    season = qbs['season'][ind]
    team = qbs['team'][ind]
    name = qbs['player_name'][ind]
    position = qbs['position'][ind]
    status =  qbs['status'][ind]
    height = qbs['height'][ind]
    weight = qbs['weight'][ind]
    college = qbs['college'][ind]
    player_id = ind
    years_exp = qbs['years_exp'][ind]
    headshot_url = qbs['headshot_url'][ind]
    qbRankWins = 0
    
    # qbdata 
    season_type = qbsData['season_type'][ind]
    completions = qbsData['completions'][ind]
    attempts = qbsData['attempts'][ind]
    passing_yards = qbsData['passing_yards'][ind]
    passing_tds = qbsData['passing_tds'][ind]
    interceptions = qbsData['interceptions'][ind]
    sacks = qbsData['sacks'][ind]
    sack_yards = qbsData['sack_yards'][ind]
    sack_fumbles = qbsData['sack_fumbles'][ind]
    sack_fumbles_lost = qbsData['sack_fumbles_lost'][ind]
    passing_air_yards = qbsData['passing_air_yards'][ind]
    passing_yards_after_catch = qbsData['passing_yards_after_catch'][ind]
    passing_first_downs = qbsData['passing_first_downs'][ind]
    passing_epa = qbsData['passing_epa'][ind]
    passing_2pt_conversions = qbsData['passing_2pt_conversions'][ind]
    pacr = qbsData['pacr'][ind]
    carries = qbsData['carries'][ind]
    rushing_yards = qbsData['rushing_yards'][ind]
    rushing_tds = qbsData['rushing_tds'][ind]
    rushing_fumbles = qbsData['rushing_fumbles'][ind]
    rushing_fumbles_lost = qbsData['rushing_fumbles_lost'][ind]
    rushing_first_downs = qbsData['rushing_first_downs'][ind]
    rushing_epa = qbsData['rushing_epa'][ind]
    rushing_2pt_conversions = qbsData['rushing_2pt_conversions'][ind]
    fantasy_points = qbsData['fantasy_points'][ind]
    fantasy_points_ppr = qbsData['fantasy_points_ppr'][ind]
    games = qbsData['games'][ind]

    filename = 'Players/QB/' + name + '.dat'
    qbHold = QB(season,team,name,position,status,height,weight,college, player_id,years_exp, headshot_url,qbRankWins, season_type, 
        completions, attempts, passing_yards,
        passing_tds, interceptions, sacks, sack_yards, sack_fumbles,
        sack_fumbles_lost, passing_air_yards, passing_yards_after_catch,
        passing_first_downs, passing_epa, passing_2pt_conversions, pacr, carries, rushing_yards, rushing_tds, rushing_fumbles,
        rushing_fumbles_lost, rushing_first_downs, rushing_epa,
        rushing_2pt_conversions,  fantasy_points, fantasy_points_ppr, games)
    qbHold.save(filename)
    
