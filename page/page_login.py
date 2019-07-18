import allure

import page
from base.base import Base


class PageLogin(Base):

    # 点击 我
    @allure.step(title='正在点击 我')
    def page_click_me(self):
        self.base_click(page.login_me)

    # 点击已有账号，去登录
    @allure.step(title='正在点击 已有账号，去登录')
    def page_click_account_link(self):
        self.base_click(page.login_account_exists)

    # 输入用户名
    @allure.step(title='正在输入用户名')
    def page_input_username(self, username):
        allure.attach("用户名：",username)
        self.base_input(page.login_username, username)

    # 输入密码
    @allure.step(title='正在输入密码')
    def page_input_pwd(self, pwd):
        allure.attach("密码：", pwd)
        self.base_input(page.login_pwd, pwd)

    # 点击登录
    @allure.step(title='正在 点击登录按钮')
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取 登录后的昵称
    @allure.step(title='正在 获取登录后的昵称')
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    # 获取异常 toast提示消息
    @allure.step(title='正在 获取toast消息')
    def page_get_err_info(self, msg):
        allure.attach("查找包含{} 的toast消息：".format(msg), " ")
        return self.base_get_toast(msg)

    # 点击 设置
    @allure.step(title='正在 点击设置')
    def page_click_setting(self):
        self.base_click(page.login_setting)

    # 点击地址 管理
    def page_click_address_manage(self):
        self.base_click(page.login_address_manage)

    # 拖拽 消息推送-->修改密码
    @allure.step(title='正在 拖拽操作')
    def page_drag_and_drop(self):
        allure.attach("从{} 元素 拖拽到 {} 元素：".format(page.login_msg_push, page.login_modify_pwd), " ")
        self.base_drag_and_drop(page.login_msg_push, page.login_modify_pwd)

    # 点击 退出
    @allure.step(title='正在 点击退出按钮')
    def page_click_logout(self):
        self.base_click(page.login_logout_btn)

    # 点击 确认退出
    @allure.step(title='确认退出操作')
    def page_click_logout_ok(self):
        self.base_click(page.login_logout_ok)

    # 退出登录组合业务方法
    @allure.step(title='调用退出组合业务方法')
    def page_logout(self):
        self.page_click_setting()
        self.page_drag_and_drop()
        self.page_click_logout()
        self.page_click_logout_ok()

    # 组合业务方法
    @allure.step(title='调用登录业务方法 ')
    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 组合业务方法
    @allure.step(title='调用 地址依赖登录业务方法、 ')
    def page_login_address(self, username="itheima", pwd="123456"):
        # 点击 我
        self.page_click_me()
        # 点击 已有账号去登录
        self.page_click_account_link()
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
        # 点击设置
        self.page_click_setting()
        # 点击 地址管理
        self.page_click_address_manage()