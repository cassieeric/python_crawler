class People():
    name = ''
    age = 0
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("我是%s: 今年%d岁" %(self.name, self.age))

class Student(People):
    grade = ''
    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("%s说：我%d岁了，我在读%d年级" %(self.name, self.age, self.grade))

stu = Student('runoob', 10, 20, 3)
stu.speak()