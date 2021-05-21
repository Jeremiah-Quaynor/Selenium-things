from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/javascript-alert-box-demo.html')
assert 'Selenium Easy Demo - Automate All Scenarios' in driver.title


#first button
time.sleep(1)
buttoon = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/button')
buttoon.click()
time.sleep(2)
driver.switch_to_alert().accept()

#alert with 'ok' and 'cancel'
time.sleep(1)
next_button = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button')
next_button.click()
time.sleep(2)
driver.switch_to_alert().accept()
time.sleep(2)
next_button.click()
time.sleep(2)
driver.switch_to_alert().dismiss()

third_button = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[3]/div[2]/button')
third_button.click()
time.sleep(2)
driver.switch_to_alert().send_keys('Jeremiah Quaynor')
time.sleep(1)
driver.switch_to_alert().accept()




