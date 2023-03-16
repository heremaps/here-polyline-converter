# Copyright (C) 2022 HERE Europe B.V.
# Licensed under MIT, see full license in LICENSE
# SPDX-License-Identifier: MIT
# License-Filename: LICENSE

from flexpolyline import iter_decode, encode

from .decoding import iter_decode_legacy
from .encoding import encode_legacy

from typing import Sequence, Union, Tuple


def decode_legacy(encoded: str) -> Sequence[Union[Tuple[str, str], Tuple[str, str, str]]]:
    """Return a list of coordinates. The number of coordinates are 2 or 3
    depending on the polyline content.
    The third dimension is specifying the corridor width for upcoming segments (CW, HW or DW).
    """
    return list(iter_decode_legacy(encoded))


def convert_flex_to_legacy(encoded: str) -> str:
    """Return a HERE (legacy) polyline out of a HERE flexible polyline encoded string. The third dimension is ignored and the width is left empty.
    """
    iter_decoded = iter_decode(encoded)
    reencoded = encode_legacy(iter_decoded)
    return reencoded


def convert_legacy_to_flex(encoded: str) -> str:
    """
    Return a HERE flexible polyline with no third dimension out of a HERE (legacy) polyline encoded string.
    The HERE Polyline third dimension is ignored.
    """
    decoded = decode_legacy(encoded)
    reencoded = encode(decoded)
    return reencoded
