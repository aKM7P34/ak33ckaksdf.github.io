from random import shuffle


def shuffle_str():
    # 将字符串转换成列表
    a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;=?@^_`:{|}~."
    for i in range(len(a)):

        str_list = list(a)
        # 调用random模块的shuffle函数打乱列表
        shuffle(str_list)
        # 将列表转字符串
        print( ''.join(str_list))


# 调用
if __name__ == '__main__':
    shuffle_str()
