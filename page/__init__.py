from selenium.webdriver.common.by import By

"""以下配置数据为登录模块"""
# 我
login_me = By.ID, "com.yunmall.lc:id/tab_me"
# 已有账号去登录
login_account_exists = By.ID, "com.yunmall.lc:id/textView1"
# 账号
login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 密码
login_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 登录按钮
login_btn = By.ID, "com.yunmall.lc:id/logon_button"
# 昵称
login_nickname = By.ID, "com.yunmall.lc:id/tv_user_nikename"
# 设置
login_setting = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 消息推送
login_msg_push = By.ID, "com.yunmall.lc:id/setting_notification"
# 修改密码
login_modify_pwd = By.ID, "com.yunmall.lc:id/setting_modify_pwd"
# 退出按钮
login_logout_btn = By.ID, "com.yunmall.lc:id/setting_logout"
# 确定退出
login_logout_ok = By.ID, "com.yunmall.lc:id/ymdialog_right_button"
# 地址管理
login_address_manage = By.ID, "com.yunmall.lc:id/setting_address_manage"

"""以下数据为地址管理配置数据"""
# 新增地址
address_new = By.ID, "com.yunmall.lc:id/address_add_new_btn"
# 收件人
address_receipt_name = By.ID, "com.yunmall.lc:id/address_receipt_name"
# 电话
address_add_phone = By.ID, "com.yunmall.lc:id/address_add_phone"
# 点击 所在地区
address_province = By.ID, "com.yunmall.lc:id/address_province"
# 选择 省/直辖市 com.yunmall.lc:id/area_title
# 选择 市
# 选择 区
# 详细地址
address_detail_info = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
# 邮编
address_postcode = By.ID, "com.yunmall.lc:id/address_post_code"
# 设为默认地址
address_default = By.ID, "com.yunmall.lc:id/address_default"
# 保存
address_save = By.ID, "com.yunmall.lc:id/button_send"
# 收件人和电话
address_person_phone = By.ID, "com.yunmall.lc:id/receipt_name"
# 地址信息
address_info = By.ID, "com.yunmall.lc:id/receipt_address"
# 编辑
address_edit = By.ID, "com.yunmall.lc:id/ymtitlebar_right_btn"
# 修改
address_modify = By.ID, "com.yunmall.lc:id/modify"
# 删除
address_delete = By.ID, "com.yunmall.lc:id/delete"
# 确认删除
address_delete_ok = By.ID, "com.yunmall.lc:id/ymdialog_left_button"
