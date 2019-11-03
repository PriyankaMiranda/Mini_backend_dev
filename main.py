
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

		level1_choice=request.args.get('filter_1')
		level2_choice=request.args.get('filter_2')
		
		if  level1_choice and not level2_choice:
			choices2=obj.get_options(level1_choice,data)
			return choices2
		if  level2_choice:
			data=obj.filter(level1_choice,level2_choice,data)

	return data



# print(data)

if __name__=="__main__":
    app.run(debug=True)































