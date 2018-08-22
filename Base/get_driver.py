
from appium import webdriver


def get_driver(pac, act):
    """

    :param pac: 包名
    :param act: 启动名
    :return: driver对象
    """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.53.101:5555'
    desired_caps['appPackage'] = pac
    desired_caps['appActivity'] = act
    # 获取toast消息
    desired_caps['automationName'] = 'Uiautomator2'
    # 设置输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
