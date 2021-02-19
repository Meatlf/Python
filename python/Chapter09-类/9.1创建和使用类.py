# 第9章 类

# 9.1 创建和使用类
# 9.1.1 创建Dog类


class Dog():
    """一次模拟小狗的简单尝试"""

    # 当创建Dog类实例时，Python都会自动运行它
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+" rolled over!")


# 9.1.2 根据类创建实例
my_dog = Dog('huhu', 6)

# 1.访问属性
# my_dog.name.title()将my_dog的属性name的值'while'改为首字母大写的
print("My dog's name is " + my_dog.name.title() + ".")
# str(my_dog.age) 将my_dog 的属性age 的值6 转换为字符串
print("My dog is " + str(my_dog.age) + " years old.")

# 2.调用方法
my_dog.sit()
my_dog.roll_over()

# 9-1 餐馆


class Restaurant():
    """餐厅"""

    # 当创建Restaurant类实例时，Python都会自动运行它
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is "+self.restaurant_name +
              "," + "the cuisine's type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant is opening!")


# 创建实例
my_restaurant = Restaurant('haha', 'student')

# 1.访问属性
# my_dog.name.title()将my_dog的属性name的值'while'改为首字母大写的
print("My restaurant's name is " + my_restaurant.restaurant_name.title() + ".")
# str(my_dog.age) 将my_dog 的属性age 的值6 转换为字符串
print("My restaurant's type is " + my_restaurant.cuisine_type+".")

# 2.调用方法
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
