![workflow][b]
[![codecov][c1]][c2]

A tool to encode/decode [HERE legacy polyline][4] strings and convert them from/into HERE [Flexible Polyline][1] format.

Note that the [HERE Places (Search) API][2] is in maintenance: Developers need to adapt their applications to the newer
[HERE Geocoding & Search API][3] to benefit from the features developed after 2018.


## Install

```shell
pip install here-polyline-converter
```

## Usage


```python
>>> convert_legacy_to_flex(legacy_polyline_string)
```

Transforms a HERE legacy polyline string into a flexible polyline string. The legacy Polyline third dimension (segments width changes) is ignored.

```python
>>> encode_legacy(iterable)
```

Encodes a list of coordinates to the corresponding HERE legacy polyline string representation. 
Expected coordinates order: `(lat, lng[, width])`. Note that `width` is expected to be one of `DW`, `HW`, `CW`.


```python
>>> decode_legacy(legacy_polyline_string)
```

Decodes a HERE legacy polyline string into an array of coordinates `(lat, lng[, width])`.


Note that `width` is expected to be one of `DW`, `HW`, `CW`.

#### Examples

```python
>>> import here_search.polyline_converter as pc
>>> legacy_polyline = "oz5xJ67i1B1B7PzIhaxL7Y"
>>> flexible_polyline = pc.convert_legacy_to_flex(legacy_polyline)
>>> flexible_polyline
'BFoz5xJ67i1B1B7PzIhaxL7Y'

>>> points = [(50.1022829, 8.6982122), (50.1020076, 8.6956695), (50.1006313, 8.6914960), (50.0987800, 8.6875156)]
>>> pc.encode_legacy(points)
'oz5xJ67i1B1B7PzIhaxL7Y'

>>> legacy_polyline = "oz5xJ67i1B.C1B7PzIha.DxL7Y"
>>> pc.decode_legacy(legacy_polyline)
[(50.10228, 8.69821, 'CW'), (50.10201, 8.69567), (50.10063, 8.6915, 'DW'), (50.09878, 8.68752)]
```

## License

Copyright (C) 2023 HERE Europe B.V.

See the [LICENSE](./LICENSE) file in the root of this project for license details.

[1]: https://github.com/heremaps/flexible-polyline
[2]: https://developer.here.com/documentation/places/dev_guide/topics/guide.html
[3]: https://developer.here.com/documentation/geocoding-search-api/dev_guide/index.html
[4]: https://developer.here.com/documentation/places/dev_guide/topics/location-contexts.html#location-contexts__here-polyline-encoding
[b]: https://github.com/heremaps/here-polyline-converter/actions/workflows/test.yml/badge.svg
[c1]: https://codecov.io/gh/heremaps/here-polyline-converter/branch/main/graph/badge.svg?token=9LPI9T7BMN
[c2]: https://codecov.io/gh/heremaps/here-polyline-converter