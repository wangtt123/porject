from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class Base:

    def __init__(self, driver):
        self.driver = driver
        self.screen_size = self.driver.get_window_size()
    def search_element(self, loc, timeout=15, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 定位方式 类型元祖  (By.ID,id_value) (By.CLASS_NAME,class_value)(By.xpath,xpath_value)
        :param timeout: 超时时间
        :param poll_frequency: 搜索间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def search_elements(self, loc, timeout=15, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 定位方式 类型元祖  (By.ID,id_value) (By.CLASS_NAME,class_value)(By.xpath,xpath_value)
        :param timeout: 超时时间
        :param poll_frequency: 搜索间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=15, poll_frequency=1):
        """
        点击元素
        :param loc: 定位方式 类型元祖  (By.ID,id_value) (By.CLASS_NAME,class_value)(By.xpath,xpath_value)
        :param timeout: 超时时间
        :param poll_frequency: 搜索间隔
        :return:
        """
        self.search_element(loc, timeout, poll_frequency).click()

    def send_data(self, loc, text, timeout=15, poll_frequency=1):
        """
        点击元素
        :param loc: 定位方式 类型元祖  (By.ID,id_value) (By.CLASS_NAME,class_value)(By.xpath,xpath_value)
        :param timeout: 超时时间
        :param poll_frequency: 搜索间隔
        :param text: 输入文本
        :return:
        """
        input_text = self.search_element(loc, timeout, poll_frequency)
        input_text.clear()
        input_text.send_keys(text)

    def screen_scroll(self, tag=1):
        """
        滑动屏幕
        :param tag: 1：向下滑动 2：向上滑动 3：向左滑动 4： 向右滑动
        :return:
        """
        sleep(2) # 防止屏幕未跳转

        if tag == 1:
            self.driver.swipe(self.screen_size.get("width")*0.5, self.screen_size.get("height")*0.3,
                              self.screen_size.get("width") * 0.5, self.screen_size.get("height") * 0.8)
        if tag == 2:
            self.driver.swipe(self.screen_size.get("width") * 0.5, self.screen_size.get("height") * 0.8,
                              self.screen_size.get("width") * 0.5, self.screen_size.get("height") * 0.3)
        if tag == 3:
            self.driver.swipe(self.screen_size.get("width") * 0.8, self.screen_size.get("height") * 0.5,
                              self.screen_size.get("width") * 0.3, self.screen_size.get("height") * 0.5)
        if tag == 4:
            self.driver.swipe(self.screen_size.get("width") * 0.3, self.screen_size.get("height") * 0.5,
                              self.screen_size.get("width") * 0.8, self.screen_size.get("height") * 0.5)

    def get_toast(self, mes):
        """
        获取toast消息
        :param mes: 传入部分值
        :return:
        """
        xpath_value = "//*[contains(@text,'{}')]".format(mes)

        return self.search_element((By.XPATH, xpath_value), timeout=5, poll_frequency=0.1).text