![workflow](https://github.com/decitre/python-flexpolyline-pbapi/actions/workflows/test.yml/badge.svg)

# FlexPolyline and HERE Polyline

This is a fork of the python implementation of the [Flexible Polyline](https://github.com/heremaps/flexible-polyline) 
format.
It has been developed to support the HERE polyline encoding used by 
[HERE Places (Search) API](https://developer.here.com/documentation/places/dev_guide/topics/guide.html)
for the [`compressedRoute`](https://developer.here.com/documentation/places/dev_guide/topics/location-contexts.html#location-contexts__here-polyline-encoding) requests parameter.

Use the original repo [heremaps/flexible-polyline](https://github.com/heremaps/flexible-polyline/tree/master/python) 
if you only need to encode/decode polylines used in 
[HERE Geocoding & Search API](https://developer.here.com/documentation/geocoding-search-api/dev_guide/topics/implementing-route.html) or [HERE Routing API](https://developer.here.com/documentation/routing-api/dev_guide/index.html).

## Install

```shell
$ pip install python-flexpolyline-pbapi
```

## Usage


```
>>> encode(iterable, pbapi=True)
```

Encodes a list (or iterator) of coordinates to the corresponding HERE polyline string representation. 
Coordinate order is `(lat, lng[, width])`. 

```
>>> decode(polyline_string, pbapi=True)
```

Decodes a HERE polyline string into an array of coordinates `(lat, lng[, width])`. `width` is epected to be one of `DW`, `HW`, `CW`.

Note that `width` is epected to be one of `DW`, `HW`, `CW`.

#### Examples

```python
import flexpolyline_pbapi as fp

example = [
    (50.1022829, 8.6982122),
    (50.1020076, 8.6956695),
    (50.1006313, 8.6914960),
    (50.0987800, 8.6875156),
]

print(fp.encode(example, pbapi=True))
```

**Output**: `oz5xJ67i1B1B7PzIhaxL7Y`.


```python
import flexpolyline_pbapi as fp

print(fp.dict_decode("oz5xJ67i1B.C1B7PzIha.DxL7Y", pbapi=True))
```

**Output**:

```
[
    (50.10228, 8.69821, 'CW'), 
    (50.10201, 8.69567), 
    (50.10063, 8.6915, 'DW')
]
```

## License

Copyright (C) 2019 HERE Europe B.V.

See the [LICENSE](./LICENSE) file in the root of this project for license details.
