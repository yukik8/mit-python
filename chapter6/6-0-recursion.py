def recursion(n):
    if n == 1:
        return n
    else:
        return 1/n+recursion(n-1)
print(recursion(4))
print(1+1/2+1/3+1/4)