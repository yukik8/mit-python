def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
def write_fib(n):
    fib_handle = open('fibonacci','w')
    for i in range(n+1):
        print(fib(i))

def read_fib(n):
    fib_handle = open('fibonacci','r')
    for line in fib_handle:
        print(line)

write_fib(9)
read_fib(9)