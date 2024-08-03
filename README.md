# on-disk-hashset
A Hash-Set Stored on Disk

# Example
```python
import fhs

with fhs.convert(['cat', 1, '2', 3, 'dog'], 'hash.set') as f:
    print('cat',   f.has('cat'))
    print('dog',   f.has('dog'))
    print('snake', f.has('snake'))

# cat True
# dog True
# snake False
```
