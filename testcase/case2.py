import unittest
import sys
sys.path.append('D:\study\webautotest')
from Page.login import Login
import HTMLTestRunner
from util.get_name import Getname
from selenium import webdriver
from util.user_log import UserLog

class Case2(unittest.TestCase):
    def setUp(self):
        log = UserLog()
        self.logging = log.get_log()

        self.driver = webdriver.Chrome()
        self.url = "http://192.168.0.134:9000/ECShop_V2.7.2_UTF8_Release0604/upload66/user.php"

    def tearDown(self):
        self.logging.info("用例执行结束")
        self.driver.quit()

    def test_input_username(self):
        self.logging.info("测试输入用户名")
        login = Login(self.driver,self.url)
        login.input_username("test!@#$%^&&个爱国")


    #
    def test_input_password(self):
        self.logging.info("测试输入密码")
        login = Login(self.driver, self.url)
        login.input_password("!@#$45GHH")
    # #
    def test_loginsuccess(self):
        self.logging.info("测试登录成功")
        login = Login(self.driver, self.url)
        login.login("test13","123456")

if __name__ == '__main__':
    # unittest.main()
    s = unittest.TestSuite()
    s.addTest((Case2('test_input_username')))
    s.addTest((Case2('test_input_password')))
    s.addTest((Case2('test_loginsuccess')))
    getname = Getname()
    filename = getname.get_report_name()
    file = 'D:\\study\\webautotest\\report\\' + filename
    with open(file,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="登录测试报告", description="测试登录功能")
        runner.run(s)

