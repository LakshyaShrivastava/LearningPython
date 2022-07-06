from operator import mul

def compose1(f,g):
    return lambda x: f(g(x))

compose1 = lambda f,g: lambda x: f(g(x))

#two above statements are equal but one is easier to understand
s = lambda x: x*x

print(s)
print(s(12))



# different implementations for the square function

def square(x):
    """
    :param x: number to be squared
    :return: x squared
    """
    return pow(x, 2)

def square(x):
    return x ** 2

def square(x):
    return mul(x,x)

square = lambda x: x * x
