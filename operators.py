a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(b - a)    # -9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division
print(a % b)    # 0 modulo: remainder

print()

# for i in range(1, a / b):
#    print(i)
#TypeError: 'float' object cannot be interpreted as an integer

for i in range(1, a // b):
    print(i)

