print("Hello World!!")

# double quotes in string
print('Hello "World"!!')

# single quotes in string
print("Hello 'World'!!")

# string concat
print("Hello" + " " + "World!!")

# taking input from User
#name = input("Please enter your name:")

#print("Hello " + name, "!!")

str = "Norwegian Blue"
for i in range(0, len(str)):
    print(str[i])

print(str)
print(str[3])
print(str[4])
print()
print(str[3])
print(str[6])
print(str[8])

print()
print(str)
print(str[-11])
print(str[-10])
print()
print(str[-11])
print(str[-8])
print(str[-6])

# slicing(up to but not including)
print()
print(str[0:6])     # Norweg
print(str[3:5])     # we
print(str[0:9])     # Norwegian
print(str[:9])      # Norwegian
print(str[10:14])   # Blue
print(str[10:])     # Blue
print(str[:])       # Blue

print()
print(str[-4:-2])   # Bl
print(str[-4:12])   # Bl
print(str[:-1])     # Norwegian Blue

# step
print()
print(str[0:6:2])   # Nre
print(str[0:6:3])   # Nw
print("0,111;222!333#444"[1::4])    # ,;!#
print(str[:-1:2])   # NreinBu

#backward slicing
print()
print(str[14:0:-1])     # eulB naigewro
print(str[::-1])        # eulB naigewroN