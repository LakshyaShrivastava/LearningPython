from operator import getitem
from operator import add
from operator import mul

members = ["Pamela", "Tinu", "Brenda", "Kaya"]

print(len(members))

# uses indexes to access values
# can also use functions
print(getitem(members, 0))

# concatenation

boba_prices = [5.50, 6.50, 7.50]
smoothie_prices = [7.00, 7.50]
all_prices = boba_prices + smoothie_prices
print(all_prices)

all_prices = add(boba_prices, smoothie_prices)
print(all_prices)

# repitition

more_boba = boba_prices * 3
print(more_boba)

more_boba = mul(boba_prices, 3)
print(more_boba)

# in operator is used to test if a value is inside a container

print(5 in boba_prices)
print(6.50 in boba_prices)

# looping through nested lists

gymnasts = [
    ["Brittany", 9.15, 9.4, 9.3, 9.2],
    ["Lea", 9, 8.8, 9.1, 9.5],
    ["Maya", 9.2, 8.7, 9.2, 8.8]
]

for gymnast in gymnasts:
    for data in gymnast:
        print(data, end="|")
    print()

# sequence unpacking in for statements
pairs = [[1, 2], [2, 2], [3, 2], [4, 4]]
same_count = 0

for x, y in pairs:
    if x == y:
        same_count = same_count + 1
print(same_count)

# List comprehension syntax
# make a new list by "mapping" an existing list

odds = [1, 3, 5, 7, 9]
evens = [(num + 1) for num in odds]
print(evens)

# my code
# def divisors(n):
#     ret_list = []
#     for x in range (1, n):
#         if n % x == 0:
#             ret_list.append(x)
#     return ret_list

# Solution
def divisors(n):
    return [x for x in range(1,n) if n % x ==0]

print(divisors(12))
