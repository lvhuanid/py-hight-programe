from itertools import islice

f = open('/var/log/system.log')
obj = islice(f, 300, 500)

for item in obj:
    print(item)

# 暂停 打印不出来