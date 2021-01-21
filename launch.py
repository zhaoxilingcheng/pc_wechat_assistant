import winreg

# 防撤回原来的字符
back_o = '8bcee85d4b6f0085c0747b8bc8e8e2536f0085c07562'
# 翻撤回更新后的字符
back_n = '8bcee85d4b6f0085c0eb7b8bc8e8e2536f0085c07562'


def run():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Tencent\\WeChat")
        value = winreg.QueryValueEx(key, "InstallPath")[0]
    except:
        value = input("在当前登录用户的目录下未找到微信安装目录, 请手动输入:")
    file_path = value + "\\WeChatWin.dll"

    # 拷贝一份文件
    with open(file_path, "rb") as f1, open("%s.bak" % file_path, "wb") as f2:
        for line in f1:
            f2.write(line)

    with open(file_path, "rb") as f:
        hex_str = f.read().hex()
        # 防撤回替换
        back_str = hex_str.replace(back_o,
                                   back_n)
        # 双开替换
        file_data = back_str.replace('e86b00000084c07456566a00', 'e86b00000084c0eb56566a00')

    # 写入文件
    with open(file_path, "wb") as f:
        f.write(bytes.fromhex(file_data))


if __name__ == '__main__':
    try:
        run()
        print("执行成功")
    except:
        print("执行失败, 请检查是否未关闭微信程序!")

    input("按任何按键退出!")
