from HTMLTestRunner import HTMLTestRunner
import unittest
import os
from threading import Thread


class LoginThread(Thread):
    def __init__(self, test_file, html_file):
        super().__init__()
        self.test_file = test_file
        self.html_file = html_file

    def run(self) -> None:
        runner = HTMLTestRunner.HTMLTestRunner(
            verbosity=1,
            title='登录测试',
            description='',
            stream=open(f'{self.html_file}', mode='w', encoding='utf-8')
        )

        runner.run(unittest.defaultTestLoader.discover(os.getcwd(), pattern=f'{self.test_file}'))


if __name__ == '__main__':

    login_s = LoginThread('testLogin1.py', '成功.html')
    login_f = LoginThread('testLogin2.py', '失败.html')

    login_f.start()
    login_s.start()
    login_s.join()
    login_f.join()


