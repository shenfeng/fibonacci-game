import time

def f(n):
    if n > 1:
        return f(n - 1) + f(n - 2)
    else:
        return 1

start = time.time()
result = f(40)
e = int((time.time() - start) * 1000)
print result
print e
