import sys
import time
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import re
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dcap = dict(webdriver.DesiredCapabilities.PHANTOMJS)
dcap[
    "phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.maximize_window()

driver.get('http://twitter.com/')
driver.delete_all_cookies()

# add cookies

# driver.add_cookie({
#FILL IN
#})

driver.add_cookie({
#FILL IN
    })
driver.add_cookie({
#FILL IN
})
driver.add_cookie({
#FILL IN
})
driver.add_cookie({
#FILL IN
})
driver.add_cookie({
#FILL IN
})
driver.add_cookie({
#FILL IN
})
driver.add_cookie({
#FILL IN
})
driver.add_cookie({
#FILL IN
})
driver.add_cookie({
#FILL IN
})

screen_name = sys.argv[1]
base_url = "https://twitter.com/"
url = base_url + '{}'.format(screen_name) + "/followers"

driver.get(url)

wait = WebDriverWait(driver, 5, poll_frequency=0.1)



class wait_for_more_than_n_elements_to_be_present(object):

    def __init__(self, locator, count):
        self.locator = locator
        self.count = count

    def __call__(self, driver):
        try:
            elements = EC._find_elements(driver, self.locator)
            return len(elements) > self.count
        except StaleElementReferenceException:
            return False

num_followers = int(driver.find_element_by_xpath(
    '//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span[2]').text)
followers = []
max_panes = math.ceil(num_followers / 6)
curr_panes = 3
#loads 3 panes of 6 followers each (batches of 18)
#18 to begin with
# Grid Grid--withGutter starts with 7 but actually 3
while True:
	followers += [driver.find_element_by_xpath('//*[@id="page-container"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div[' + str(curr_panes) + ']')]
	driver.execute_script("arguments[0].scrollIntoView();", followers[-1])
	try:
		wait.until(wait_for_more_than_n_elements_to_be_present((By.XPATH, '//*[@id="page-container"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div['+ str(curr_panes) + ']'), max_panes))
		curr_panes += 3
	except TimeoutException:
		break

# pg = 0
# while True:
#     if pg == 25:
#         break

#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     try:
#         print(wait.until(wait_for_more_than_n_elements_to_be_present(
#             (By.TAG_NAME, 'a'), 50)))
#         pg += 1
#     except TimeoutException:
#     	break





# class wait_for_display(object):

#     def __init__(self, locator):
#         self.locator = locator

#     def __call__(self, driver):
#         try:
#             element = EC._find_element(driver, self.locator)
#             print(element.get_attribute("data-min-position"))
#             return element.get_attribute("data-min-position") != 0
#         except StaleElementReferenceException:
#             return False

# wait = WebDriverWait(driver, 5, poll_frequency=0.1)
# wait.until(wait_for_display(
#     (By.XPATH, '//*[@id="page-container"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]')))



links = driver.find_elements_by_tag_name('a')

for l in links:
    print(l.get_attribute('class') + "//" + l.text)
    print('\n')



# for _ in range(5):
#     driver.execute_script("window.scrollTo(0, 0)")
#     driver.execute_script("arguments[0].scrollIntoView(true);", tweets[-1])
#     time.sleep(0.5)

# page_source = driver.page_source
# driver.close()

# soup = BeautifulSoup(page_source, 'lxml')
# i = 1
# for f in soup.find_all('a'):
# 	print(str(i) + ": ")
# 	if f.string:
# 		print(f.string)
# 	print('\n')
# 	i+=1

    # ProfileCard-screennameLink u-linkComplex js-nav
    # fullname ProfileNameTruncated-link u-textInheritColor js-nav


# import argparse
# import mechanicalsoup
# from getpass import getpass

# from robobrowser import RoboBrowser

# #Opens browser
# browser = RoboBrowser(history=True)
# browser.open('http://twitter.com/login')

# #Retrieves form
# form = browser.get_form(class_='t1-form clearfix signin js-signin')

# # Fill out login form
# form['session[username_or_email]'].value = 'ali.aka.ahmed@gmail.com'
# form['session[password]'].value = 'Berkatores19'

# # Submit the login form
# browser.submit_form(form)

# #uses entered argument
# screen_name = sys.argv[1]
# base_url = "https://twitter.com/"
# url = base_url + '{}'.format(screen_name) + "/followers"
# browser.open(url)

# # attrs={'class': lambda L: 'ProfileNameTruncated-link' in L.split() if L else False}
# # strainer = SoupStrainer(search) #attrs=attrs
# soup = BeautifulSoup(open('search.html','r'), "lxml") #browser.parsed

# follower_handle = []
# follower_name = []

# ###################################################################
# # div1 = soup.find("div", {"id":"doc"})
# # div2 = div1.find("div", {"id":"page-outer"})
# # div3 = div2.find("div", {"id":"page-container"})
# # div4 = div3.find("div", {"class":"AppContainer"})
# # print(div4.prettify())
# # div5 = div4.find("div", {"class":"AppContent-main content-main u-cf"})
# # div6 = div5.find("div", {"class":"Grid Grid--withGutter"})
# # div7 = div6.find("div", {"class":"Grid-cell u-size2of3 u-lg-size3of4"})
# # div8 = div7.find("div", {"class":"Grid Grid--withGutter"})
# # div9 = div8.find("div", {"class":"Grid-cell"})
# # div10 = div9.find("div", {"class":"GridTimeline"})
# # div11 = div10.find("div", {"class":"GridTimeline-items has-items"})
# # for div12 in div11.find_all("div", {"class":"Grid Grid--withGutter"}):
# # 	for div13 in div12.find_all("div", {"class":"Grid-cell u-size1of2 u-lg-size1of3 u-mb10"}):
# # 		for div14 in div13.find_all("div", {"class":"js-stream-item"}):
# # 			for div15 in div14.find_all("div", {"class":"ProfileCard js-actionable-user"}):
# # 				for div16 in div15.find_all("div", {"class":"ProfileCard-content"}):
# # 					for div17 in div16.find_all("div", {"class":"ProfileCard-userFields"}):
# # 						div18 = div17.find("div")
# # 						div19 = div18.find("div")
# # 						link = div19.find("a")
# # 						follower_handle += [link.get('href')]
# # 						follower_name += [link.string]
# ####################################################################

# for follower in soup.find_all('a'):
#     print(follower)

# print(soup.prettify())


# from bs4 import BeautifulSoup
# import requests
# username='justinbieber'
# url = 'https://www.twitter.com/'+username
# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'lxml')

# f = soup.find_all('li', class_="ProfileNav-item--followers")
# title = f.find_all('a')['title']
# print(f)
# # 81,346,708 Followers

# num_followers = int(title.split(' ')[0].replace(',',''))
# print(num_followers)
# # 81346708
