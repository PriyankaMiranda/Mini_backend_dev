import csv
import json
import os.path
import utils  

def main():

	obj=utils.operations()

	obj.csv_to_json()

	# initialize with all data
	data=obj.load_json()
	choices=obj.get_titles(data)

	data = obj.search(input(),data	)
	print(data)
	print(choices)

	data=obj.sort(choices[int(input())],data)
	
	print(data)
	print("Filtering")
	print(choices)

	level1_choice=choices[int(input())]
	choices2=obj.get_options(level1_choice,data)
	print(choices2)
	level2_choice=choices2[int(input())]
	data=obj.filter(level1_choice,level2_choice,data)

	print(data)

if __name__=="__main__":
	main()