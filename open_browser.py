from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from initialization import log
from stop_process import close_chrome
import time


#opening chrome browser
def open_chrome(parabank_link):

    log_msg = "open_browser.py: opening chrome..."
    log(log_msg)

    #reseting attepts
    attempts = 0

    while attempts < 3:
        try:
            global driver
            options = Options()
            options.add_experimental_option("detach", True)

            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

            driver.get(parabank_link)
            driver.maximize_window()

            time.sleep(3)

        #increasing attempt count in case of error
        except:
            attempts += 1

            #in case of 3 unsuccessful attempts - terminate process
            if attempts == 3:
                
                msg = 'open_browser.py: failed to open chrome!'
                log(msg)
                close_chrome(driver)
            
            #logging failed attept
            else:
                msg = f'open_browser.py: unable to open chrome due to an error. attepmt #{attempts}'
                log(msg)
                time.sleep(3)

        #logging in case of no error
        else:
            log_msg = "open_browser.py: chrome opening is completed"
            log(log_msg)

            return driver

            #break

