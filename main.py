import struct
import hashlib
import marshal


def HASH(x: any) -> int:
    if isinstance(x, str):
        x = x.encode()
    elif isinstance(x, int):
        x = struct.pack('>I', x)

    digest = hashlib.sha256(x).digest()
    return int.from_bytes(digest, byteorder='big')


class FileHashSet:
    def __init__(self, path: str) -> None:
        pass


def convert(array: list[any], fout: str) -> FileHashSet:
    modulo = len(array)
    hashmap = [(i, set()) for i in range(modulo)]

    for item in array:
        id = HASH(item) % modulo
        hashmap[id][1].add(item)

    _dump(hashmap, modulo, fout)
    return FileHashSet(fout)


def _dump(hashmap: list[tuple[int, set]], modulo: int, fout: str):
    rawblocksize = 0
    blocks = []
    for i in hashmap:
        marshalled = marshal.dumps(i[1])
        lm = len(marshalled)

        rawblocksize = max(rawblocksize, lm)
        blocks.append((marshalled, lm))

    blocksize = rawblocksize + 4 + 4

    with open(fout, 'wb') as f:
        f.write(struct.pack('>II', modulo, blocksize + 4))

        for (block, bsize) in blocks:
            f.write(struct.pack('>I', bsize))
            f.write(block)
            f.write(b'\0' * (blocksize - bsize))


convert(['cat', 1, '2', 3, 'dog'], 'hash.set')
