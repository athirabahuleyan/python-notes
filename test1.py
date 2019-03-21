def add(a, b):
    sum = a + b
    return sum

def sub(a, b):
    diff = a - b
    return diff

x = 5
y = 5
z = 1

temp_result = add(x, y)
result = sub(temp_result, z)

print('The numbers are')
print(x)
print(y)
print(z)

print('The result of a+b-c =')
print(result)



