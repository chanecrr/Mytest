import os
import sys
import time
from builtins import range

import allure
from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
import pytest
from base.base_yml import yml_data_with_file
from base.base_driver import init_driver
from page.login_page import LogIn
from page.passenger_mgt_page import Passenger_Mgt_page


def data_with_key(key):
    return yml_data_with_file("passenger_mgt", key)


class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.driver.implicitly_wait(20)
        self.driver.wait_activity("io.dcloud.PandoraEntryActivity", 20)
        time.sleep(8)
        self.login_page = LogIn(self.driver)
        self.passenger_mgt_page = Passenger_Mgt_page(self.driver)

    # @pytest.mark.skipif(True, reason="done")
    @allure.step(title="常用乘客管理-新增-证件类型：身份证")
    @pytest.mark.parametrize("args", data_with_key("text_passenger_mgt01"))
    def test_login(self, args):
        passname = args["passname"]
        passidnum = args["passidnum"]
        phone = args["phone"]
        exist = args["exist"]
        screen = args["screen"]
        title = args["title"]

        allure.attach("", "标题:" + title)
        allure.attach("", "点击我的按钮进入我的页面")
        self.login_page.click_mine()
        allure.attach("", "点击常用乘客管理")
        self.passenger_mgt_page.click_passenger_mgt()
        allure.attach("如已登录不做操作，未登录自动完成登录", "判断是否已登陆")
        self.passenger_mgt_page.judge_longin()
        allure.attach("", "点击新增常用乘客按钮")
        self.passenger_mgt_page.click_new_passenger()
        allure.attach("", "输入姓名：" + passname)
        self.passenger_mgt_page.input_passname(passname)
        allure.attach("", "输入证件号：" + passidnum)
        self.passenger_mgt_page.input_passidnum(passidnum)
        allure.attach("", "输入手机号" + phone)
        self.passenger_mgt_page.input_passenger_phone(phone)
        allure.attach("", "点击保存按钮")
        self.passenger_mgt_page.click_passenger_save()
        allure.attach("如已存在，先完成删除操作，再次进行添加。", "判断-乘客是否已存")
        self.passenger_mgt_page.judge_repeat(passname, "down", passname, passidnum, phone)
        allure.attach("找不到时，进行滑动翻页操作", "查找常用乘客")
        self.passenger_mgt_page.slide_find(passname, "down")
        allure.attach("", "判断是否成功显示：" + exist)
        try:
            assert self.passenger_mgt_page.is_element_exist(exist)
        except Exception:
            self.login_page.screenshot(screen)
            assert False
        self.driver.quit()
