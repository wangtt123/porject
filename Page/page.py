from Page.home_page import Home_Page
from Page.sign_page import Sign_Page
from Page.login_page import Login_Page
from Page.person_page import Person_Page
from Page.setting_page import Setting_Page

class Page:
    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        # 返回主页面对象
        return Home_Page(self.driver)
    def get_sign_page(self):
        # 返回注册页面对象
        return Sign_Page(self.driver)
    def get_login_page(self):
        # 返回登陆页面对象
        return Login_Page(self.driver)
    def get_person_page(self):
        # 返回个人中心页面
        return Person_Page(self.driver)
    def get_setting_page(self):
        # 返回设置页面对象
        return Setting_Page(self.driver)
