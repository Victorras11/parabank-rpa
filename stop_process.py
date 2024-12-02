from initialization import log

#closing browser
def close_chrome(driver):

    log_msg = 'close_browser.py: closing browser.'
    log(log_msg)

    driver.close()

    log_msg = 'close_browser.py: process stopped, browser closed.'
    log(log_msg)

    exit()