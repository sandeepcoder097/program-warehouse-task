n=int(input()) #size input
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) +fib(n-2)

def fib_seq(f):
    a = {}
    def z(x):
        if x not in a:            
            a[x] = f(x)
        return a[x]
    return z


fib = fib_seq(fib)

print(fib(n))
