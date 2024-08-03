import fhs

f = fhs.convert(['cat', 1, '2', 3, 'dog'], 'hash.set')

print('cat',   f.has('cat'))
print('dog',   f.has('dog'))
print('snake', f.has('snake'))
