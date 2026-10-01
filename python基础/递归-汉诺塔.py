def haoni(n,x,y,z):
    if n == 1:
        print(x,"-->",z)
    else:
        haoni(n-1,x,z,y)
        print(x,"-->",z)