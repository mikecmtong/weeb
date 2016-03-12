__author__ = 'michaeltong'

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

    	if not os.path.exists(GNRL_CSV_PATH_2013):
    		raise FileNotFoundError('The .csv file was not found in %s' % GNRL_CSV_PATH_2013)
    	else:
        	self.cms_lookup = pandas.read_csv(CSV_PATH, quotechar='"', quoting=csv.QUOTE_ALL, usecols=categories)

    def read(self, geo, params):
    	'''
    	Queries the cms dataframe
    	:param geo: geographic filters, possibilities are city, state, zipcode. Use * for any.
    	e.g. geo = {'city': 'Cleveland', 'state': 'OH', 'zipcode': '*'}
    	:type geo: dict
    	:param params: other filters. Not supported yet
    	:type params: dict
    	'''

        search = ''

    	if 'city' in geo:
    		geo['city'] = string.upper(geo['city'])
    	else:
    		geo['city'] = '*'

    	if 'state' not in geo:
    		geo['state'] = '*'


    	if 'zipcode' in geo and geo['zipcode'] != '*':
    		geo['zipcode'] = geo['zipcode'][0:5]   #set 5 letter zipcode
    	else:
    		geo['zipcode'] = '*'

    	for param in geo.keys():
    		if geo[param] != '*':
    			search += "%s == '%s' " %(param, geo[param])
    			search += 'and '

    	if len(search) > 0:
    		return df.query(search[-4])
    	else:
    		return df
