from time import time
from random import randint
from collections import OrderedDict 

# python 2版本需要
# 创建一个有序字典对象
# dict_data = dict()
dict_data = OrderedDict()

players = ['邓超','鹿晗','陈赫','王勉']


# 创建答题时间对象
t_start = time()

players_max_index = len(players) -1
for i in range(len(players)):
    # 模拟同学答题过程
    input('输入任意数据模拟学生答题过程：')
    person = players.pop(randint(0, players_max_index - i))
    t_end = time()
    print(i + 1, person, t_end - t_start)
    dict_data[person] = (i + 1, t_end - t_start)

print(dict_data)