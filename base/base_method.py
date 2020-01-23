# coding:utf-8
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def background(self, n):
        """将app放置后台N秒"""
        self.driver.background_app(n)

    # 查找元素
    def find_element(self, by, value):
        """如（'id', 'yousyou'）"""
        element = WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element(by, value))
        return element

    # po方法查找
    """
    搜索单个xpath单个条件""test,我的""
    搜索xpath多个条件：["test,我的"，"id,001"]"""

    def find_elementp(self, loc, timeout=10.0, poll=1.0):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)  # //*
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elementsp(self, loc, timeout=10.0, poll=1.0):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)  # //*
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    # 查找多元素
    def find_elements(self, by, value, index):
        """如（'id'， 'youyou'）
        ('xpath','//*[@resource-id="loginOrRegister"]')"""
        element = WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_elements(by, value))
        return element[index]

    # 点击元素
    def click_element(self, by, value):
        click = self.find_element(by, value).click()
        return click

    # po方法点击
    def click(self, loc):
        self.find_elementp(loc).click()

    # 多元素点击
    def click_elements(self, by, value, index):
        element = self.find_elements(by, value, index)
        element.click()

    #  输入内容
    def send_key(self, by, value, text):

        tex = self.find_element(by, value).send_keys(text)
        return tex

    # po方法输入
    def input_text(self, loc, text):
        self.find_elementp(loc).send_keys(text)

    # 多元素输入内容
    def send_keys(self, by, value, index, text):
        tex = self.find_elements(by, value, index).send_keys(text)
        return tex

    # 清除元素
    def clear_ele(self, by, value):
        clear = self.find_element(by, value).clear()
        return clear

    # po方法清空文本框
    def clear_text(self, loc):
        clear = self.find_elementp(loc).clear()
        return clear

    def clear_eles(self, by, value, index):
        clear = self.find_elements(by, value, index).clear()
        return clear

    def is_toast_exist(self, driver, text, timeout=20, poll_frequency=0.5):
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            return True
        except:
            return False

    # 上滑
    def swip_up(self):
        window_size = self.get_window_size()
        width = int(window_size['width'])
        height = int(window_size['height'])
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, duration=500)
        # logger.info("向上滑")

    # 下滑
    def swip_down(self):
        window_size = self.get_window_size()
        width = int(window_size['width'])
        height = int(window_size['height'])
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, duration=500)
        # logger.info("向下滑")

    # 左滑
    def swip_left(self):
        window_size = self.get_window_size()
        width = int(window_size['width'])
        height = int(window_size['height'])
        self.driver.swipe(width * 3 / 4, height / 2, width / 4, height / 2, duration=100)
        # logger.info("向左滑")

    # 右滑
    def swip_right(self):
        window_size = self.get_window_size()
        width = int(window_size['width'])
        height = int(window_size['height'])
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, duration=500)
        # logger.info("向右滑")

    # 获取短信
    def getCodeFromSms(self, timeout=20):
        os.system("adb logcat -c")
        cmd = ' adb logcat -d |findstr D/Mms/Txn'
        n = 0
        while n < timeout:
            smscode = os.popen(cmd).read()
            print(smscode)
            if smscode != " ":
                smscode = smscode.split("验证码:")[1].split(",")[0]
                print("code is {}:".format(smscode))
                break
            else:
                time.sleep(1)
                n += 1
                print('已等待:{}秒'.format(n))
                continue
        print('短信接收失败！')

    # 安装app
    def ins(self, path):
        """:param path: 路径
        """
        self.driver.install_app(path)

    # 卸载app
    def rem(self, packageName):
        """ :param packageName: 包名
        """
        self.driver.remove_app(packageName)

    # ios
    def rem_ios(self, bundleId):
        self.driver.remove_app(bundleId)

    # 关闭app
    def close(self):
        self.driver.close_app()

    # 重置app
    def reset(self):
        self.driver.reset()

    # 隐藏键盘
    def hide_key(self):
        self.driver.hide_keyboard()

    # 安卓有
    def sned_press_key_code(self, keycode):
        self.driver.press_keycode(keycode=keycode)

    # 长按发送
    def long_press_keycode(self, keycode):
        self.driver.long_press_keycode(keycode)

    def current_activity(self):
        activity = self.driver.current_activity()
        return activity

    # def run_back(self, second):
    #     self.driver.background_app(seconds=second)

    # ios需要buildid
    def is_app_installed(self, packagename):
        self.driver.is_app_installed(packagename)

    # 启动app
    def launch_app(self):
        self.driver.launch_app()

    def start_activity(self, app_package, app_activity):
        self.driver.start_activity(app_package, app_activity)

    def ios_lock(self, locktime):
        self.driver.lock(locktime)

    # 安卓api 18以上
    def open_notice(self):
        self.driver.open_notifications()

    # 返回网络
    def renturn_network(self):
        network_type = self.driver.network_connection
        return network_type

    # 设置网络
    def set_network_type(self, type):
        from appium.webdriver.connectiontype import ConnectionType
        if type == 'wifi' or type == 'WIFI' or type == 'w' or type == 'WIFI_ONLY':
            self.driver.set_network_connection(ConnectionType.WIFI_ONLY)
        elif type == 'data' or type == 'DATA' or type == 'd' or type == 'DATA_ONLY':
            self.driver.set_network_connection(ConnectionType.DATA_ONLY)
        elif type == 'ALL' or type == 'all' or type == 'a' or type == 'ALL_NETWORK_ON':
            self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        elif type == 'NO' or type == 'no' or type == 'n' or type == 'NO_CONNECTION':
            self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        elif type == 'AIRPLANE_MODE' or type == 'air' or type == 'ar' or type == 'fly':
            self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
        else:
            raise NameError('plase wifi ,data,all,no,fly')

    # 输入法
    def run_typewriting(self):
        typewriting = self.driver.available_ime_engines
        return typewriting

    def input_active(self):
        check = self.driver.is_ime_active
        return check

    def active_typewriting(self, engine):
        self.driver.activate_ime_engine(engine)

    def close_typewriting(self):
        self.driver.deactivate_ime_engine()

    def return_typewriting(self):
        shurufa_name = self.driver.active_ime_engine
        return shurufa_name

    def open_location(self):
        self.driver.toggle_location_services()

    def set_location(self, latitude, longitude, altitude):
        """:param latitude: 纬度
        :param longitude: 经度
        :param altitude: 海拔
        :return:
        """
        self.driver.set_location(latitude, longitude, altitude)

    def get_size(self):
        size = self.driver.se.size
        return size

    def text(self):
        text = self.driver.text
        return text

    def is_displayed(self, method, path):
        """:param method: 定位方法
        :param path: 方法的具体值
        :return: 该元素是否显示
        """
        el = self.find_element(method, path)
        dis = el.is_displayed()
        return dis

    def screet(self, filename):
        self.driver.get_screenshot_as_base64(filename)

    def close(self):
        self.driver.close_app()

    def quit(self):
        self.driver.quit()

    def screet_wind(self):
        me = self.driver.get_screenshot_as_file()
        return me  # 返回 ture,flase

    # 获取窗口大小
    def get_window_size(self):
        return self.driver.get_window_size()

    # 放大
    def zoom(self, element):
        self.driver.zoom(element)

    # 缩小
    def pinch(self, element):
        self.driver.pinch(element)

    # 从一点到另一点
    def kuaisuhuadong(self, s_x, s_y, e_x, e_y):
        self.driver.flick(s_x, s_y, e_x, e_y)

    # def swipe(self, s_x, s_y, e_x, e_y, duration=None):
    #     self.driver.swipe(s_x, s_y, e_x, e_y)

    def tap(self, x, y, duration=None):
        x1 = x / 1080
        y1 = y / 2280
        screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        self.driver.tap([(x1 * screen_width, y1 * screen_height)], duration=0)

    # 滚动元素
    def scroll(self, x, y):
        self.driver.scroll(x, y)

    # 移动元素
    def drag_and_drop(self, e1, e2):
        self.driver.drag_and_drop(e1, e2)

    # 可用
    def contexts_is(self):
        self.driver.contexts()

    def push(self, data, path):
        self.driver.push_file(data, path)

    def pull(self, path):
        self.driver.pull_file(path)

    def wait(self, second):
        self.driver.wait_activity(second)

    def send_key1(self, pas):
        self.driver.send_keys(pas)

    # 截屏
    def get_screenshot_as_file(self, filename):
        self.driver.get_screenshot_as_file(self, filename)

    # 页面是否包含该元素
    def is_element_exist(self, element, times=1):
        count = 0
        while count < times:
            source = self.driver.page_source
            if element in source:
                return True
            else:
                count += 1
                time.sleep(3)
            return False

    # 允许弹窗
    def always_allow(self, driver, number=5):
        for i in range(number):
            loc = ("xpath", "//*[@resource-id='android:id/button1']")
            try:
                e = WebDriverWait(driver, 1, 0.1).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass

    def back(self):  # 返回
        # self.driver.press_keycode(4)
        self.driver.keyevent(4)

    def find_toast(self, text: object) -> object:  # 判断toast提示信息
        try:
            toast_loc = (By.XPATH, "//*[contains(@text,'" + text + "')]")
            t = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(toast_loc))
            print(t.text)
            return True
        except:
            return False

    def long_press(self, el=None, x=None, y=None):  # 长按发送语音内容

        TouchAction(self.driver).long_press(el).wait(5000).release().perform()

    def clean_text(self, text):
        """清空文本框方法的封装"""
        self.driver.keyevent(123)  # 123代表光标移动到末尾键
        for i in range(0, len(text)):
            self.driver.keyevent(67)  # 67退格键

    def find_eles(self, id):
        """获取到要删除的文本框内容"""
        find_eles = self.driver.find_element_by_id(id)
        find_eles.click()
        return find_eles.get_attribute('text')

    def Deletes(self):
        """删除文本框内容"""
        get_text = self.find_eles()
        self.clean_text(get_text)

    def check_Delete(self):
        '''检查文本框是否删除成功'''
        get_text = self.find_eles()
        if get_text == "":
            print("文本框删除成功")
        else:
            print("文本框删除失败")

    def source(self):
        source = self.driver.page_source
        return source

    def tapele(self, by, value):
        ele = self.find_element(by, value)
        TouchActions(self.driver).tap(ele).perform()

    def swipe_Down(self, t=500, n=1):  # 日期下滑   针对test7请假审批选择日期模块
        l = self.driver.get_window_size()
        print(l)
        x1 = l['width'] * 0.81  # x坐标
        y1 = l['height'] * 0.91  # 起始y坐标
        y2 = l['height'] * 0.82  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def time_Sure(self, x, y, z, t=100, n=1):  # 确定按钮   针对test7请假审批选择日期模块
        l = self.driver.get_window_size()
        x1 = l['width'] * x  # x坐标   0.92=x坐标/分辨率
        y1 = l['height'] * y  # 起始y坐标
        y2 = l['height'] * z  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def make_xpath_with_unit_feature(self, loc):
        """
        拼接xpath中间的部分
        :param loc:
        :return:
        """
        key_index = 0
        value_index = 1
        option_index = 2

        args = loc.split(",")
        feature = ""

        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
        elif len(args) == 3:
            if args[option_index] == "1":
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + "and "
            elif args[option_index] == "0":
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "

        return feature

    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""

        if isinstance(loc, str):
            # 如果是正常的xpath
            if loc.startswith("//"):
                return loc

            # loc str
            feature = self.make_xpath_with_unit_feature(loc)
        else:
            # loc 列表
            for i in loc:
                feature += self.make_xpath_with_unit_feature(i)

        feature = feature.rstrip("and ")

        loc = feature_start + feature + feature_end

        return loc
