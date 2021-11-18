from time import time, localtime


class Clock():

    def __init__(self, h=0, m=0, s=0):
        self._h = h
        self._m = m
        self._s = s

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def show(self):
        return '%02d:%02d:%02d' % \
               (self._h, self._m, self._s)


# 通过类方法创建对象并调用方法获取时间
clock = Clock.now()
print(clock.show())
