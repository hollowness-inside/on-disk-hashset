import struct
import hashlib


def HASH(x: any) -> int:
    if isinstance(x, str):
        x = x.encode()
    elif isinstance(x, int):
        x = struct.pack('>I', x)

    digest = hashlib.sha256(x).digest()
    return int.from_bytes(digest, byteorder='big')


class FileHashSet:
    pass


def convert(array: list[any], fout: str) -> FileHashSet:
    modulo = len(array)
    hashmap = [(i, set()) for i in range(modulo)]

    for item in array:
        id = HASH(item) % modulo
        hashmap[id][1].add(item)

    print(hashmap)


convert(['cat', 1, '2', 3, 'dog'], 'hash.set')
