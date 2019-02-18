#元类就是用来创建类的“东西”。
#Python中类也是一种对象。
#定义一个类
# Python解释器在执行的时候会创建一个对象
class AI(object):
    pass
#使用type方法查看类类型<class 'type'>
print(type(AI))
# <class 'type'>
#type拥有创建类的功能

#type可以动态的创建类。
#type(类名, 由父类名称组成的元组，包含属性的字典)
AI = type("AI", (), {"hp": 100,"age":25})
print(AI)
print(AI.__class__)
a1 = AI()
print(a1.__class__)
