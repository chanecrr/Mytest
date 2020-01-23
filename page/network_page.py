import os, sys

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())

from base.base_action import BaseAction


class NetworkPage(BaseAction):

    more_button = By.XPATH, "//*[contains(@text,'更多')]"

    network_button = By.XPATH, "//*[contains(@text,'移动网络')]"

    # 首选网络类型
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    # 2g按钮
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    # 3g按钮
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    def click_more(self):
        self.click(self.more_button)

    def click_network(self):
        self.click(self.network_button)


    def click_first_network(self):
        self.click(self.first_network_button)

    def click_2g_network(self):
        self.click(self.network_2g_button)

    def click_3g_network(self):
        self.click(self.network_3g_button)

    def get_side_menu_book_marks(self):
        book_marks = self.find_elements(self.side_menu_book_mark)
        book_mark_list = list()
        for i in book_marks:
            book_mark_list.append(i.text)
        return book_mark_list