def factorial(n):
    result = 1
    for x in range(1,n+1):
        result *= x
    return result

def fibonacci(n):
    if n==0: return 0
    if n==1: return 1
    x,y=0,1
    for i in range(1,n+1):
        r = x+y
        y = x
        x = r
    return r
