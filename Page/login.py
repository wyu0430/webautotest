
from selenium import webdriver
from util.get_element import Getelement
from util.read_elementfile import Read_inifile
from util.get_name import Getname
import time
from util.user_log import UserLog
#
class Login:
    def __init__(self,driver,url):
        self.driver = driver
        self.driver.get(url)
        log = UserLog()
        self.logging = log.get_log()

        self.getele = Getelement(self.driver)
        self.read = Read_inifile()
        self.getname = Getname()

    # def login(self,url):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(url)
    #     self.driver.find_element_by_name("username").send_keys("test13")
    #     self.driver.find_element_by_name("password").send_keys("123456")
    #     self.driver.find_element_by_xpath("font[contains(@class,'f4_b')]").click()


    def input_username(self,username):
        self.logging.info("输入用户名")
        value = self.read.getOptionValue('login_element','username')
        match = value.split(">")[0]
        value = value.split(">")[1]
        ele = self.getele.get_element(match,value)
        ele.send_keys(username)
        filename = self.getname.get_img_name()
        filepath = "D:\\study\\webautotest\\images\\"
        path = filepath + filename
        self.driver.save_screenshot(path)


    def input_password(self,password):
        self.logging.info("输入密码")
        value = self.read.getOptionValue('login_element','password')
        match = value.split(">")[0]
        value = value.split(">")[1]
        ele = self.getele.get_element(match,value)
        ele.send_keys(password)
        filepath = "D:\\study\\webautotest\\images\\"
        filename = self.getname.get_img_name()
        path = filepath + filename
        self.driver.save_screenshot(path)


    def click_login(self):
        value = self.read.getOptionValue('login_element','login_button')
        match = value.split(">")[0]
        value = value.split(">")[1]
        ele = self.getele.get_element(match,value)
        ele.click()


    def login(self,username,password):
        self.logging.info("登录")
        self.input_username(username)
        self.input_password(password)
        self.click_login()
        self.driver.quit()

    def close(self):
        self.driver.quit()




if __name__ == '__main__':
    test =  Login('http://192.168.0.134:9000/ECShop_V2.7.2_UTF8_Release0604/upload66/user.php')
    # test.input_username("test13")
    # test.input_password("123456")
    # test.click_login()
    test.login(username="test13",password="123456")