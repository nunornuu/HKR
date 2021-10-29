from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://localhost:8080/HKR/')
driver.maximize_window()

driver.find_element_by_xpath('//*[@id = "loginname"]').send_keys('jason')
driver.find_element_by_xpath('//*[@id = "password"]').send_keys('1234567')
driver.find_element_by_id('submit').click()
sleep(5)
result = driver.title
if result != 'Student Login':
    driver.save_screenshot('error.png')

driver.find_element_by_id('img').click()
driver.find_element_by_xpath('//li[@title = "小海豹"]').click()
sleep(4)
input('*** quit ***')
driver.quit()



