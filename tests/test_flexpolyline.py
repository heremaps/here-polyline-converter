# Copyright (C) 2019 HERE Europe B.V.
# Licensed under MIT, see full license in LICENSE
# SPDX-License-Identifier: MIT
# License-Filename: LICENSE

import unittest

import flexpolyline_pbapi as fp


class TestFlexPolyline(unittest.TestCase):
    def test_encode1(self):
        input = [
            (50.1022829, 8.6982122),
            (50.1020076, 8.6956695),
            (50.1006313, 8.6914960),
            (50.0987800, 8.6875156),
        ]
        res = fp.encode(input)
        expected = "BFoz5xJ67i1B1B7PzIhaxL7Y"

        self.assertEqual(res, expected)

    def test_dict_encode(self):
        input = [
            {'lat': 50.1022829, 'lng': 8.6982122},
            {'lat': 50.1020076, 'lng': 8.6956695},
            {'lat': 50.1006313, 'lng': 8.6914960},
            {'lat': 50.0987800, 'lng': 8.6875156}
        ]
        res = fp.dict_encode(input)
        expected = "BFoz5xJ67i1B1B7PzIhaxL7Y"

        self.assertEqual(res, expected)

    def test_encode_alt(self):
        input = [
            (50.1022829, 8.6982122, 10),
            (50.1020076, 8.6956695, 20),
            (50.1006313, 8.6914960, 30),
            (50.0987800, 8.6875156, 40),
        ]
        res = fp.encode(input, third_dim=fp.ALTITUDE)
        expected = "BlBoz5xJ67i1BU1B7PUzIhaUxL7YU"

        self.assertEqual(res, expected)

    def test_encode2(self):
        input = [
            [52.5199356, 13.3866272],
            [52.5100899, 13.2816896],
            [52.4351807, 13.1935196],
            [52.4107285, 13.1964502],
            [52.38871, 13.1557798],
            [52.3727798, 13.1491003],
            [52.3737488, 13.1154604],
            [52.3875198, 13.0872202],
            [52.4029388, 13.0706196],
            [52.4105797, 13.0755529],
        ]

        res = fp.encode(input)
        expected = "BF05xgKuy2xCx9B7vUl0OhnR54EqSzpEl-HxjD3pBiGnyGi2CvwFsgD3nD4vB6e"

        self.assertEqual(res, expected)

    def assertAlmostEqualSequence(self, first, second, places=None):
        for row1, row2 in zip(first, second):
            for a, b in zip(row1, row2):
                self.assertAlmostEqual(a, b, places=places)

    def assertAlmostEqualDictSequence(self, first, second, places=None):
        for row1, row2 in zip(first, second):
            for k, a in row1.items():
                self.assertAlmostEqual(a, row2[k], places=places)

    def test_iter_decode1(self):
        polyline = list(p for p in fp.iter_decode("BFoz5xJ67i1B1B7PzIhaxL7Y"))
        expected = [
            (50.10228, 8.69821),
            (50.10201, 8.69567),
            (50.10063, 8.69150),
            (50.09878, 8.68752)
        ]
        self.assertAlmostEqualSequence(polyline, expected, places=7)

    def test_iter_decode_fails(self):
        with self.assertRaises(ValueError):
            list(fp.iter_decode("BFoz5xJ67i1B1B7PzIhaxL7"))

        with self.assertRaises(ValueError):
            list(fp.iter_decode("CFoz5xJ67i1B1B7PzIhaxL7"))

    def test_dict_decode(self):
        polyline = fp.dict_decode("BlBoz5xJ67i1BU1B7PUzIhaUxL7YU")
        expected = [
            {'lat': 50.10228, 'lng': 8.69821, 'alt': 10},
            {'lat': 50.10201, 'lng': 8.69567, 'alt': 20},
            {'lat': 50.10063, 'lng': 8.69150, 'alt': 30},
            {'lat': 50.09878, 'lng': 8.68752, 'alt': 40}
        ]
        self.assertAlmostEqualDictSequence(polyline, expected, places=7)

    def test_iter_decode2(self):
        polyline = list(fp.iter_decode("BF05xgKuy2xCx9B7vUl0OhnR54EqSzpEl-HxjD3pBiGnyGi2CvwFsgD3nD4vB6e"))
        expected = [
            (52.51994, 13.38663),
            (52.51009, 13.28169),
            (52.43518, 13.19352),
            (52.41073, 13.19645),
            (52.38871, 13.15578),
            (52.37278, 13.14910),
            (52.37375, 13.11546),
            (52.38752, 13.08722),
            (52.40294, 13.07062),
            (52.41058, 13.07555),
        ]
        self.assertAlmostEqualSequence(polyline, expected, places=7)

    def test_get_third_dimension(self):
        self.assertEqual(fp.get_third_dimension("BFoz5xJ67i1BU"), fp.ABSENT)
        self.assertEqual(fp.get_third_dimension("BVoz5xJ67i1BU"), fp.LEVEL)
        self.assertEqual(fp.get_third_dimension("BlBoz5xJ67i1BU"), fp.ALTITUDE)
        self.assertEqual(fp.get_third_dimension("B1Boz5xJ67i1BU"), fp.ELEVATION)

    def test_encode_pbapi1(self):
        input = [
            (50.1022829, 8.6982122),
            (50.1020076, 8.6956695),
            (50.1006313, 8.6914960),
            (50.0987800, 8.6875156),
        ]
        res = fp.encode(input, pbapi=True)
        expected = "oz5xJ67i1B1B7PzIhaxL7Y"

        self.assertEqual(expected, res)

    def test_decode_pbapi1(self):
        input = 'ghxgK820xC.Cze7kBw4E3wBkc4rBotEj4HsYrwE41G3oF.HgwCnpGgpD3wBw5GwCsoIvuJjSz2Yo7C_pUk2I3wa0sErkFooJzy' \
                'B8gNvkJo5NvoWo_Pr-Rk1GrrEsuFntJw1D7gwCnpGgpD3wBw5GwCsoIvuJjSz2Yo7C_pUk2I3wa0sErkFooJzyB8gNvkJo5Nvo' \
                'Wo_Pr-Rk1GrrEsuFntJw1D7a0yB7lI88Er6JsqC_jN0qP_-b8pG_wT8iCjqYwlGz1M87C3tK4gE36QgjBjzRksIngS8gDr2L0U' \
                'n2R0jG3pMa0yB7lI88Er6JsqC_jN0qP_-b8pG_wT8iCjqYwlGz1M87C3tK4gE36QgjBjzRksIngS8gDr2L0Un2R0jG3pMooE7t' \
                'OjIvjMo8EvluBoLziYslHn3dk7Dz9hB_7B_vR41BvzYrlC7jT.Ck_BjvOn2C7ua'
        res = fp.decode(input, pbapi=True)
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

        self.assertEqual(expected, res)

    def test_encode_pbapi2(self):
        input = [
            (50.1022829, 8.6982122),
            (50.1020076, 8.6956695),
            (50.1006313, 8.6914960),
            (50.0987800, 8.6875156),
        ]
        res = fp.encode_pbapi(input)
        expected = "oz5xJ67i1B1B7PzIhaxL7Y"

        self.assertEqual(expected, res)

    def test_decode_pbapi2(self):
        input = 'ghxgK820xC.Cze7kBw4E3wBkc4rBotEj4HsYrwE41G3oF.HgwCnpGgpD3wBw5GwCsoIvuJjSz2Yo7C_pUk2I3wa0sErkFooJzy' \
                'B8gNvkJo5NvoWo_Pr-Rk1GrrEsuFntJw1D7gwCnpGgpD3wBw5GwCsoIvuJjSz2Yo7C_pUk2I3wa0sErkFooJzyB8gNvkJo5Nvo' \
                'Wo_Pr-Rk1GrrEsuFntJw1D7a0yB7lI88Er6JsqC_jN0qP_-b8pG_wT8iCjqYwlGz1M87C3tK4gE36QgjBjzRksIngS8gDr2L0U' \
                'n2R0jG3pMa0yB7lI88Er6JsqC_jN0qP_-b8pG_wT8iCjqYwlGz1M87C3tK4gE36QgjBjzRksIngS8gDr2L0Un2R0jG3pMooE7t' \
                'OjIvjMo8EvluBoLziYslHn3dk7Dz9hB_7B_vR41BvzYrlC7jT.Ck_BjvOn2C7ua'
        res = fp.decode_pbapi(input)
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

        self.assertEqual(res, expected)

    def test_reencode_to_pbapi_no_width(self):
        input = "BFoz5xJ67i1B1B7PzIhaxL7Y"
        expected = "oz5xJ67i1B1B7PzIhaxL7Y"
        res = fp.reencode_flex_to_pbapi(input)
        self.assertEqual(expected, res)

    def test_reencode_to_flexpolyline_no_width(self):
        input = "oz5xJ67i1B1B7PzIhaxL7Y"
        expected = "BFoz5xJ67i1B1B7PzIhaxL7Y"
        res = fp.reencode_pbapi_to_flex(input)
        self.assertEqual(expected, res)

    def test_reencoding_cycle_no_width1(self):
        input = "oz5xJ67i1B1B7PzIhaxL7Y"
        res = fp.reencode_flex_to_pbapi(fp.reencode_pbapi_to_flex(input))
        self.assertEqual(input, res)

    def test_reencoding_cycle_no_width2(self):
        input = "BFoz5xJ67i1B1B7PzIhaxL7Y"
        res = fp.reencode_pbapi_to_flex(fp.reencode_flex_to_pbapi(input))
        self.assertEqual(input, res)


if __name__ == '__main__':
    unittest.main()
