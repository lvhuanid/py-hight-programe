from random import randint, sample
from functools import reduce

name_list = ['邓超','鹿晗','陈赫','王勉']

# res = sample(name_list, 3)
# print(res)

dict_data_1 = {x: randint(10, 50) for x in sample(name_list, 3)}
dict_data_2 = {x: randint(10, 50) for x in sample(name_list, 3)}
dict_data_3 = {x: randint(10, 50) for x in sample(name_list, 3)}

# res = []

# for k in dict_data_1:
#     if k in dict_data_2 and k in dict_data_3:
#         res.append(k)

# print(res)


# 可以利用集合数据类型中的交集特性完成功能
res = dict_data_1.keys() & dict_data_2.keys() & dict_data_3.keys()
print(res)


# data = map(dict.keys, [dict_data_1,dict_data_2,dict_data_3])
# print(data)

res = reduce(lambda a, b: a & b, map(dict.keys, [dict_data_1,dict_data_2,dict_data_3]))
print(res)