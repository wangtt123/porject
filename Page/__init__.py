from selenium.webdriver.common.by import By
"""
    主页面
"""
# 我
my_btn_id = (By.ID, "com.yunmall.lc:id/tab_me")
"""
    注册页面
"""
# 已有账户，去登陆
exits_account_id = (By.ID, "com.yunmall.lc:id/textView1")
"""
    登陆页面
"""
# 用户名
login_name_id = (By.ID, "com.yunmall.lc:id/logon_account_textview")
# 密码
login_pwd_id = (By.ID, "com.yunmall.lc:id/logon_password_textview")
# 登陆按钮
login_btn_id= (By.ID, "com.yunmall.lc:id/logon_button")
# 关闭登录按钮
login_close_page_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
"""
    个人中心页
"""
# 我的优惠券
my_coupons_id = (By.ID, "com.yunmall.lc:id/txt_my_coupons")
# 设置
setting_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
"""
    设置页面
"""
# 退出按钮
logout_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")
# 确认退出按钮
acc_logout_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")