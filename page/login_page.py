import os
import sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LogIn(BaseAction):
    # 我的按钮
    mine_button = By.XPATH, "//android.view.View[@text=' 我的']"
    # 登录注册按钮
    login_reg = By.XPATH, "//android.view.View[@resource-id='loginOrRegister']"
    # 手机号文本框
    phone_text_view = By.XPATH, "//android.widget.EditText[@resource-id='username']"
    # 密码文本框
    password_text_view = By.XPATH, "//android.widget.EditText[@resource-id='password']"
    # 登录按钮
    login_bu = By.XPATH, "//android.view.View[@resource-id='login' and @text='登 录']"
    # 退出按钮
    login_out = By.XPATH, "//android.view.View[@resource-id='loginOut']"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        # self.click_mine()

    #   点击我的按钮
    def click_mine(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.driver.find_element(self.display_button[0], self.display_button[1]).click()
        # self.find_element(self.display_button).click()
        self.click(self.mine_button)

    # 点击登录注册按钮
    def click_login_reg(self):
        self.click(self.login_reg)

    # 输入手机号
    def input_phone_text(self, phone):
        self.input_text(self.phone_text_view, phone)

    # 清空手机号文本框
    def clear_phone_text(self):
        self.clear_text(self.phone_text_view)

    # 输入密码
    def input_password_text(self, password):
        self.input_text(self.password_text_view, password)

    # 清空密码文本框
    def clear_password_text(self):
        self.clear_text(self.password_text_view)

    # 点击登录按钮
    def click_login_bu(self):
        self.click(self.login_bu)

    # 点击退出按钮
    def click_login_out(self):
        self.click(self.login_out)

    # 查看登陆状态（检查未登录）
    def judgment_login(self):
        while True:
            result = self.find_element(self.login_reg).text
            if result in "登录或注册":
                # print("未登录状态")
                break
            else:
                self.click_login_reg()
                self.click_login_out()

    # 查看登陆状态（检查已登录）
    def judgment_login2(self):
        while True:
            result = self.find_element(self.login_reg).text
            if result not in "登录或注册":
                self.click_login_reg()
                self.click_login_out()
                break
            else:
                self.click_login_reg()
                self.input_phone_text("13366691616")
                self.input_password_text("123456aa")
                self.click_login_bu()
