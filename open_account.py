from selenium.webdriver.common.by import By
from initialization import log
from stop_process import close_chrome
import time

#opening new account
def new_account(driver):
    
    global acc_num
    
    #reseting attepts
    attempts = 0

    while attempts < 3:
        try:

            log_msg = "open_account.py: opening new account..."
            log(log_msg)

            #navigating to "open new account" page
            links = driver.find_elements('xpath', '//a[@href]')

            for l in links:
                    if "Open New Account" in l.get_attribute("innerHTML"):
                        l.click()

                        break
            
            time.sleep(3)

            form = driver.find_element(By.ID, 'openAccountForm')
            button = form.find_element(By.CLASS_NAME, 'button')
            
            time.sleep(2)

            button.click()

            time.sleep(3)

            select_account = driver.find_elements('xpath', '//a[@id="newAccountId"]')

            for value in select_account:
                acc_num = value.text

            time.sleep(2)

            
        #increasing attempt count in case of error
        except:
            attempts += 1

            #in case of 3 unsuccessful attempts - terminate process
            if attempts == 3:
                
                log_msg = 'open_account.py: failed to open account'
                log(log_msg)
                close_chrome(driver)

            #logging failed attept
            else:

                log_msg = f'open_account.py:: unable to open account due to an error. attepmt #{attempts}'
                log(log_msg)
                time.sleep(3)

        #logging in case of no error
        else:
            log_msg = f"open_account.py: account {acc_num} opened successfully"
            log(log_msg)
            return acc_num

            break
                    
        