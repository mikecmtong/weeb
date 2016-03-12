__author__ = 'michaeltong'

import os.path
import pandas
import csv
import string

GNRL_CSV_PATH_2013 = './general_2013.csv' 
# just 2013 general data for now

categories = [3, 10, 11, 12, 28] 
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
        	self.cms_lookup = pandas.read_csv(GNRL_CSV_PATH_2013, quotechar='"', quoting=csv.QUOTE_ALL, usecols=categories)

    def get_geo_filters(self, geo, translate):
    	search = ''
    	if 'city' in geo:
    		geo['city'] = string.upper(geo['city'])


    	if 'zipcode' in geo:
    		geo['zipcode'] = geo['zipcode'][0:5]   #set 5 number zipcode

    	for param in geo.keys():
    		if geo[param] != '*':
    			search += "%s == '%s' and " %(translate[param], geo[param])
    	return search

    def get_params_filters(self, params, translate):
    	search = ''
    	if 'minamt' in params and params['minamt'] != '*':
    		search += "%s >= %.2f and " %(translate['amt'], float(params['minamt']))

    	if 'maxamt' in params and params['maxamt'] != '*':
    		search += "%s <= %.2f and " %(translate['amt'], float(params['maxamt']))
    	return search

    def read(self, geo, params):
    	'''
    	Queries the cms dataframe
    	:param geo: geographic filters, possibilities are city, state, zipcode. Use * for any.
    	e.g. geo = {'city': 'Cleveland', 'state': 'OH', 'zipcode': '*'}
    	:type geo: dict
    	:param params: other filters. minamt, maxamt. Use * for any.
    	:type params: dict
    	'''

        search = ''
        translate = {'city': 'Recipient_City', 'state': 'Recipient_State', 'zipcode': 'Recipient_Zip_Code', \
        'amt': 'Total_Amount_of_Payment_USDollars'}

        #geo params
        search += self.get_geo_filters(geo, translate)
    	
    	#other params

    	search += self.get_params_filters(params, translate)

        print search[:-4]

    	if len(search) > 0:
    		return self.cms_lookup.query(search[:-4])  #[:-4] gets rid of last "and"
    	else:
    		return self.cms_lookup
