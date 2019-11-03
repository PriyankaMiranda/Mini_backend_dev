import pandas as pd
import constants
import csv
import json
class operations:
	def __init__(self):
		self.json_data=None

	def load_json(self):
		return json.load(open(constants.data_loc+constants.file+'_json.json'))

	# Converting to json
	def csv_to_json(self):
		df = pd.DataFrame(pd.read_csv(constants.data_loc+constants.file+".csv", sep = constants.csv_file_separator, header = 0, index_col = False))
		df=self.remove_cols(df)
		df.to_json(constants.data_loc+constants.file+'_json.json', orient='columns')

	def get_titles(self,data):
		try:
			df = pd.DataFrame.from_dict(data, orient='columns')
			df = self.remove_spaces(df)
			return {k: 0 for k in df.columns.values}
		except:
			return {}

	def get_options(self,choice,data):
		if(data and choice):
			df = pd.DataFrame.from_dict(data, orient='columns')
			df = self.remove_spaces(df)
			return dict(enumerate(df[choice].unique()))
		else:
			return {0:0}

	def remove_spaces(self, df):
		redo_header=[x.strip(' ') for x in list(df.columns.values)]
		df.columns = redo_header
		return df

	def remove_cols(self, df):
		df = df.iloc[1:]# removing second column
		df = df.iloc[:-1]# removing last column
		df = self.remove_spaces(df)
		df.drop(constants.remove_cols, axis=1, inplace=True)
		return df

	def search(self, text, data):	
		if(data and text):
			df = pd.DataFrame.from_dict(data, orient='columns')
			df = self.remove_spaces(df)
			df3 = pd.DataFrame(columns=df.columns.values)
			for elem in constants.search_cols:
				df2=df[(df[elem] == text)]
				df3=pd.concat([df3,df2], axis=0)
			return df3.to_dict()
		else:
			return {0:0}

	def sort(self, title, data):
		if (title and data):
			df = pd.DataFrame.from_dict(data, orient='columns')
			df = self.remove_spaces(df)
			return df.sort_values(by=[title], ascending=True).to_dict()
		else:
			return {0:0}

	def filter(self,elem, inside_choice,data):
		df = pd.DataFrame.from_dict(data, orient='columns')
		df = self.remove_spaces(df)
		df=df[(df[elem] == inside_choice)]
		return df.to_dict()
