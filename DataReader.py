__author__ == 'michaeltong'

import os.path
import pandas

GNRL_CSV_PATH_2013 = './general_2013.csv' 
# just 2013 general data for now

categories = [3, 10, 11, 12, 16, 17, 30, 31, 32, 37, 38, 46] 
#only take some of the categories: optional
#use pandas.read_csv(usecols = categories) keyword


class GeneralReader():
   
    def __init__(self):
    	self.get_cms_dataframe()

    def get_cms_dataframe(self):
    	'''Read from the relevant csv file if it exists

    	:return: sets self.cms_lookup equal to the dataframe
    	:rtype: None
    	'''

    	if not os.path.exists(GNRL_CSV_PATH_2013)
        self.cms_lookup = pandas.read_csv(CSV_PATH, quotechar='"', quoting=csv.QUOTE_ALL)

