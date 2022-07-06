# Normal recursion

def  cascade(n):
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)

cascade(123)

def virfib(n):
    """Compute the nth Virahanka-Fibonacci number for N>=1"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return virfib(n-1) + virfib(n-2)

print(virfib(8))

# counting partitions problem:
# Total number of partitions of a positive integer n using parts up to size m

def count_partitions(n,m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m,m)
        without_m = count_partitions(n,m-1)
        return with_m + without_m

print(count_partitions(6,4))
