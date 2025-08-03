def exp(x,y):
    val = 1
    for i in range(y):
        val *= x
    return val

print(exp(2,3))