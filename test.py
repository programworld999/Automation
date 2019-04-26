from selenium import webdriver
from getpass import getpass
import time

url = 'http://127.0.0.1:5500/test.html'

driver = webdriver.Chrome('./chromedriver')
driver.get(url)

btn = driver.find_element_by_id('')
btn = btn.
btn.click()
