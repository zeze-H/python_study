import test1  # 导入自定义模块 test1（该模块中包含 fun1 和 fun2 等自定义函数）

test1.fun1()
test1.fun2()

import test1 as t  # 将自定义模块 test1 重命名为 t，简化后续调用
t.fun2()

from test1 import fun1, fun2  # 从 test1 模块中直接导入函数（无需通过模块名调用）
fun1()
fun2()
