def f(n):
    if n > 1:
        return f(n - 1) + f(n - 2)
    else:
        return 1

print f(40)
