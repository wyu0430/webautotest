from selenium import webdriver
import time
class Getelement:

    def __init__(self,driver):
        self.driver = driver

    def get_element(self,match,value):
        if match == "id":
            ele = self.driver.find_element_by_id(value)
        elif  match=="name":
            ele = self.driver.find_element_by_name(value)
        elif match == "xpatch":
            ele = self.driver.find_element_by_xpath(value)

        return ele

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://192.168.0.134:9000/ECShop_V2.7.2_UTF8_Release0604/upload66/user.php')
    test = Getelement(driver)
    ele = test.get_element('name',"username")
    print(ele)





