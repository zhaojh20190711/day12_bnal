import yaml


def read_yaml(filename):
    with open("./data/"+filename,"r",encoding="utf-8")as f:
        return yaml.load(f)

if __name__ == '__main__':
    """ 以下登录 读取测试数据 调试"""
    # print(read_yaml("login.yaml"))
    # print("--" * 50)
    # arrs = []
    # for arr in read_yaml("login.yaml").values():
    #     arrs.append(tuple(arr.values()))
    # print(arrs)

    """以下地址管理 读取测试数据 调试"""
    arrs = []
    print(read_yaml("address.yaml"))
    print("--" * 50)
    arrs.append(tuple(read_yaml("address.yaml").get("post_address").values()))
    print(arrs)