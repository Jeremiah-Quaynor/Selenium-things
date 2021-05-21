from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
assert 'Selenium Easy - Checkbox demo for automation using selenium' in driver.title

#SELECTING one CHECKBOX

checkbox= driver.find_element_by_id('isAgeSelected')
checkbox.click()
time.sleep(2)
# message = driver.find_element_by_id('txtAge')
# assert 'Check box is chcked' in message.text

#SELECTING MANY CHECKBOXES
multply_checkbox= driver.find_element_by_xpath('//*[@id="check1"]')
multply_checkbox.click()
time.sleep(2)

onecheckbox = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[3]/label/input')
onecheckbox.click()
time.sleep(1)


