
import json
import utils  

from flask import Flask

from flask import request

app = Flask(__name__)
obj=utils.operations()
data_dict={}
obj.csv_to_json()
data=obj.load_json()
data_dict=data

@app.route("/")
def start():
	return data

@app.route("/choices")
def show_level1_choices():
	choices=obj.get_titles(data_dict)
	return choices

@app.route("/operations",methods = ['GET'])
def ops():
	data=obj.load_json()
	if  request.method == 'GET':
		search_query = request.args.get('search') # get query to be searched(number)
		if search_query:
			data= obj.search(search_query,data)

		sort_col = request.args.get('sort')
		if sort_col:
			data=obj.sort(sort_col,data) # get column to be sorted(number)
			print(data)

		level1a_choice=request.args.get('filter_1a')
		level2a_choice=request.args.get('filter_2a')

		if  level1a_choice and not level2a_choice:
			choices2a=obj.get_options(level1a_choice,data)
			return choices2a
		if  level2a_choice:
			data=obj.filter(level1a_choice,level2a_choice,data)

		level1b_choice=request.args.get('filter_1b')
		level2b_choice=request.args.get('filter_2b')

		if  level1b_choice and not level2b_choice:
			choices2b=obj.get_options(level1b_choice,data)
			return choices2b
		if  level2b_choice:
			data=obj.filter(level1b_choice,level2b_choice,data)

		level1c_choice=request.args.get('filter_1c')
		level2c_choice=request.args.get('filter_2c')

		if  level1c_choice and not level2c_choice:
			choices2c=obj.get_options(level1c_choice,data)
			return choices2c
		if  level2c_choice:
			data=obj.filter(level1c_choice,level2c_choice,data)

	return data


if __name__=="__main__":
    app.run(debug=True)































