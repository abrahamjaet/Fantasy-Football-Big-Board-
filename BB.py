import numpy as np 
import nfl_data_py as NFL 
import pandas as pd 
import warnings
from QB import QB

def showLevel1(obj1, obj2):
    print(obj1.name,end=' vs ')
    print(obj2.name)
    print(obj1.team,end=' Team ')
    print(obj2.team)

    choice = int(input('Who would you rather have everything else equal? (input 1 or 2)\n'))
    print('\n')
    return choice 

warnings.filterwarnings("ignore") 


year = [2022]

# get seasonal data and rosters
data = NFL.import_seasonal_data(year)
rosters = NFL.import_rosters(year)

# ids of players who achieved a stat in 2021 season 
playerID = list(data.player_id)

rosters = rosters[['season','team','position','status',
'player_name','height','weight','college','player_id','years_exp','headshot_url']]


################## groupby position ##################

## QB ## 
qbs = rosters.groupby("position").get_group('QB') # get QBs from roster
qbsName = qbs[['player_name']]  # QB names 
qbID = qbs.player_id # QB player ID from rosters 
qbsData = data[data["player_id"].isin(qbID)] # get qb stats from data 
qbsData = qbsData[qbsData.passing_air_yards > 2000] # only qbs with more than 2000 passing yards 
qbID = qbsData.player_id # player ids for qbs that meet the above constraint 
qbs = qbs[qbs["player_id"].isin(qbID)] # get qbs from roster  

listQB  = []

for ind in qbs.index: 
    
    season = rosters['season'][ind]
    team = rosters['team'][ind]
    name = rosters['player_name'][ind]
    position = rosters['position'][ind]
    status =  rosters['status'][ind]
    player_name = rosters['player_name'][ind]
    height = rosters['height'][ind]
    weight = rosters['weight'][ind]
    college = rosters['college'][ind]
    player_id = rosters['player_id'][ind]
    years_exp = rosters['years_exp'][ind]
    headshot_url = rosters['headshot_url'][ind]
    qbHold = QB(season,team,name,position,status,player_name,height,weight,college, player_id,years_exp, headshot_url,0 )
    listQB.append(qbHold)
   
numQB = len(listQB)


################## Ranking  V0 ################ 

## Success! but really slow and tedious. Brute force method 
## amount of inputs by user needed are nCr = 528 (working on it)

testQB = listQB
for i in range(len(testQB)):
    holdQB1 = testQB[i]
    for j in range(i+1,len(testQB)):
        holdQB2 = testQB[j]
        choice = showLevel1(holdQB1, holdQB2)
        if choice == 1: 
            # holdQB1 must be ranked higher than holdQB2 
            testQB[i].qbRankWins = testQB[i].qbRankWins + 1 
            #print(holdQB1.name, testQB[i].qbRankWins, holdQB2.name, testQB[j].qbRankWins)
             
        else:  
            testQB[j].qbRankWins = testQB[j].qbRankWins + 1 

            #print(holdQB1.name, testQB[i].qbRankWins, holdQB2.name, testQB[j].qbRankWins)


testQB.sort(key = lambda x: x.qbRankWins,reverse=True)
print('Rankings:')
for j in range(len(testQB)):
    print(j+1, testQB[j].name)


