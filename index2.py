from selenium import webdriver
from getpass import getpass
import time

url = 'https://bit.ly/2vkJ39C'
passw = getpass('Password : ')

driver = webdriver.Chrome('./chromedriver')
driver.get(url)


# def reloadMails(loopTime):
#     x = 1
#     while x == 1:
#         driver.find_element_by_xpath(
#             "//div[@role='button' and data-tooltip='Refresh']"
#         ).click()


username_input = driver.find_element_by_id('identifierId')
next_btn = driver.find_element_by_id('identifierNext')

username_input.send_keys('sarjsk991@gmail.com')
next_btn.click()


# Password

time.sleep(5)
password_input = driver.find_element_by_xpath("//input[@type='password']")
next_btn = driver.find_element_by_id('passwordNext')

password_input.send_keys(passw)
next_btn.click()


time.sleep(15)

# # refrash mail box
# reloadMails(10)

# print('complete')

driver.find_element_by_xpath(
    "//div[@role='button' and text()='Compose']"
).click()


time.sleep(5)

to_input = driver.find_element_by_name('to')
subject_input = driver.find_element_by_name('subjectbox')
message_input = driver.find_element_by_id(':qk')
# attachFile_btn = driver.find_element_by_id(':qx')
send_btn = driver.find_element_by_id(':p5')

to = 'sksarfaraz4006@gmail.com, programworld999@gmail.com'
subject = 'Hello Man'
message = 'This Is A Message Throw By Python'


to_input.send_keys(to)
subject_input.send_keys(subject)
message_input.send_keys(message)

time.sleep(2)
send_btn.click()
