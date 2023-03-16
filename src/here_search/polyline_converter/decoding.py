###############################################################################
#
# Copyright (c) 2023 HERE Europe B.V.
#
# SPDX-License-Identifier: MIT
# License-Filename: LICENSE
#
###############################################################################

from flexpolyline.decoding import to_signed
from flexpolyline.encoding import ENCODING_TABLE
from typing import Union, Generator

from .encoding import PBAPI_WIDTHS

PBAPI_REV_WIDTHS = {v: k for k, v in PBAPI_WIDTHS.items()}

__all__ = ['iter_decode_legacy']

DECODING_TABLE = [
    62, -1, -1, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1,
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
    22, 23, 24, 25, -1, -1, -1, -1, 63, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
    36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51
]


def decode_char(char: str) -> Union[int, str]:
    """Decode a single char to the corresponding value"""
    char_value = ord(char)
    if char_value < 45:
        raise ValueError('Invalid encoding')
    value = ENCODING_TABLE.index(char)
    if value < 0:
        raise ValueError('Invalid encoding')
    return value


def decode_unsigned_values(encoded: str) -> Generator[Union[str, int], str, None]:
    """Return an iterator over encoded unsigned values part of an `encoded` polyline"""
    result = shift = 0

    dot_encountered = False
    for char in encoded:
        if dot_encountered:
            yield f".{char}"
            dot_encountered = False
            continue
        elif char == ".":
            dot_encountered = True
            continue
        value = decode_char(char)

        result |= (value & 0x1F) << shift
        if (value & 0x20) == 0:
            yield result
            result = shift = 0
        else:
            shift += 5

    if shift > 0:
        raise ValueError('Invalid encoding')


def iter_decode_legacy(encoded: str):
    """Return an iterator over coordinates. The number of coordinates are 2 or 3
    depending on the polyline content."""

    last_lat = last_lng = 0
    decoder = decode_unsigned_values(encoded)

    factor_degree, factor_z, third_dim = 10.0 ** 5, 1, None

    encountered_last_lat = False
    while True:
        try:
            if not encountered_last_lat:
                last_lat += to_signed(next(decoder))
            else:
                encountered_last_lat = False

            last_lng += to_signed(next(decoder))

            try:
                third_value = next(decoder)
            except StopIteration:
                yield last_lat / factor_degree, last_lng / factor_degree
            else:
                if isinstance(third_value, int):
                    yield last_lat / factor_degree, last_lng / factor_degree
                    last_lat += to_signed(third_value)
                    encountered_last_lat = True
                else:
                    width = PBAPI_REV_WIDTHS[third_value]
                    yield last_lat / factor_degree, last_lng / factor_degree, width

        except StopIteration:
            return  # sequence completed
