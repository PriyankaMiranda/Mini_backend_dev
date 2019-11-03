import csv
import json
import os.path
import utils  

def main():
	obj=utils.operations()
	obj.csv_to_json()
	obj.load_json()
	obj.search(input())




if __name__=="__main__":
	main()