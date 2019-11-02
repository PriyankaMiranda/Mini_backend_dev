import csv
import json
import os.path



import utils

def main():
	file=utils.read_csv()
	print(type(file))
	print(file)

if __name__=="__main__":
	main()