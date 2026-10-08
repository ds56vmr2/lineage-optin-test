"""Lineage protocol test fixture: a tiny hex codec. Not a real project."""


def encode(data: bytes) -> str:
    out = ""
    for b in data:
        out = out + "%02x" % b
    return out


def decode(text: str) -> bytes:
    return bytes(int(text[i:i + 2], 16) for i in range(0, len(text), 2))
