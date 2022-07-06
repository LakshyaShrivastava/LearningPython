# Tuples
import collections

t = "venus", -28, "green", "21", 19.74

print(t.count("venus"))
print(t.index(19.74))

hair = "black", "brown", "blonde", "red"
print(hair[2])
print(hair[1:])

x = hair[:2], "grey", hair[2:] # results in a 3 tuple that results in two 2-tuples
print(x)

x = hair[:2] + ("grey",) + hair[2:] # results in a 1 tuple with grey added in the middle
print(x)

# Tuples can be nested infinitely

things = (1, -7.5, ("pea", (5, "Xyz"), "queue"))

print(things[2][1][1][2])

# Named Tuples - same as regular, but can be referred to by names and indexes

Sale = collections.namedtuple("Sale", "Product_ID Customer_ID Date Quantity Price") # Arguments = (Name of the custom tuple data type, String of space separated names -> one for each item that the custom tuple can take)

sales = []
sales.append(Sale(432, 921, "2008-09-14", 3, 7.99))
sales.append(Sale(419, 874, "2008-09-15", 1, 18.49))

total = 0
for sale in sales:
    total += sale.Quantity * sale.Price
print("Total: ${0:.2f}".format(total))

print("Product_ID: {Product_ID} \nCustomer_ID: {Customer_ID}".format(**sale._asdict())) # ._asdict() can be used to print easily

# Lists - Arrays, can hold any data types

L = [-17.5, "kilo", 49, "V",  ["ram", 5, "echo"], 7]

L2 = list()
L2.append(-17.5)
L2.append("kilo")
L2.append(49)
L2.append("V")
L2.append(["ram", 5, "echo"])
L2.append(7)

print(L) # Both list are equal
print(L2)

# some ways to access elements of the lists
print(L[0] == L[-6] == -17.5)
print(L[1] == L[-5] == 'kilo')
print(L[1][0] == L[-5][0] == 'k')
print(L[4][2] == L[4][-1] == L[-2][2] == L[-2][-1] == 'echo')
print(L[4][2][1] == L[4][2][-3] == L[-2][-1][1] == L[-2][-1][-3] == 'c')

# * is the sequence unpacking operator

first, *rest = [9,2,-4,8,7]
print(first, rest)

first, *mid, last = "Charles Phillip Aurthur George Windsor".split()
print(first,mid,last)

*dictionaries, executable = "/usr/local/bin/gvim".split("/")
print(dictionaries, executable)

woods = ["Cedar", "Yew", "Fir"]
print(woods)
woods += ["Kauri", "Larch"]   # woods.extend(["Kauri", "Larch"])
print(woods)
woods[2:2] = ["Pine"]   # woods.insert(2, "Pine")
print(woods)
woods[2:4] = [] # del woods[2:4]
print(woods)

