import pandas as pd
import constants
import csv
import json

def __init__(self):
	self.json_data=None

def load_json():
	self.json_data = json.load(open(constants.data_loc+constants.file+'_json.json'))

def csv_to_json():
	df = pd.DataFrame(pd.read_csv(constants.data_loc+constants.file+".csv", sep = constants.csv_file_separator, header = 0, index_col = False))
	df = df.iloc[1:]
	df.to_json (constants.data_loc+constants.file+'_json.json', orient='split')
