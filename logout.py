from initialization import log
from stop_process import close_chrome
import time

def log_out(driver):
    
    #resetting attempts
    attempts = 0

    while attempts < 3:
        try:

            log_msg = "logout.py: logging out..."
            log(log_msg)

            links = driver.find_elements('xpath', '//a[@href]')

            #logging out
            for l in links:
                if "Log Out" in l.get_attribute("innerHTML"):
                    l.click()

                    break
                
            time.sleep(3)
            
        except:
            attempts += 1

            if attempts == 3:

                log_msg = 'logout.py: failed to log out!'
                log(log_msg)
                close_chrome(driver)

            #logging failed attept
            else:

                log_msg = f'logout.py: unable to log out due to an error. attepmt #{attempts}'
                log(log_msg)
                time.sleep(3)
        
        else:
            log_msg = f"logout.py: customer logged out"
            log(log_msg)

            break