import fhs

with fhs.convert(['cat', 1, '2', 3, 'dog'], 'hash.set') as f:
    print('cat',   f.has('cat'))
    print('dog',   f.has('dog'))
    print('snake', f.has('snake'))
