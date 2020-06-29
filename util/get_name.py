import time

class Getname:
    def __init__(self):
        self.time_fromat  = time.strftime("%Y%m%d%H%M%S")


    def get_img_name(self):

        fimename = self.time_fromat + ".png"
        return fimename


    def get_report_name(self):
        fimename = self.time_fromat + "testReport.html"
        return fimename

    def get_logger_name(self):
        fimename = self.time_fromat + ".log"
        return fimename

if __name__ == '__main__':
    test = Getname()
    test.get_img_name()
    print(test.get_img_name())
    print(test.get_report_name())
    print(test.get_logger_name())
