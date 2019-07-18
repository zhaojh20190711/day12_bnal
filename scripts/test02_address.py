import os
import sys



sys.path.append(os.getcwd())
import allure
from tool.read_yaml import read_yaml
import pytest

from page.page_in import PageIn
from tool.get_driver import GetDriver


def get_data(type):
    arrs = []
    if type =="post":
        arrs.append(tuple(read_yaml("address.yaml").get("post_address").values()))
    elif type =="put":
        arrs.append(tuple(read_yaml("address.yaml").get("put_address").values()))
    return arrs


# def get_data_modify():
#     # name, phone, province, city, area, info, code, msg, expect_toast
#     # return [("张三", "13800001111", "广东省", "湛江市", "坡头区", "XXXX大街108号", "100080", "成功", "保存成功")]
#     # 改造后数据，让msg和expect_toast相同
#     return [("王二", "13811112222", "河北省", "石家庄市", "新华区", "XXXX大街288号", "110888", "保存成功")]


class TestAddress:
    # 初始化
    @allure.step(title="正在初始化 setup_class")
    def setup_class(self):
        # 获取PageLogin 并 调用 登录方法
        PageIn().page_get_PageLogin().page_login_address()
        # 获取PageAddress对象
        self.address = PageIn().page_get_PageAddress()

    # 结束
    @allure.step(title="正在调用 teardown_class")
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_driver()

    # 测试方法
    @allure.step(title="正在调用 新增地址测试用例")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("name,phone,province,city,area,info,code", get_data("post"))
    def test_post_address(self, name, phone, province, city, area, info, code):
        # 调用新增地址业务方法
        self.address.page_add_address(name, phone, province, city, area, info, code)
        try:
            # 组合 收件人和电话
            result_person = name + "  " + phone
            # 断言 收件人和电话
            assert result_person in self.address.page_get_person_phone_list()
            # 组合 地址
            address = province+city+area+info
            # 断言地址
            assert address in self.address.page_get_address_list()
        except:
            # 截图
            self.address.base_get_img()
            # 抛异常
            raise

    # 修改测试方法
    @allure.step(title="正在调用 修改地址测试用例")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name, phone, province, city, area, info, code, expect_toast", get_data("put"))
    def test_put_address(self, name, phone, province, city, area, info, code, expect_toast):
        self.address.page_put_address(name, phone, province, city, area, info, code)
        try:
            # 断言toast消息
            assert expect_toast == self.address.page_get_modify_toast(expect_toast)
            # 组合 收件人和电话
            result_person = name + "  " + phone
            # 断言 收件人和电话
            assert result_person in self.address.page_get_person_phone_list()
            # 组合 地址
            address = province + city + area + info
            # 断言地址
            assert address in self.address.page_get_address_list()
        except:
            # 截图
            self.address.base_get_img()
            # 抛异常
            raise

    # 删除地址方法
    @allure.step(title="正在调用 删除地址测试用例")
    @pytest.mark.run(order=3)
    def test_delete_address(self):
        # 调用 删除地址业务方法
        self.address.page_delete_address()
        try:
            # 断言
            assert self.address.page_if_address_exists()
        except:
            # 截图
            self.address.base_get_img()
            # 抛异常
            raise