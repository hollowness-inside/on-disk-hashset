# on-disk-hashset
A Hash-Set Stored on Disk

# Example
```python
import fhs
import gzip

with gzip.open('hash.set', 'wb') as fout:
    fhs.dump(['cat', 1, '2', 3, 'dog'], fout)


with gzip.open('hash.set', 'rb') as fin:
    f = fhs.FileHashSet(fin)
    print('cat',   f.has('cat'))
    print('dog',   f.has('dog'))
    print('snake', f.has('snake'))

# cat True
# dog True
# snake False
```