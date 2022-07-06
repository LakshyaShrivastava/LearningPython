import Shape

a = Shape.Point()
print(repr(a))

b = Shape.Point(3,4)
print(str(b))
print(b.distanceFromOrigin())
b.x = -19
print(str(b))

print(a==b, a!=b)

p = Shape.Point(28,45)
c = Shape.Circle(5,28,45)
