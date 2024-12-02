from datetime import datetime
import json
import logging

#loading json file with defined paths and customer data
with open('config.json', 'r') as f:
    config = json.load(f)

#assigning variables
paths = config['data']['paths']
log_file = paths['LogFile']
website_link = paths['Parabank']
cust_data = config['data']['Customer']
funds = config['data']['Funds']
funds_amount = funds['Amount']

#creating logging
def log(log_msg):
    day = str(datetime.today().strftime('%Y-%m-%d'))
    
    day = str(datetime.today().strftime('%Y-%m-%d'))
    logging.basicConfig(filename=log_file + day + '.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    logging.info(log_msg)

#logging process
log_msg = "------------------------"
log(log_msg)

log_msg = "initialization.py: initialization completed"
log(log_msg)