import os
import sys
import time

sys.path.append(os.getcwd())
from appium import webdriver
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from page.login_page import LogIn


class Passenger_Mgt_page(LogIn):
    # 常用乘客管理
    passenger_mgt = By.XPATH, "//android.view.View[@text='常用乘客管理']"
    # 新增常用乘客
    new_passenger = By.XPATH, "//android.view.View[@resource-id='addPassenger']"
    # 保存按钮
    passenger_save = By.XPATH, "//android.view.View[@resource-id='save']"
    # 姓名
    passName = By.XPATH, "//android.widget.EditText[@resource-id='passName']"
    # 证件类型
    passIDType = By.XPATH, "//android.widget.EditText[@resource-id='passIDType']"
    # 证件号
    passIDNum = By.XPATH, "//android.widget.EditText[@resource-id='passIDNum']"
    # 手机号
    passenger_phone = By.XPATH, "//android.widget.EditText[@resource-id='passPhone']"
    # 删除按钮
    passenger_deletepass = By.XPATH, "//android.view.View[@resource-id='deletepass']"
    # 删除中的确认按钮
    confirm_button = By.XPATH, "//android.widget.Button[@resource-id='android:id/button3']"

    # 点击常用乘客管理
    def click_passenger_mgt(self):
        self.click(self.passenger_mgt)

    # 判断是否已登录，如未登录自动完成登录
    def judge_longin(self):
        try:
            self.find_element(self.new_passenger, 3, 1)
            # self.find_element(self.phone_text_view, 4, 1)
            # self.input_phone_text("13366691616")
            # self.input_password_text("123456aa")
            # self.click_login_bu()
            # self.click_passenger_mgt()
        except Exception:
            self.input_phone_text("13366691616")
            self.input_password_text("123456aa")
            self.click_login_bu()
            time.sleep(2)
            self.click_passenger_mgt()

    # 点击新增常用乘客
    def click_new_passenger(self):
        self.click(self.new_passenger)

    # 点击保存按钮
    def click_passenger_save(self):
        self.click(self.passenger_save)

    # 点击删除按钮
    def click_passenger_deletepass(self):
        self.click(self.passenger_deletepass)

    #  点击确认删除按钮
    def click_confirm_button(self):
        self.click(self.confirm_button)

    # 滑动查找乘客
    def slide_find(self, text, direction):
        i = 0
        while i <= 2:
            result = self.is_toast_exist(text, 2, 0.5)
            # print(result)
            if result == True:
                break
            else:
                self.scroll_page_one_time(direction)
            i += 1

    # 输入姓名
    def input_passname(self, text):
        self.input_text(self.passName, text)

    # 选择证件类型：身份证
    # 选择证件类型：护照
    # 选择证件类型：回乡证
    # 选择证件类型：台胞证

    # 输入证件号
    def input_passidnum(self, text):
        self.input_text(self.passIDNum, text)

    # 输入手机号
    def input_passenger_phone(self, text):
        self.input_text(self.passenger_phone, text)

    def judge_repeat(self, text, direction, passname, passidnum, passenger_phone):
        judge = self.is_toast_exist("已存在乘车人信息")
        if judge == True:
            self.driver.back()
            self.slide_find(text, direction)
            self.find_element((By.XPATH, "//android.view.View[@text='%s']" % text)).click()
            self.click_passenger_deletepass()
            self.click_confirm_button()
            self.click_new_passenger()
            self.input_passname(passname)
            self.input_passidnum(passidnum)
            self.input_passenger_phone(passenger_phone)
            self.click_passenger_save()
