from selenium import webdriver
from getpass import getpass
import time


username = input('Enter User Name : ')
password = getpass('Enter Password : ')


driver = webdriver.Chrome('./chromedriver')
driver.get('https://facebook.com')

username_input = driver.find_element_by_id('email')
password_input = driver.find_element_by_id('pass')
login_btn = driver.find_element_by_id('loginbutton')

username_input.send_keys(username)
password_input.send_keys(password)
login_btn.submit()
