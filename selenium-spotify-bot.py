import time

# from selenium import webdriver

# from selenium.webdriver.chrome.service import Service

# service = Service('/path/to/chromedriver')

# service.start()

# driver = webdriver.Remote(service.service_url)

# driver.get('http://www.google.com/');

# time.sleep(60) # Let the user actually see something!

# # driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def get_chrome_driver():
    """This sets up our Chrome Driver and returns it as an object"""
    path_to_chrome = "F:\Selenium_Drivers\Windows_Chrome85_Driver\chromedriver.exe"
    chrome_options = webdriver.ChromeOptions() 
    
    # Keeps the browser open
    chrome_options.add_experimental_option("detach", True)
    
    # Browser is displayed in a custom window size
    chrome_options.add_argument("window-size=1500,1000")
    
    # Removes the "This is being controlled by automation" alert / notification
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    
    return webdriver.Chrome(executable_path = path_to_chrome,
                            options = chrome_options)


# Gets our chrome driver and opens our site
chrome_driver = get_chrome_driver()
chrome_driver.get("https://www.spotify.com/login")
username = chrome_driver.find_element(by=By.ID, value= 'login-username')
username.clear()
username.send_keys("hommeyj7@gmail.com")
time.sleep(1)
password = chrome_driver.find_element(by=By.ID, value= 'login-password')
password.clear()
password.send_keys("Happyfeet@22")
time.sleep(1)
button = chrome_driver.find_element(by=By.ID, value="login-button")
button.click()

time.sleep(2)
chrome_driver.get("https://open.spotify.com/")

# close_cookies = chrome_driver.find_element(by=By.CLASS_NAME, value= 'onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon')
# close_cookies.click() 


print('The browser should not close after you see this message')
chrome_driver.service.stop()