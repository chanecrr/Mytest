import os
import sys
import time
import allure

sys.path.append(os.getcwd())
import pytest
from base.base_yml import yml_data_with_file
from base.base_driver import init_driver
from page.login_page import LogIn

def data_with_key(key):
    return yml_data_with_file("login_data", key)


class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.driver.implicitly_wait(20)
        self.driver.wait_activity("io.dcloud.PandoraEntryActivity", 20)
        self.login_page = LogIn(self.driver)
        time.sleep(8)

    # @pytest.mark.skipif(True, reason="done")
    @allure.step(title="登录模块")
    @pytest.mark.parametrize("args", data_with_key("test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        exist = args["exist"]
        screen = args["screen"]
        title = args["title"]
        # try:
        allure.attach("", "标题：" + title)
        # time.sleep(5)
        # 点击我的
        allure.attach("", "点击我的按钮进入我的页面")
        self.login_page.click_mine()
        # 判断是否登录
        allure.attach("如已登录自动退出登录", "判断是否已登陆")
        self.login_page.judgment_login()
        # 点击登陆注册
        allure.attach("", "点击登陆注册")
        self.login_page.click_login_reg()
        # 输入手机号
        allure.attach("", "输入手机号" + username)
        self.login_page.input_phone_text(username)
        # 输入密码
        allure.attach("", "输入密码" + password)
        self.login_page.input_password_text(password)
        # 点击登录按钮
        allure.attach("", "点击登录按钮")
        self.login_page.click_login_bu()
        allure.attach("", "判断是否成功显示：" + exist)
        if screen == "test_login_006":
            print("进入分支")
            text = self.login_page.find_element(self.login_page.phone_text_view).text
            try:
                assert text == exist
            except Exception:
                self.login_page.screenshot(screen)
                assert False
        else:
            try:
                assert self.login_page.is_toast_exist(exist)
            except Exception:
                self.login_page.screenshot(screen)
                assert False
        self.driver.quit()

    # @pytest.mark.skipif(True, reason="done")
    @allure.step(title="登录-成功退出")
    def test_drop_out(self):
        """登录-成功退出"""
        # time.sleep(5)
        # 点击我的
        allure.attach("", "点击我的按钮进入我的页面")
        self.login_page.click_mine()
        # 判断是否登录如未登录，先完成登录后在做退出操作。
        allure.attach("", "如已登录自动退出登录/未登录先完成登录")
        self.login_page.judgment_login2()
        allure.attach("", "判断是否成功显示：登录或注册")
        assert self.login_page.is_element_exist("登录或注册")
        self.login_page.screenshot("test_drop_out")
        self.driver.quit()
