class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield '%.1f' % t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield '%.1f' % t
            t -= self.step

for item in FloatRange(3, 5, 0.5):
    print(item)

for item in reversed(FloatRange(3, 5, 0.5)):
    print(item)