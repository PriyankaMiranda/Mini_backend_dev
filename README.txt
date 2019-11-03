* Folder structure
	--main folder
	 -main.py
	 -utils.py
	 -constants.py
	 --dataset
	  -csv_file.csv
*
* Ensure the system has python 3.6. Install virtualenv and install all the 
* requirements in the requirements.txt file 
* Use command - pip3 install -r requirements.txt
* 
* The constants file consists of the dataset location
* It also consists of the columns to be removed and searched among
* For datasets at different locations, change the location of the dataset in contants.py
*
* The utils file consists of all the necessary computations broken down into smaller modules.
* 
* Since front end is not developed, please use postman for the GET methods to function accordingly
* Running the code.
* 1) Open terminal in the main folder and run script - python3 main.py
* 2) Open postaman and go to the local host address provided
* 3) Operations to be performed- a) search b) sort c) filter
*    Go to host_address/operations
* 	 For searching, set variable 'search' to the query		
*    For sorting, set variable 'sort' to one of the column headers.
*	 To know the names of the headers, go to host_address/choices
*	 For filtering, set variable 'filter_1' to one of the column headers.
*    After this, you will be shown the options you can select aamong in the column for filtering
*    Set 'filter_2' as one of these values to get results.
