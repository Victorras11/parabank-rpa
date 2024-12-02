#Importing flows
from initialization import website_link, cust_data, funds_amount
import open_browser
import register_customer
import open_account
import transfer_funds
import logout
import stop_process


#Calling flows
open_browser.open_chrome(website_link)
register_customer.fill_form(open_browser.driver, cust_data)
open_account.new_account(open_browser.driver)
transfer_funds.transfer_founds(open_browser.driver, open_account.acc_num, funds_amount)
logout.log_out(open_browser.driver)
stop_process.close_chrome(open_browser.driver)