import sys, os

sys.path.append(os.getcwd())

from Page.page import Page
from Base.get_driver import get_driver
from Base.get_data import Get_Data
import pytest


def cup_data():
    data_list = []
    yml_data = Get_Data('login_data.yml').return_yaml_data()
    for i in yml_data.keys():
        data_list.append((i, yml_data.get(i).get("username"), yml_data.get(i).get("password"),
                          yml_data.get(i).get("expect_message"), yml_data.get(i).get("tag"),
                          yml_data.get(i).get("toast_ms")))
    return data_list


class Test_Login:
    def setup_class(self):
        # 实例化统一入口类
        self.page_obj = Page(get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))

    def teardown_class(self):
        # 退出driver
        self.page_obj.driver.quit()

    @pytest.mark.parametrize("test_num,username,password,expect_message,tag,toast_ms", cup_data())
    def test_login(self, test_num, username, password, expect_message, tag, toast_ms):
        """
        :param test_num: 用例编号
        :param username: 用户名
        :param password: 密码
        :param expect_message: 预期结果
        :param toast_ms: toast消息获取文本
        :return:
        """
        # 点击我
        self.page_obj.get_home_page().click_my_btn()
        # 点击已有账户 去登陆
        self.page_obj.get_sign_page().click_exit_account()
        # 登陆操作
        self.page_obj.get_login_page().login(username, password)
        # 断言
        if tag:
            # 执行预期成功
            try:
                # 获取我的优惠券
                coupons_text = self.page_obj.get_person_page().get_coupons_text()
                assert expect_message == coupons_text
                # 点击设置按钮
                self.page_obj.get_person_page().click_setting()
                # 执行退出登录
                self.page_obj.get_setting_page().logot()
            except:
                # 关闭登陆页面
                self.page_obj.get_login_page().close_login_page()
                assert False
        else:
            try:
                # 执行预期失败
                # 获取toast消息
                toast_message = self.page_obj.get_person_page().get_toast(toast_ms)
                # 判断登录是否存在
                login_if_exit = self.page_obj.get_login_page().if_login_btn()
                # 断言
                assert login_if_exit and expect_message == toast_message
            finally:
                # 关闭登陆页面
                self.page_obj.get_login_page().close_login_page()
