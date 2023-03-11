# 1. 根据条件筛选列表中的元素
list_data = [1, 5, -7, -3, 0, -2, 6]
res = []
for x in list_data:
    if x >= 0:
        res.append(x)

print(res)

# 实用filter函数进行筛选

res = filter(lambda x: x >= 0, list_data)
print(list(res))

#列表解析
res = [x for x in list_data if x >= 0]
print(res)


# 2. 根据条件筛选字典中的元素
from random import randint

# for i in dict_data.items():
# for i in dict_data.values():
# for i in dict_data:
dict_data = {f'stu_{x}': randint(60, 100) for x in range(1, 21)}
res = {k: v for k, v in dict_data.items() if v >= 90}
print(res)


# 3. 根据条件筛选集合中的元素 筛选出能被3整除的元素
set_data = {randint(-10, 10) for _ in range(10)}
res = {x for x in set_data if x % 3 == 0}
print(res)