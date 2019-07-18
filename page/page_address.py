import allure

import page
from base.base import Base


class PageAddress(Base):
    # 点击 新增地址
    @allure.step(title="点击 新增地址按钮")
    def page_click_add_address(self):
        self.base_click(page.address_new)

    # 输入 收件人
    @allure.step(title="输入收件人")
    def page_input_receiver(self, name):
        allure.attach("收件人：{}".format(name)," ")
        self.base_input(page.address_receipt_name, name)

    # 输入 手机号
    @allure.step(title="输入收件人")
    def page_input_phone(self, phone):
        allure.attach("手机号：{}".format(phone), " ")
        self.base_input(page.address_add_phone, phone)

    # 点击 所在地区
    @allure.step(title="点击所在地区")
    def page_click_area(self):
        self.base_click(page.address_province)

    # 选择 省/直辖市
    @allure.step(title="点击省")
    def page_click_province(self,text):
        allure.attach("正在点击：{} 省".format(text), " ")
        self.base_text_click(text)

    # 选择 市
    @allure.step(title="点击市")
    def page_click_city(self, text):
        allure.attach("正在点击：{} 市".format(text), " ")
        self.base_text_click(text)

    # 选择 区
    @allure.step(title="点击区/县/市")
    def page_click_small_area(self, text):
        allure.attach("正在点击：{} 区/县/市".format(text), " ")
        self.base_text_click(text)

    # 详细地址
    @allure.step(title="正在输入详细地址")
    def page_click_address_info(self, info):
        allure.attach("正在输入详细地址：{}".format(info), " ")
        self.base_input(page.address_detail_info, info)

    # 邮编
    @allure.step(title="正在输入 邮编")
    def page_input_code(self, code):
        allure.attach("正在输入邮编：{}".format(code), " ")
        self.base_input(page.address_postcode, code)

    # 设为默认地址
    @allure.step(title="正在点击 设为默认地址")
    def page_default_address(self):
        self.base_click(page.address_default)

    # 保存
    @allure.step(title="正在点击 保存")
    def page_click_save(self):
        self.base_click(page.address_save)

    # 获取地址列表中所有的 收件人和电话
    @allure.step(title="获取地址列表 所有收件人姓名和电话")
    def page_get_person_phone_list(self):
        # 1. 实现 最传统写法
        # arrs = []
        # for el in self.base_finds(page.address_person_phone):
        #     arrs.append(el.text)
        # return arrs

        # 2. 推荐写法
        return [el.text for el in self.base_finds(page.address_person_phone)]

    # 获取地址列表中 所有地址信息
    @allure.step(title="获取地址列表 所有地址信息")
    def page_get_address_list(self):
        return [el.text for el in self.base_finds(page.address_info)]

    # 点击 编辑按钮
    @allure.step(title="点击 编辑按钮")
    def page_click_edit_btn(self):
        self.base_click(page.address_edit)

    # 点击修改第一个元素
    @allure.step(title="点击 修改按钮")
    def page_click_one_element(self):
        self.base_click(page.address_modify)

    # 获取 修改后的toast消息
    @allure.step(title="获取修改 toast信息")
    def page_get_modify_toast(self, msg):
        return self.base_get_toast(msg)

    # 删除 按钮
    @allure.step(title="点击 删除按钮")
    def page_delete_btn(self):
        self.base_click(page.address_delete)

    # 确认删除
    @allure.step(title="点击 确认删除")
    def page_delete_btn_ok(self):
        self.base_click(page.address_delete_ok)

    # 删除全部地址 业务方法
    @allure.step(title="删除 组合业务方法")
    def page_delete_address(self):
        for i in range(len(self.page_get_person_phone_list())):
            # 点击编辑
            self.page_click_edit_btn()
            # 点击 删除
            self.page_delete_btn()
            # 点击 确认删除
            self.page_delete_btn_ok()

    # 判断地址列表中 是否还有地址
    @allure.step(title="判断地址列表中 是否还有地址")
    def page_if_address_exists(self):
        try:
            self.base_find(page.address_person_phone, timeout=2)
            return False  # 没删除干净
        except:
            return True  # 删除干净

    # 填写地址信息 公共方法
    @allure.step(title="填写地址信息 公共方法")
    def page_input_address(self, name, phone, province, city, area, info, code):
        # 填写收件人
        self.page_input_receiver(name)
        # 填写 电话
        self.page_input_phone(phone)
        # 点击 所在区域
        self.page_click_area()
        # 选择 省
        self.page_click_province(province)
        # 选择 市
        self.page_click_city(city)
        # 选择 区/县/县级市
        self.page_click_small_area(area)
        # 输入 详细 地址
        self.page_click_address_info(info)
        # 输入邮编
        self.page_input_code(code)

    # 修改 组合业务方法
    @allure.step(title="修改 组合业务方法")
    def page_put_address(self, name, phone, province, city, area, info, code):
        # 点击编辑
        self.page_click_edit_btn()
        # 点击修改
        self.page_click_one_element()
        # 调用 填写地址信息方法
        self.page_input_address(name, phone, province, city, area, info, code)
        # 点击保存
        self.page_click_save()

    # 新增 组合业务方法
    @allure.step(title="新增 组合业务方法")
    def page_add_address(self, name, phone, province, city, area, info, code):
        # 点击新增地址
        self.page_click_add_address()
        # 调用 填写地址信息方法
        self.page_input_address(name, phone, province, city, area, info, code)
        # 点击默认地址
        self.page_default_address()
        # 点击保存
        self.page_click_save()

