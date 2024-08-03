import struct
import hashlib


def HASH(x: any) -> int:
    if isinstance(x, str):
        x = x.encode()
    elif isinstance(x, int):
        x = struct.pack('>I', x)

    digest = hashlib.sha256(x).digest()
    return int.from_bytes(digest, byteorder='big')
