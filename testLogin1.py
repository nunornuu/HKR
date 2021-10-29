# 成功测试

import unittest
from selenium import webdriver
from ddt import ddt, data, unpack
from time import sleep
from data import success


@ddt
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/HKR/')
        self.driver.maximize_window()

    def tearDown(self) -> None:
        sleep(4)
        self.driver.quit()

    @data(*success)
    @unpack
    def test_login_success(self, name, password, expect):
        self.driver.find_element_by_xpath('//*[@id = "loginname"]').send_keys(name)
        self.driver.find_element_by_xpath('//*[@id = "password"]').send_keys(password)
        self.driver.find_element_by_id('submit').click()
        sleep(5)
        result = self.driver.title

        self.assertEqual(expect, result)



