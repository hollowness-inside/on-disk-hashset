import struct
import hashlib
import marshal
import gzip


def HASH(x: any) -> int:
    if isinstance(x, str):
        x = x.encode()
    elif isinstance(x, int):
        x = struct.pack('>I', x)

    digest = hashlib.sha256(x).digest()
    return int.from_bytes(digest, byteorder='big')


class FileHashSet:
    _blocksize: int
    _modulo: int

    def __init__(self, stream):
        self.stream = stream

        r = self.stream.read(8)
        self.modulo, self.blocksize = struct.unpack('>II', r)

    def has(self, x: any) -> bool:
        id = HASH(x) % self.modulo
        offset = 4 + 4 + id * self.blocksize

        self.stream.seek(offset, 0)
        r = self.stream.read(4)
        if len(r) != 4:
            return False

        size = struct.unpack('>I', r)[0]

        block = self.stream.read(size)
        array = marshal.loads(block)
        for i in array:
            if x == i:
                return True

        return False


def dump(array: list[any], fout) -> None:
    modulo = len(array)
    hashmap = [(i, set()) for i in range(modulo)]

    for item in array:
        id = HASH(item) % modulo
        hashmap[id][1].add(item)

    _dump(hashmap, modulo, fout)


def _dump(hashmap: list[tuple[int, set]], modulo: int, fout) -> None:
    rawblocksize = 0
    blocks = []
    for i in hashmap:
        marshalled = marshal.dumps(i[1])
        lm = len(marshalled)

        rawblocksize = max(rawblocksize, lm)
        blocks.append((marshalled, lm))

    blocksize = rawblocksize + 4 + 4

    fout.write(struct.pack('>II', modulo, blocksize + 4))

    for (block, bsize) in blocks:
        fout.write(struct.pack('>I', bsize))
        fout.write(block)
        fout.write(b'\0' * (blocksize - bsize))
