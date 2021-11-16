# 类


class Point:  # class关键词定义类 + 单词首字母大写的类名 “:”+缩进是python中的代码块表示方法
    def __init__(self, x, y):  # 双下划线初始化构造方法
        self.x = x
        self.y = y

    def move(self):  # 类中可以定义方法/函数，在类中定义的这个方法的参数，pycharm会自动添加关键字self关键字
        print("移动")

    def draw(self):
        print("绘制")


numbers = [1, 2, 3, 5]

# point1 = Point()  # 实例化得到一个对象
# point1.draw()  # 使用.操作符来调用对象的方法

point2 = Point(10, 20)  # 构造函数
print(point2.y)
