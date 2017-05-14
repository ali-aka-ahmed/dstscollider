import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



__author__ = 'Ali'


class CookieManagerTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get('http://twitter.com/login')
        driver = self.driver

        username_or_email_xpath = '//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input'
        password_xpath = '//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input'
        login_button_xpath = '//*[@id="page-container"]/div/div[1]/form/div[2]/button'

        username_or_email = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(username_or_email_xpath))
        password = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(password_xpath))
        login_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(login_button_xpath))

        username_or_email.clear()
        username_or_email.send_keys(twitter_username)
        password.clear()
        password.send_keys(twitter_password)

        login_button.click()

        driver.maximize_window()

    def test(self):
        driver = self.driver
        listcookies = driver.get_cookies()

        for s_cookie in listcookies:
            # this is what you are doing
            c = {s_cookie['name']: s_cookie['value']}
            print("*****The partial cookie info you are doing*****\n")
            print(c)
            # Should be done
            print("The Full Cookie including domain and expiry info\n")
            print(s_cookie)
            # driver.add_cookie(s_cookie)


    def tearDown(self):
        self.driver.quit()



twitter_username = input("Twitter Username:")
twitter_password = input("Twitter Password:")

t1 = CookieManagerTest()
t1.setUp()
t1.test()
t1.tearDown()

print("if no twitter cookies are displayed, username and password were wrong. Also check texts - if twitter sends you one they're suspicious that we're using script. If you recieve one then you have to login with the code they give you and run this again.")