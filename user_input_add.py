def add(a, b):
    sum = a + b
    return sum

a = input('first number:')
b = input('second number:')
a = int(a)
b = int(b)
q = add(a, b)
print(f"sum of the numbers is: {q}")
