# A generator function uses yield instead of return

def evens():
    num = 0
    while num < 10:
        yield num
        num += 2


even_generator = evens()

print(next(even_generator))
print(next(even_generator))
print(next(even_generator))
print(next(even_generator))
print(next(even_generator))
# print(next(even_generator))

print()


# Using for loop on generators
def evens(start, end):
    num = start + (start % 2)

    while num < end:
        yield num
        num += 2


for num in evens(12, 60):
    print(num)
