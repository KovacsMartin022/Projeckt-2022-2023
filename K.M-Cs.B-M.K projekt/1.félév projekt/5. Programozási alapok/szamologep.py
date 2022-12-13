num1 = int(input("Első szám:"))
op = input("Művelet")
num2 = int(input("Második szám:"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Nem érvényes művelet")