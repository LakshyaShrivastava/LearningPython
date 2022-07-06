# Factorial without recursion
def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(fact_iter(4))
print(factorial(4))


# The two functions below are mutually recursive
def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)


def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)


result = is_even(5)

print("The result was: " + str(result))

# This can be condensed into 1 function

def is_Even(n):
    if n==0:
        return True
    else:
        if (n-1) == 0:
            return False
        else:
            return is_Even((n-1)-1)

result = is_Even(5)

print("The result was: " + str(result))
