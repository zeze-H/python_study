#一行流,匿名函数
def squareX(x):
    return x*x
print(squareX(3))

squareY = lambda y:y*y
print(squareY(3))

#lambda是表达式而非语句,所以可以存在在一些普通函数无法存在的地方
y = [lambda x:x*x,2,3]
# 在y0处使用一个y1的数
print(y[0](y[1]))

mapped = map(lambda x:ord(x)+10,"zeze")
print(list(mapped))
#上面等价于:
def boring(x):
    return ord(x) + 10
print(list(map(boring,"zeze")))


# def用于定义哪些功能较为复杂的函数,lambda就可以定义简单函数