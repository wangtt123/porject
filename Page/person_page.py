from Base.Base import Base
import Page
class Person_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def get_coupons_text(self):
        # 返回优惠券文本内容
        return self.search_element(Page.my_coupons_id).text

    def click_setting(self):
        # 点击设置按钮
        self.click_element(Page.setting_btn_id)