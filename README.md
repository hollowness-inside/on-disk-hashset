# on-disk-hashset
A hash-set stored on the disk.

# Implementation
The given array is turned into a hashmap whose keys are numbers from 0 to N.

The keys for the buckets are calculated with `sha256` modulo length of the array.

## The output binary file format
modulo (4 bytes), blocksize (4 bytes), [datasize (4 bytes), data (N bytes + zero-padded to match blocksize)]*

where
- `modulo` is the modulo used for calculating bucket keys. (currently, length of the input array)
- `blocksize` is the byte size per bucket (including zero-padding).
- `datasize` is the byte size of the actual data in the bucket.
- `data` is the `marshal`'ed object.

`blocksize` is calculated as maximum size of all buckets.

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
