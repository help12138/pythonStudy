"""
创建基本类
"""
class person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def play(self):
        print(self.name + "在玩篮球")

one1 = person("狗蛋", "男", 18)
one1.play()

