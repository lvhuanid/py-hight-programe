# def my_split(s, ds):
#     res = [s]
#     for d in ds:
#         t = []
#         list(map(lambda x: t.extend(x.split(d)), res))
#         res = t
#     # return res
#     return [x for x in res if x]
#
# s = 'hd,,,i|uags;df\tua\tsg;swesdsdf'
# print(my_split(s, ',|\t;'))

import re

s = 'hd,,,i|uags;df\tua\tsg;swesdsdf'
print((re.split('[,|;\t]+', s)))