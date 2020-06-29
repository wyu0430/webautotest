from configparser import ConfigParser

class Read_inifile:

    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read('D:\study\webautotest\config\element.ini', encoding='utf-8')

    # def getItemSection(self, sectionName):
    #     optionDict = dict(self.cf.items(sectionName))
    #     return optionDict

    def getOptionValue(self, sectionName, optionName):
        value = self.cf.get(sectionName, optionName)
        return value

if __name__ == '__main__':
    test = Read_inifile()
    # dict1 = test.getItemSection("login_element")
    # print(dict1)
    value = test.getOptionValue("register_element", "reg_username")
    print(value)