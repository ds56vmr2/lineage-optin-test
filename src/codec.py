"""Lineage protocol test fixture: a tiny hex codec. Not a real project."""


def encode(data: bytes) -> str:
    return data.hex()


def decode(text: str) -> bytes:
    return bytes(int(text[i:i + 2], 16) for i in range(0, len(text), 2))
