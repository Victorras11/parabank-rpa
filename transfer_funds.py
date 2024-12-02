from selenium.webdriver.common.by import By
from initialization import log
from stop_process import close_chrome
import time

#transfering funds
def transfer_founds(driver, acc_num, funds_amount):

    #resetting attempts
    attempts = 0

    while attempts < 3:
        try:
            log_msg = "transfer_funds.py: transfering funds..."
            log(log_msg)

            links = driver.find_elements('xpath', '//a[@href]')

            #navigating to "transfer funds" page
            for l in links:
                if "Transfer Funds" in l.get_attribute("innerHTML"):
                    l.click()

                    break

            time.sleep(2)
            #entering transfer amount
            transfer_form = driver.find_element(By.ID, 'transferForm')
            amount = transfer_form.find_element(By.ID, 'amount')
            amount.click()
            amount.clear()
            amount.send_keys(funds_amount)

            time.sleep(2)

            #selecting new account
            select_account = driver.find_elements('xpath', f'//form/div/select[@id="toAccountId"]/option[@value="{acc_num}"]')

            for option in select_account:
                if acc_num in option.get_attribute('innerHTML'):
                    option.click()

                    break
            
            time.sleep(2)

            #sending money
            transfer_button = driver.find_element(By.XPATH, "//input[@value='Transfer']")
            transfer_button.click()

            time.sleep(3)

        #increasing attempt count in case of error
        except:
            attempts += 1

            if attempts == 3:

                log_msg = 'transfer_funds.py: failed to transfer!'
                log(log_msg)
                close_chrome(driver)

            #logging failed attept
            else:

                log_msg = f'transfer_funds.py: unable to transfer due to an error. attepmt #{attempts}'
                log(log_msg)
                time.sleep(3)
        
        else:
            log_msg = f"transfer_funds.py: transaction completed. {funds_amount}$ was successfully sent to {acc_num}"
            log(log_msg)

            break