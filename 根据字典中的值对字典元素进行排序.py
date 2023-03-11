# int_list = [3, 1, 6, 2, 4, 0]
# # 对列表进行排序
# res = sorted(int_list)
# print(res)
# print(int_list) #不会对原数组进行更改

# int_list.sort()
# print(int_list)

from random import randint

student_name_list = ['邓超','鹿晗','陈赫','王勉']
student_dict = {x: randint(60, 100) for x in student_name_list}
print(student_dict)

# 方式一 通过zip函数将字典数据转为元组
zip_obj = zip(student_dict.values(), student_dict.keys())
# print(list(zip_obj))
res = sorted(list(zip_obj))
print(res)

# 方式二 直接使用sorted进行排序 指定key属性
print(student_dict.items())
res = sorted(student_dict.items(), key= lambda x: x[1])
print(res)

# 从大到小
res = sorted(student_dict.items(), key= lambda x: x[1], reverse = True)
print(res)