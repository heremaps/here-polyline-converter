# Copyright (C) 2019 HERE Europe B.V.
# Licensed under MIT, see full license in LICENSE
# SPDX-License-Identifier: MIT
# License-Filename: LICENSE

from collections import namedtuple
from typing import Iterable, Generator, Callable, Dict
import warnings

__all__ = ['ABSENT', 'LEVEL', 'ALTITUDE', 'ELEVATION', 'encode', 'THIRD_DIM_MAP']

ENCODING_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"

FORMAT_VERSION = 1

ABSENT = 0
LEVEL = 1
ALTITUDE = 2
ELEVATION = 3
# Reserved values 4 and 5 should not be selectable
CUSTOM1 = 6
CUSTOM2 = 7

THIRD_DIM_MAP = {ALTITUDE: 'alt', ELEVATION: 'elv', LEVEL: 'lvl', CUSTOM1: 'cst1', CUSTOM2: 'cst2'}

PBAPI_WIDTHS: Dict[str, str] = {"DW": ".D", "CW": ".C", "HW": ".H"}

PolylineHeader = namedtuple('PolylineHeader', 'precision,third_dim,third_dim_precision')


def encode_unsigned_varint(value: int, appender: Callable[[str], None], pbapi: bool=False) -> None:
    """Uses veriable integer encoding to encode an unsigned integer.
    Returns the encoded string."""
    while value > 0x1F:
        pos = (value & 0x1F) | 0x20
        appender(ENCODING_TABLE[pos])
        value >>= 5
    appender(ENCODING_TABLE[value])


def encode_scaled_value(value: int, appender: Callable[[str], None], pbapi: bool=False) -> None:
    """Transform a integer `value` into a variable length sequence of characters.
    `appender` is a callable where the produced chars will land to"""
    negative = value < 0

    value = value << 1
    if negative:
        value = ~value

    encode_unsigned_varint(value, appender, pbapi)


def encode_header(appender, precision, third_dim, third_dim_precision) -> None:
    """Encode the `precision`, `third_dim` and `third_dim_precision` into one
    encoded char"""
    if precision < 0 or precision > 15:
        raise ValueError("precision out of range")
    if third_dim_precision < 0 or third_dim_precision > 15:
        raise ValueError("third_dim_precision out of range")
    if third_dim < 0 or third_dim > 7:
        raise ValueError("third_dim out of range")
    if third_dim == 4 or third_dim == 5:
        warnings.warn("Third dimension types 4 and 5 are reserved and should not be used "
            "as meaning may change in the future")

    res = (third_dim_precision << 7) | (third_dim << 4) | precision
    encode_unsigned_varint(FORMAT_VERSION, appender)
    encode_unsigned_varint(res, appender)


def encode(coordinates: Iterable, precision=5, third_dim=ABSENT, third_dim_precision=0, pbapi: bool=False) -> str:
    """Encode a sequence of lat,lng or lat,lng(,{third_dim}).
    `precision`: how many decimal digits of precision to store the latitude and longitude.
    `third_dim`: type of the third dimension if present in the input.
    `third_dim_precision`: how many decimal digits of precision to store the third dimension.
    `pbapi`: set to True to encode HERE Polyline (In Maintenance).
    """
    multiplier_degree = 10 ** precision
    multiplier_z = 10 ** third_dim_precision

    last_lat = last_lng = last_z = 0

    res = []
    appender: Callable[[str], None] = res.append
    if not pbapi:
        encode_header(appender, precision, third_dim, third_dim_precision)

    for location in coordinates:
        lat = int(round(location[0] * multiplier_degree))
        encode_scaled_value(lat - last_lat, appender, pbapi)
        last_lat = lat

        lng = int(round(location[1] * multiplier_degree))
        encode_scaled_value(lng - last_lng, appender, pbapi)
        last_lng = lng

        if third_dim and not pbapi:
            z = int(round(location[2] * multiplier_z))
            encode_scaled_value(z - last_z, appender)
            last_z = z
        elif pbapi:
            try:
                if len(location) > 2:
                    appender(PBAPI_WIDTHS[location[2]])
            except KeyError:
                raise ValueError(f"third_dim not one of: {', '.join(PBAPI_WIDTHS.keys())}")

    return ''.join(res)


def _dict_to_tuple(coordinates: Iterable[dict],
                   third_dim: int) -> Generator:
    """Convert a sequence of dictionaries to a sequence of tuples"""
    if third_dim:
        third_dim_key = THIRD_DIM_MAP[third_dim]
        return ((point['lat'], point['lng'], point[third_dim_key]) for point in coordinates)

    return ((point['lat'], point['lng']) for point in coordinates)
