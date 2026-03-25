p = float(input("Enter principal value: "))
r = float(input("Enter rate of interest: "))
t = int(input("Enter time (in years): "))

A = p * (1 + r/100) ** t
A = round(A, 2)

ci = A - p
ci = round(ci, 2)

print("Compound Interest is:", ci)
print("Total Amount is:", A)
