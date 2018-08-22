from Base.Base import Base
import Page
class Setting_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def logot(self, tag=1):
        """
        退出操作
        :param tag: 1 确认退出  2 取消
        :return:
        """
        # 向上滑动
        self.screen_scroll(tag=2)
        # 点击退出
        self.click_element(Page.logout_btn_id)
        # 判断tag =1 确认退出
        if tag == 1:
            self.click_element(Page.acc_logout_btn_id)

