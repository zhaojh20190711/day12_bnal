import allure

from page.page_address import PageAddress
from page.page_login import PageLogin
from tool.get_driver import GetDriver


class PageIn:

    def __init__(self):
        self.driver = GetDriver.get_driver()

    # 获取PageLogin对象
    @allure.step(title='正在获取PageLogin对象')
    def page_get_PageLogin(self):
        return PageLogin(self.driver)

    # 获取PageAddress对象
    @allure.step(title='正在获取PageAddress对象')
    def page_get_PageAddress(self):
        return PageAddress(self.driver)
