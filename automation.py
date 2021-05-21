from selenium import webdriver
import time


chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in chrome_browser.title

time.sleep(2)
#for annoying ad:
close_ad_button = chrome_browser.find_element_by_xpath('//*[@id="at-cv-lightbox-close"]')
if close_ad_button:
    close_ad_button.click()

show_message_button = chrome_browser.find_element_by_xpath('//*[@id="get-input"]/button')
print(show_message_button.get_attribute('innerHMTL'))
# assert 'Show Messsage' in chrome_browser.page_source

user_message  = chrome_browser.find_element_by_id("user-message")
user_message.clear()

user_message.send_keys('I AM EXTRA COOL')
show_message_button.click()

display_message = chrome_browser.find_element_by_id("display")

assert 'I AM EXTRA COOL' in display_message.text

chrome_browser.close()