f = open("sample.txt", "w")
f.write("Lucky is a good girl.")
f.close()

f = open("sample.txt", "r")
print(f.read())
f.close()

f = open("sample.txt", "a")
f.write(" Lucky also likes food.")
f.close()

f = open("sample.txt", "r")
print(f.read())
f.close()
