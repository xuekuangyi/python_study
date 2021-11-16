class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'你好，我是{self.name}')


person1 = Person(input("请输入姓名>>"))
person1.talk()