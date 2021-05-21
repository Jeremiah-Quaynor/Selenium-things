from selenium import webdriver
import time

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get("https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html")
assert "Selenium Easy - Best Demo website for Bootstrap Date picker" in chrome_browser.title

time.sleep(2)
# close_ad_button = chrome_browser.find_element_by_id('at-cv-lightbox-close')
# if close_ad_button:
#     close_ad_button.click()

# just selecting on date
date_button=chrome_browser.find_element_by_xpath('//*[@id="sandbox-container1"]/div/span/i')
date_button.click()
time.sleep(1)
today_button = chrome_browser.find_element_by_xpath('/html/body/div[3]/div[1]/table/tfoot/tr[1]/th')
today_button.click()
time.sleep(2)
date_button.click()
time.sleep(1)
clear_button=chrome_browser.find_element_by_xpath('/html/body/div[3]/div[1]/table/tfoot/tr[2]/th')
clear_button.click()
time.sleep(1)

#for selecting date range
date_space1 = chrome_browser.find_element_by_xpath('//*[@id="datepicker"]/input[1]')
date_space1.click()
time.sleep(2)
date1 = chrome_browser.find_element_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr[3]/td[3]')
date1.click()
date_space2 = chrome_browser.find_element_by_xpath('//*[@id="datepicker"]/input[2]')
date_space2.click()
time.sleep(2)
dateee = chrome_browser.find_element_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr[4]/td[6]')
dateee.click()

chrome_browser.close()