class Test:
    _x = 10
    __y = 20

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self.__y


t = Test()
print(t.x)
print(t.y)