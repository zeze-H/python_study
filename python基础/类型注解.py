"""类型注解示例：变量、函数和默认参数。"""

# 1. 变量注解：直接为变量添加注解

# 没有类型注解的代码
name = "Alice"
age = 30
is_student = False
scores = [95, 88, 91]

# 有类型注解的代码
name: str = "Alice"  # 字符串
age: int = 30  # 整数
is_student: bool = False  # 布尔值
scores: list[int] = [95, 88, 91]  # 整数列表


# 2. 函数注解：在参数和返回值后添加类型

# 没有类型注解
def greet_plain(first_name, last_name):
    full_name = first_name + " " + last_name
    return "Hello, " + full_name


# 有类型注解
def greet_typed(first_name: str, last_name: str) -> str:
    full_name = f"{first_name} {last_name}"
    return f"Hello, {full_name}"


# 示例
def add_numbers(a: int, b: int) -> int:
    """将两个整数相加并返回结果。"""
    return a + b


result = add_numbers(5, 3)
print(result)


# 3. 参数默认值：同时使用类型注解和默认值
def say_hello(name: str, times: int = 1) -> str:
    """向指定的人问好指定次数。"""
    return "".join(f"Hello, {name}!" for _ in range(times))


print(say_hello("bob"))
print(say_hello("alice", 3))
