print("Hello World!!!")

n1, n2, name = 10, 11.5, "vishrut"

print(n1)
print("n2 is", n2)
print("My name is", name)

print(n1, "is of type:", type(n1))
print(n2, "is complex number?", isinstance(11.5, complex))

n3 = 1 + 2j
print(n3, "is complex number?", isinstance(1 + 2j, complex))

print(name[0])
print(name[1:3])
print(name[4:])
print(name[:5])
print(name * 4)
print("hello" + name)

l1 = [10, 20, 30.5, "vishrut"]

print(l1, type(l1))
print(l1[1])
print(l1[1:3])

t1 = (10, 20, 30, 40, 50)

print(t1, type(t1))
print(t1[1])
print(t1[3:])
print(t1[:3])

d1 = {10: "hello", "a1": 100, 20: 200}

print(d1, type(d1))
print(d1[10])
print(d1["a1"])
print(d1[20])
