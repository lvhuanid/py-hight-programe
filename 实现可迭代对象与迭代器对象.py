import requests
from collections.abc import Iterable, Iterator



# 自定义迭代器类
class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def get_weather(self, city):
        response = requests.get(
            'https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city=' + city
        ).json()
        return f"{response['city']} : {response['data'][0]['tem1']} ~ {response['data'][0]['tem2']}"

    # 需要定义城市循环规则
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)

# 自定义可迭代对象
class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    # 需要自定义可迭代对象中返回一个迭代器实例
    def __iter__(self):
        return WeatherIterator(self.cities)

my_iterable = WeatherIterable(['北京', '上海', '南昌', '武汉'])

for i in my_iterable:
    print(i)