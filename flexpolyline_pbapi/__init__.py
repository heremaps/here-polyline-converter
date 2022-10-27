# Copyright (C) 2019 HERE Europe B.V.
# Licensed under MIT, see full license in LICENSE
# SPDX-License-Identifier: MIT
# License-Filename: LICENSE

from .encoding import _dict_to_tuple, ABSENT, ALTITUDE, LEVEL, ELEVATION, CUSTOM1, CUSTOM2, THIRD_DIM_MAP
from .decoding import get_third_dimension

from .decoding import iter_decode
from .encoding import encode

from typing import Sequence, Iterable, Union, Tuple, Generator


def dict_encode(coordinates: Iterable[dict], precision: int=5, third_dim: int=ABSENT, third_dim_precision: int=0) -> str:
    """Encode the sequence of coordinates dicts into a polyline string"""
    return encode(
        _dict_to_tuple(coordinates, third_dim),
        precision=precision,
        third_dim=third_dim,
        third_dim_precision=third_dim_precision
    )


def decode(encoded: str, pbapi: bool=False) -> Sequence[Union[Tuple[str, str], Tuple[str, str, str]]]:
    """Return a list of coordinates. The number of coordinates are 2 or 3
    depending on the polyline content."""
    return list(iter_decode(encoded, pbapi))


def iter_dict_decode(encoded: str) -> Generator:
    """Return an iterator over coordinates dicts. The dict contains always the keys 'lat', 'lng' and
    depending on the polyline can contain a third key ('elv', 'lvl', 'alt', ...)."""
    third_dim_key = THIRD_DIM_MAP[get_third_dimension(encoded)]
    for row in iter_decode(encoded):
        yield {
            'lat': row[0],
            'lng': row[1],
            third_dim_key: row[2]
        }


def dict_decode(encoded: str):
    """Return an list of coordinates dicts. The dict contains always the keys 'lat', 'lng' and
    depending on the polyline can contain a third key ('elv', 'lvl' or 'alt')."""
    return list(iter_dict_decode(encoded))


def encode_pbapi(coordinates: Iterable) -> str:
    """Encode a sequence of lat,lng or lat,lng(,{width}).
    `width`: Additional 3rd dimension precising the width for upcoming segments (CW, HW or DW).
    """
    return encode(coordinates, pbapi=True)


def decode_pbapi(encoded: str) -> Sequence[Union[Tuple[str, str], Tuple[str, str, str]]]:
    """Return a list of coordinates. The number of coordinates are 2 or 3
    depending on the polyline content.
    The third dimension is specifying the corridor width for upcoming segments (CW, HW or DW).
    """
    return decode(encoded, pbapi=True)


def reencode_flex_to_pbapi(encoded: str) -> str:
    """Return a HERE Polyline out of a flexpolyline encoded string. The third dimension is ignored and the width is left empty.
    """
    iter_decoded = iter_decode(encoded)
    reencoded = encode_pbapi(iter_decoded)
    return reencoded


def reencode_pbapi_to_flex(encoded: str) -> str:
    """Return a flexible polyline with no third dimension out of a HERE Polyline encoded string.
    The HERE Polyline potential width changes are ignored: The resulting corridor will be of constant width, expressed
    in HERE geocoding & Search API in a specific request parameter.
    """
    decoded = decode_pbapi(encoded)
    reencoded = encode(decoded)
    return reencoded
