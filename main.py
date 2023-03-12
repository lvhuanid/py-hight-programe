from random import randint

N = randint(0, 100)


def guess(k):
    if k == N:
        return True
    if k < N:
        print('猜小了...')
    else:
        print('猜大了...')
    return False

while True:
    data = input('请输入整数数字：')
    if data.isdigit():
        res = int(data)
        if guess(res):
            break
    else:
        print('输入的数据类型有误...')

# 队列