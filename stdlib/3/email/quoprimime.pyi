# Stubs for email.quoprimime (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def header_length(bytearray): ...
def body_length(bytearray): ...
def unquote(s): ...
def quote(c): ...
def header_encode(header_bytes, charset=...): ...
def body_encode(body, maxlinelen=..., eol=...): ...
def decode(encoded, eol=...): ...

body_decode = ...  # type: Any
decodestring = ...  # type: Any

def header_decode(s): ...
