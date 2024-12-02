from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from initialization import log
from selenium.common.exceptions import NoSuchElementException
from stop_process import close_chrome
import selenium.webdriver.common.keys
import time

#filling registration form
def fill_form(driver, cust_data):

    log_msg = "register_customer.py: filling registration form..."
    log(log_msg)

    #reseting attepts
    attempts = 0

    while attempts < 3:
        try:

            #navigating to registration form
            links = driver.find_elements("xpath", "//a[@href]")
            for l in links:
                if "Register" in l.get_attribute("innerHTML"):
                    l.click()

                    break
            
            time.sleep(3)

            #entering customer data
            customer_form = driver.find_element(By.ID, 'customerForm')
            first_name = customer_form.find_element(By.NAME, 'customer.firstName')
            first_name.click()
            first_name.clear()
            first_name.send_keys(cust_data['Name'])

            last_name = customer_form.find_element(By.NAME, 'customer.lastName')
            last_name.click()
            last_name.clear()
            last_name.send_keys(cust_data['Lastname'])

            address = customer_form.find_element(By.NAME, 'customer.address.street')
            address.click()
            address.clear()
            address.send_keys(cust_data['Address'])

            city = customer_form.find_element(By.NAME, 'customer.address.city')
            city.click()
            city.clear()
            city.send_keys(cust_data['City'])

            state = customer_form.find_element(By.NAME, 'customer.address.state')
            state.click()
            state.clear()
            state.send_keys(cust_data['State'])

            zip_code = customer_form.find_element(By.NAME, 'customer.address.zipCode')
            zip_code.click()
            zip_code.clear()
            zip_code.send_keys(cust_data['ZIPcode'])

            phone_number = customer_form.find_element(By.NAME, 'customer.phoneNumber')
            phone_number.click()
            phone_number.clear()
            phone_number.send_keys(cust_data['Phone'])

            ssn = customer_form.find_element(By.NAME, 'customer.ssn')
            ssn.click()
            ssn.clear()
            ssn.send_keys(cust_data['SSN'])

            username = customer_form.find_element(By.NAME, 'customer.username')
            username.click()
            username.clear()
            username.send_keys(cust_data['Username'])

            password = customer_form.find_element(By.NAME, 'customer.password')
            password.click()
            password.clear()
            password.send_keys(cust_data['Password'])

            repeat_password = customer_form.find_element(By.NAME, 'repeatedPassword')
            repeat_password.click()
            repeat_password.clear()
            repeat_password.send_keys(cust_data['Password'])

            register_button = customer_form.find_element(By.CLASS_NAME, "button")
            register_button.click()

            time.sleep(3)

            #checking if customer logged in
            cust_name = driver.find_element(By.XPATH, "//div[@id='leftPanel']/p[@class='smallText']").text

            if cust_data['Lastname'] in cust_name:
                log_msg = f'register_customer.py: logged in to {cust_data['Username']}'
                log(log_msg)
                
            
            else:
                error_msg = driver.find_element(By.CLASS_NAME, 'error').text
                log_msg = f'register_customer.py: cannot register {cust_data['Username']} because {error_msg}'
                log(log_msg)

                raise Exception
                
            


            
        #increasing attempt count in case of error
        except:
            attempts += 1

            #in case of 3 unsuccessful attempts - terminate process
            if attempts == 3:
                log_msg = f'register_customer.py: failed to register customer {cust_data['Username']}!'
                log(log_msg)
                close_chrome(driver)
            
            #logging failed attept
            else:
                log_msg = f'register_customer.py: unable to complete registration due to an error. attempt #{attempts}'
                log(log_msg)

                time.sleep(3)

        #logging in case of no error
        else:
            log_msg = f'register_customer.py: registration completed'
            log(log_msg)

            break