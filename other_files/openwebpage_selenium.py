import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.PhantomJS()

driver.get('http://twitter.com/login')

username_or_email_xpath = '//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input'
password_xpath = '//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input'
login_button_xpath = '//*[@id="page-container"]/div/div[1]/form/div[2]/button'

username_or_email = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(username_or_email_xpath))
password = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(password_xpath))
login_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(login_button_xpath))

username_or_email.clear()
username_or_email.send_keys(input("Twitter username"))
password.clear()
password.send_keys(input("Twitter password"))

login_button.click()

screen_name = sys.argv[1]
base_url = "https://twitter.com/"
url = base_url + '{}'.format(screen_name) + "/followers"

driver.get(url)