###
### AUTOGRADER TEST - DO NOT REMOVE
###

#from testing_tools import ...
import pandas as pd
import numpy as np
import sqlite3
from scipy.sparse import coo_matrix
import importlib
#import run_tests
import pickle
import time
#import geopandas as gpd

# Demo cell - run this cell before moving on.
conn = sqlite3.connect('resource/asnlib/publicdata/data.db')
pd.read_sql_query('''
    SELECT * 
    FROM indiv_contrib 
    ORDER BY random() limit 10
''', conn)