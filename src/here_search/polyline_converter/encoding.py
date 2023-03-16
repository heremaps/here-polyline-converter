###############################################################################
#
# Copyright (c) 2023 HERE Europe B.V.
#
# SPDX-License-Identifier: MIT
# License-Filename: LICENSE
#
###############################################################################

from flexpolyline.encoding import encode_scaled_value
from typing import Iterable, Callable, Dict

__all__ = ['encode_legacy', 'PBAPI_WIDTHS']


PBAPI_WIDTHS: Dict[str, str] = {"DW": ".D", "CW": ".C", "HW": ".H"}


def encode_legacy(coordinates: Iterable, precision=5) -> str:
    """Encode a sequence of lat,lng or lat,lng(,{width_type}).
    `width_type`: Additional 3rd dimension precises the type for upcoming segments (CW, HW or DW).
    `precision`: how many decimal digits of precision to store the latitude and longitude.
    """
    multiplier_degree = 10 ** precision

    last_lat = last_lng = 0

    res = []
    appender: Callable[[str], None] = res.append

    for location in coordinates:
        lat = int(round(location[0] * multiplier_degree))
        encode_scaled_value(lat - last_lat, appender)
        last_lat = lat

        lng = int(round(location[1] * multiplier_degree))
        encode_scaled_value(lng - last_lng, appender)
        last_lng = lng

        try:
            if len(location) > 2:
                appender(PBAPI_WIDTHS[location[2]])
        except KeyError:
            raise ValueError(f"third_dim not one of: {', '.join(PBAPI_WIDTHS.keys())}")

    return ''.join(res)
