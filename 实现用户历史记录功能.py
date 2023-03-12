from random import randint
from collections import deque
import pickle


#deque双端循环队列

history = deque([], 5)
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
        history.append(res)
        pickle.dump(history, open('history.txt', 'wb'))
        if guess(res):
            break

    elif data == 'h?':
        print('内存中的历史记录信息', list(history))
        file_history = pickle.load(open('history.txt', 'rb'))
        print('文件中的历史记录信息', list(file_history))
    else:
        print('输入的数据类型有误...')

