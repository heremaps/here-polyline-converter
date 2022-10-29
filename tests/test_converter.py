# Copyright (C) 2022 HERE Europe B.V.
# Licensed under MIT, see full license in LICENSE
# SPDX-License-Identifier: MIT
# License-Filename: LICENSE

import polyline_converter as fp


def test_encode_alt():
    input = [
        (50.1022829, 8.6982122, "CW"),
        (50.1020076, 8.6956695),
        (50.1006313, 8.6914960, "DW"),
        (50.0987800, 8.6875156, "HW"),
    ]
    res = fp.encode_legacy(input)
    expected = "oz5xJ67i1B.C1B7PzIha.DxL7Y.H"

    assert res == expected


def test_encode_legacy1():
    input = [
        (50.1022829, 8.6982122),
        (50.1020076, 8.6956695),
        (50.1006313, 8.6914960),
        (50.0987800, 8.6875156),
    ]
    res = fp.encode_legacy(input)
    expected = "oz5xJ67i1B1B7PzIhaxL7Y"

    assert res == expected


def test_decode_legacy1():
    input = 'ghxgK820xC.Cze7kBw4E3wBkc4rBotEj4HsYrwE41G3oF.HgwCnpGgpD3wBw5GwCsoIvuJjSz2Yo7C_pUk2I3wa0sErkFooJzy' \
            'B8gNvkJo5NvoWo_Pr-Rk1GrrEsuFntJw1D7gwCnpGgpD3wBw5GwCsoIvuJjSz2Yo7C_pUk2I3wa0sErkFooJzyB8gNvkJo5Nvo' \
            'Wo_Pr-Rk1GrrEsuFntJw1D7a0yB7lI88Er6JsqC_jN0qP_-b8pG_wT8iCjqYwlGz1M87C3tK4gE36QgjBjzRksIngS8gDr2L0U' \
            'n2R0jG3pMa0yB7lI88Er6JsqC_jN0qP_-b8pG_wT8iCjqYwlGz1M87C3tK4gE36QgjBjzRksIngS8gDr2L0Un2R0jG3pMooE7t' \
            'OjIvjMo8EvluBoLziYslHn3dk7Dz9hB_7B_vR41BvzYrlC7jT.Ck_BjvOn2C7ua'
    res = fp.decode_legacy(input)
    expected = [(52.516, 13.3771, 'CW'), (52.5111, 13.3712), (52.5355, 13.3634), (52.54, 13.3704),
                (52.5626, 13.3307), (52.5665, 13.3076), (52.6007, 13.2806, 'HW'), (52.6135, 13.2484),
                (52.6303, 13.2406), (52.6651, 13.241), (52.7074, 13.1926), (52.7045, 13.0661), (52.7191, 12.9621),
                (52.7636, 12.8263), (52.7861, 12.8), (52.8335, 12.7919), (52.9002, 12.7451), (52.9708, 12.6311),
                (53.0526, 12.5392), (53.0867, 12.5169), (53.1146, 12.4687), (53.1334, 12.05896),
                (53.1012, 12.07576), (53.0934, 12.11056), (53.0938, 12.15286), (53.0454, 12.14996),
                (52.9189, 12.16456), (52.8149, 12.20906), (52.6791, 12.23156), (52.6528, 12.27896),
                (52.6447, 12.34566), (52.5979, 12.41626), (52.4839, 12.49806), (52.392, 12.53216),
                (52.3697, 12.56006), (52.3215, 12.57886), (52.3172, 12.58696), (52.2753, 12.61206),
                (52.225, 12.62396), (52.1578, 12.70246), (52.0146, 12.73476), (51.9146, 12.74546),
                (51.7901, 12.77706), (51.7252, 12.79176), (51.6718, 12.81236), (51.5856, 12.81796),
                (51.4955, 12.86086), (51.4033, 12.87636), (51.3434, 12.87966), (51.2528, 12.91096),
                (51.1898, 12.91109), (51.1979, 12.86919), (51.223, 12.81889), (51.2349, 12.75169),
                (51.3134, 12.60849), (51.3457, 12.50849), (51.3564, 12.38399), (51.388, 12.31909),
                (51.4027, 12.26569), (51.4233, 12.17949), (51.4289, 12.08939), (51.4718, 11.99719),
                (51.4873, 11.93729), (51.4906, 11.84669), (51.5219, 11.78369), (51.5437, 11.70979),
                (51.5424, 11.64779), (51.5674, 11.41139), (51.5692, 11.28809), (51.6059, 11.13589),
                (51.6256, 10.96219), (51.616, 10.87259), (51.6246, 10.74659), (51.6135, 10.64869, 'CW'),
                (51.6236, 10.57459), (51.6098, 10.43909)]

    assert res == expected


def test_encode_legacy2():
    input = [
        (50.1022829, 8.6982122),
        (50.1020076, 8.6956695),
        (50.1006313, 8.6914960),
        (50.0987800, 8.6875156),
    ]
    res = fp.encode_legacy(input)
    expected = "oz5xJ67i1B1B7PzIhaxL7Y"

    assert res == expected


def test_decode_legacy2():
    input = 'ghxgK820xC.Cze7kBw4E3wBkc4rBotEj4HsYrwE41G3oF.HgwCnpGgpD3wBw5GwCsoIvuJjSz2Yo7C_pUk2I3wa0sErkFooJzy' \
            'B8gNvkJo5NvoWo_Pr-Rk1GrrEsuFntJw1D7gwCnpGgpD3wBw5GwCsoIvuJjSz2Yo7C_pUk2I3wa0sErkFooJzyB8gNvkJo5Nvo' \
            'Wo_Pr-Rk1GrrEsuFntJw1D7a0yB7lI88Er6JsqC_jN0qP_-b8pG_wT8iCjqYwlGz1M87C3tK4gE36QgjBjzRksIngS8gDr2L0U' \
            'n2R0jG3pMa0yB7lI88Er6JsqC_jN0qP_-b8pG_wT8iCjqYwlGz1M87C3tK4gE36QgjBjzRksIngS8gDr2L0Un2R0jG3pMooE7t' \
            'OjIvjMo8EvluBoLziYslHn3dk7Dz9hB_7B_vR41BvzYrlC7jT.Ck_BjvOn2C7ua'
    res = fp.decode_legacy(input)
    expected = [(52.516, 13.3771, 'CW'), (52.5111, 13.3712), (52.5355, 13.3634), (52.54, 13.3704),
                (52.5626, 13.3307), (52.5665, 13.3076), (52.6007, 13.2806, 'HW'), (52.6135, 13.2484),
                (52.6303, 13.2406), (52.6651, 13.241), (52.7074, 13.1926), (52.7045, 13.0661), (52.7191, 12.9621),
                (52.7636, 12.8263), (52.7861, 12.8), (52.8335, 12.7919), (52.9002, 12.7451), (52.9708, 12.6311),
                (53.0526, 12.5392), (53.0867, 12.5169), (53.1146, 12.4687), (53.1334, 12.05896),
                (53.1012, 12.07576), (53.0934, 12.11056), (53.0938, 12.15286), (53.0454, 12.14996),
                (52.9189, 12.16456), (52.8149, 12.20906), (52.6791, 12.23156), (52.6528, 12.27896),
                (52.6447, 12.34566), (52.5979, 12.41626), (52.4839, 12.49806), (52.392, 12.53216),
                (52.3697, 12.56006), (52.3215, 12.57886), (52.3172, 12.58696), (52.2753, 12.61206),
                (52.225, 12.62396), (52.1578, 12.70246), (52.0146, 12.73476), (51.9146, 12.74546),
                (51.7901, 12.77706), (51.7252, 12.79176), (51.6718, 12.81236), (51.5856, 12.81796),
                (51.4955, 12.86086), (51.4033, 12.87636), (51.3434, 12.87966), (51.2528, 12.91096),
                (51.1898, 12.91109), (51.1979, 12.86919), (51.223, 12.81889), (51.2349, 12.75169),
                (51.3134, 12.60849), (51.3457, 12.50849), (51.3564, 12.38399), (51.388, 12.31909),
                (51.4027, 12.26569), (51.4233, 12.17949), (51.4289, 12.08939), (51.4718, 11.99719),
                (51.4873, 11.93729), (51.4906, 11.84669), (51.5219, 11.78369), (51.5437, 11.70979),
                (51.5424, 11.64779), (51.5674, 11.41139), (51.5692, 11.28809), (51.6059, 11.13589),
                (51.6256, 10.96219), (51.616, 10.87259), (51.6246, 10.74659), (51.6135, 10.64869, 'CW'),
                (51.6236, 10.57459), (51.6098, 10.43909)]

    assert res == expected


def test_reencode_to_legacy_no_width():
    input = "BFoz5xJ67i1B1B7PzIhaxL7Y"
    expected = "oz5xJ67i1B1B7PzIhaxL7Y"
    res = fp.convert_flex_to_legacy(input)
    assert res == expected


def test_reencode_to_flexpolyline_no_width():
    input = "oz5xJ67i1B1B7PzIhaxL7Y"
    expected = "BFoz5xJ67i1B1B7PzIhaxL7Y"
    res = fp.convert_legacy_to_flex(input)
    assert res == expected


def test_reencoding_cycle_no_width1():
    input = "oz5xJ67i1B1B7PzIhaxL7Y"
    res = fp.convert_flex_to_legacy(fp.convert_legacy_to_flex(input))
    assert res == input


def test_reencoding_cycle_no_width2():
    input = "BFoz5xJ67i1B1B7PzIhaxL7Y"
    res = fp.convert_legacy_to_flex(fp.convert_flex_to_legacy(input))
    assert res == input

