from Base.Base import Base
import Page
class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, name, pwd):
        # 登陆
        # 输入用户名
        self.send_data(Page.login_name_id, name)
        # 输入密码
        self.send_data(Page.login_pwd_id, pwd)
        # 点击登陆按钮
        self.click_element(Page.login_btn_id)

    def if_login_btn(self):
        # 判断登录是否存在 存在返回True 不存在返回False
        try:
            # 定位登录按钮
            self.search_element(Page.login_btn_id)
            return True
        except:
            return False
    def close_login_page(self):
        # 关闭登录按钮
        self.click_element(Page.login_close_page_btn_id)
