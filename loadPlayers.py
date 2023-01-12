import numpy as np 
import nfl_data_py as NFL 
import pandas as pd 
import warnings
from QB import QB
import pickle 
import os


for file in os.listdir('Players/QB'):
    file = 'Players/QB/' + file
    holdQB = QB.load(file)
    print(holdQB.name, holdQB.fantasy_points)