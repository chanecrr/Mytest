from appium import webdriver

def init_driver():
    # server 启动参数
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    # desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = '127.0.0.1:62001'
    # desired_caps['deviceName'] = '930c1fe7'
    # app信息
    desired_caps['appPackage'] = 'io.dcloud.H5A6DF4A7'
    desired_caps['appActivity'] = 'io.dcloud.PandoraEntry'
    #toast
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['noReset'] = True
    # 中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
