"""文档字符串、类型注解和内省示例。"""


def exchange(dollar: float, rate: float = 6.7) -> float:
    """把美元换算为人民币。

    Args:
        dollar: 美元金额。
        rate: 汇率，默认 6.7。

    Returns:
        人民币金额。
    """
    return dollar * rate


print(exchange(10))
print(exchange.__doc__)


def repeat_str(s: str, n: int) -> str:
    return s * n


# 类型注解只是提示，运行时不会强制检查。
print(repeat_str("zeze", 5))
print(repeat_str(5, 5))


# 自定义默认值
def repeat_str_default(s: str = "zeze", n: int = 3) -> str:
    return s * n


print(repeat_str_default())


# 希望结果是列表
def repeat_list(s: list, n: int = 3) -> list:
    return s * n


print(repeat_list([1, 2, 3, 4, 5]))


# 希望结果是整数列表，注解更精确
def repeat_int_list(s: list[int], n: int = 3) -> list[int]:
    return s * n


print(repeat_int_list([1, 2, 3, 4, 5]))


# 映射类型：字典的键值对类型
def repeat_keys(s: dict[str, int], n: int = 3) -> list[str]:
    return list(s) * n


print(repeat_keys({"A": 1, "B": 2, "C": 3}))

# 第三方模块 mypy 可以对类型注解进行静态检查。


#内省
print(repeat_keys.__name__)