# 完成计算 建议使用进程

# 使用多线程的方式完成网站数据的抓取工作，提升爬虫运行效率 

import time
import requests
import threading

# def work_1():
#     for i in range(5):
#         print('任务1')
#         time.sleep(1)


# def work_2():
#     for i in range(5):
#         print('任务2')
#         time.sleep(1)


# t1 = threading.Thread(target=work_1)
# t2 = threading.Thread(target=work_2)

# t1.start()
# t2.start()

# 单线程爬虫任务
def get_image(url):
    response = requests.get(url)
    file_name = url.rsplit('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response.content)
    print('下载中')

url_list = [
    'https://images2.alphacoders.com/211/thumbbig-211020.webp',
    'https://images2.alphacoders.com/498/thumbbig-498306.webp',
    'https://images5.alphacoders.com/498/thumbbig-498305.webp'
]

# 单线程
# for i in url_list:
#     get_image(i)

#多线程
# 文件读写 or io
for item in url_list:
    t = threading.Thread(target=get_image, args=(item,))#这里','是为了保证args是个元组
    t.start()