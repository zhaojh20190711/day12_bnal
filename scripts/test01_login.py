import os
import sys



sys.path.append(os.getcwd())
import allure

from tool.read_yaml import read_yaml
import pytest
from page.page_in import PageIn
from tool.get_driver import GetDriver


def get_data():
    arrs = []
    for arr in read_yaml("login.yaml").values():
        arrs.append(tuple(arr.values()))
    return arrs


class TestLogin():
    # 初始化
    def setup_class(self):
        # 获取PageLogin对象
        self.pagein = PageIn()
        # 调用登录
        self.login = self.pagein.page_get_PageLogin()
        # 点击我
        self.login.page_click_me()
        # 点击已有账号去登录
        self.login.page_click_account_link()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_driver()

    # 登录测试方法
    @pytest.mark.parametrize("username, pwd, nickname, expect_toast", get_data())
    def test_login(self, username, pwd, nickname, expect_toast):
        # 调用登录业务方法
        self.login.page_login(username, pwd)
        # 如果是正向
        if nickname:
            try:
                # 断言 昵称
                assert nickname == self.login.page_get_nickname()
            except:
                # 截图
                self.login.base_get_img()
            finally:
                # 退出登录
                self.login.page_logout()
                # 点击 我
                self.login.page_click_me()
                # 点击 已有账号，去登录
                self.login.page_click_account_link()
        # 否则逆向
        else:
            try:
                # 断言 toast
                assert expect_toast in self.login.page_get_err_info(expect_toast)
            except:
                # 截图 并 将截图写入报告
                self.login.base_get_img()
                raise
