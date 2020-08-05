class Student(object):

    def __init__(self):
        self._score = 60

    @property                 # 设置score 读取的方法为一个属性
    def score(self):
        return self._score

    @score.setter             # property.setter 使得property 可以写入
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
# s.score = 60         #类内封装的属性也可以直接访问了，转化为s.set_score(60)
print(s.score)              # 实际转化为s.get_score()
s.score = 9999       # 实现了参数检查