a, b = input().split()
a = a.replace("5", "6")
b = b.replace("5", "6")
n = int(a) + int(b)
a = a.replace("6", "5")
b = b.replace("6", "5")
m = int(a) + int(b)
print(m, n)