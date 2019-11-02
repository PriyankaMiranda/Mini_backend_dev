import pandas as pd
import constants
import csv
import json

def read_csv():
	df = pd.DataFrame(pd.read_csv(constants.data_loc+constants.file+".csv", sep = constants.csv_file_separator, header = 0, index_col = False))
	# df.to_json(constants.data_loc+constants.file+'_json.json', orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
	df = df.iloc[1:]
	df.to_json (constants.data_loc+constants.file+'_json.json', orient='split')

	print(df)
	return df


def get_header():
	print("Getting header")
	file = pd.read_csv('details.csv')
	return list(file.head(0))


def csv_to_json():
	csvfile = open(constants.data_loc+constants.file+".csv", 'r')
	jsonfile = open(constants.data_loc+constants.file+'_json.json', 'w')

	fieldnames = ("FirstName","LastName","IDNumber","Message")
	jsonfile.write(out)