a = 0b1101
b = 0b1011

and_operator = a & b
or_operator = a | b
xor_operator = a ^ b

print(f"UND: {bin(and_operator)} ({and_operator})")
print(f"ODER: {bin(or_operator)} ({or_operator})")
print(f"XOR: {bin(xor_operator)} ({xor_operator})")

if and_operator % 2 == 0:
    print(f"Gerade")
else:
    print(f"Ungerade")

