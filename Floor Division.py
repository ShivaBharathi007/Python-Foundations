# a = 17
# b = 5
# q = a // b   # 3
# r = a % b    # 2
#
# # check:
# print(q * b + r)  # 3*5 + 2 = 17

a = -17
b = 5

q = a /b  # floor division
r = a % b   # modulus

print("a =", a)
print("b =", b)
print("Quotient (q) =", q)
print("Remainder (r) =", r)
print("Check: q * b + r =", q * b + r)  # Should equal a
