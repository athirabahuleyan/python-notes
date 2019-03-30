grocery = ['bread', 'egg', 'rice', 'milk']
print(f'Initial list is : {grocery}')
b = 'avocado'
grocery.append(b)
print(f'The edited list with new item is: {grocery}')
grocery.append('chocolate')
print(f'the sunday shopping list is: {grocery}')
grocery.remove('milk')
a = input('the item to be added:')
grocery.append(a)
print(f'The final list is: {grocery}')
print(f'the length of the list is: {len(grocery)}') 