from itertools import chain
from random import randint

chinese = [randint(60, 100) for _ in range(40)]
math = [randint(60, 100) for _ in range(40)]
english = [randint(60, 100) for _ in range(40)]

res = list()

# zip函数 并连
for c, m, e in zip(chinese, math, english):
    res.append(c + m + e)

# print(res)


# chain
cls_1 = [randint(60, 100) for _ in range(40)]
cls_2 = [randint(60, 100) for _ in range(47)]
cls_3 = [randint(60, 100) for _ in range(50)]
cls_4 = [randint(60, 100) for _ in range(43)]

count = 0

for student in chain(cls_1, cls_2, cls_3, cls_4):
    if student > 90:
        count += 1

print(count)