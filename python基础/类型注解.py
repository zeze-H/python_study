'''
#没有类型注解
def greet(name):
    return f"hello,{name}"
#没有类型注解
def greet(name:str) -> str:
    return f"hello,{name}"
'''



#1.变量注解:直接为变量添加注解

#没有类型注解的代码
name="Alice"
age=30
is_student=False
scores=[95,88,91]
#有类型注解的代码
name:str="Alice"#注解为字符串
age:int=30#注解为整数
is_student:bool=False#注解为布尔
scores:list=[95,88,91]#注解为列表



#2.函数注解:在函数后添加类型

#没有
def greet(frist_name,last_name):
    full_name=frist_name+""+last_name
    return "Hello,"+full_name
#有
def greet(frist_name:str,last_name:str)->str:
    full_name=frist_name+""+last_name
    return "Hello,"+full_name

#实例
def add_numbers(a:int,b:int)->int:
    """将两个整数相加并返回结果"""
    return a+b

    #调用函数
result=add_numbers(5,3)
print(result)



#3.参数默认值:同时使用类型注解和默认值
def say_hello(name:str,times:int=1)->str:
    '''向某人问好指定次数'''
    return "".join([f"Hello,{name}!"]*times)
print(say_hello("bob"))
print(say_hello("alice",3))