
# Tuples can have any objects inside

new_tuple = 1, 2 + 3
print(new_tuple)

new_tuple = ('the', 1, ("and", "only"))
print(new_tuple)

empty_tuple = ()
one_element_tuple = (10,)

code = ("up", "up", "down", "down") + ("left", "right") * 2
print(len(code))
print(code[3])
print(code.count("down"))
print(code.index("left"))

# methods for manipulating the contents of a list are not available for tuples ebcause tuples are immutable
