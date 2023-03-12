# 生成器
# def func():
#     print('fun')
#     yield 1
#
#     print('fun2')
#     yield 2
#
#     print('fun3')
#     yield 3

# 生成器是一种特殊的迭代器 实现了迭代器的协议 __next__方法
# f = func()
# print((next(f)))
# print((next(f)))
# print((next(f)))
# print((next(f)))

# for item in f:
#     print(item)


class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # 遍历规则
    @staticmethod
    def is_prime_numbers(k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.is_prime_numbers(k):
                yield k

for item in PrimeNumbers(1, 100):
    print(item)