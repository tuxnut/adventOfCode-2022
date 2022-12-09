import unittest

from parameterized import parameterized

from day8.main import (
    create_down_of_position,
    create_left_of_position,
    create_right_of_position,
    create_up_of_position,
    create_viewing_down_of_position,
    create_viewing_left_of_position,
    create_viewing_right_of_position,
    create_viewing_up_of_position,
)


class TestDay8(unittest.TestCase):
    matrix_0 = [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]]
    matrix_1 = [[5, 2, 2, 3, 6], [2, 7, 2, 1, 0], [3, 6, 7, 5, 3], [4, 8, 7, 6, 6], [5, 7, 6, 5, 3]]

    @parameterized.expand(
        [
            (matrix_0, [7, 1, 3]),
            (matrix_1, [3, 1, 5]),
        ]
    )
    def test_create_up_of_position(self, input_matrix, expected):
        # WHEN
        up = create_up_of_position(3, 3, input_matrix)

        # THEN
        self.assertListEqual(up, expected)

    @parameterized.expand(
        [
            (matrix_0, [5, 3, 5]),
            (matrix_1, [6, 8, 7]),
        ]
    )
    def test_create_down_of_position(self, input_matrix, expected):
        # WHEN
        down = create_down_of_position(1, 1, input_matrix)

        # THEN
        self.assertListEqual(down, expected)

    @parameterized.expand(
        [
            (matrix_0, [2, 5, 5, 1]),
            (matrix_1, [2, 7, 2, 1]),
        ]
    )
    def test_create_left_of_position(self, input_matrix, expected):
        # WHEN
        left = create_left_of_position(1, 4, input_matrix)

        # THEN
        self.assertListEqual(left, expected)

    @parameterized.expand(
        [
            (matrix_0, [3, 9, 0]),
            (matrix_1, [6, 5, 3]),
        ]
    )
    def test_create_right_of_position(self, input_matrix, expected):
        # WHEN
        right = create_right_of_position(4, 1, input_matrix)

        # THEN
        self.assertListEqual(right, expected)

    @parameterized.expand(
        [
            (matrix_0, 3),
            (matrix_1, 3),
        ]
    )
    def test_create_viewing_up_of_position(self, input_matrix, expected):
        # WHEN
        viewing_up = create_viewing_up_of_position(3, 3, input_matrix)

        # THEN
        self.assertEqual(viewing_up, expected)

    @parameterized.expand(
        [
            (matrix_0, 1),
            (matrix_1, 2),
        ]
    )
    def test_create_viewing_down_of_position(self, input_matrix, expected):
        # WHEN
        viewing_down = create_viewing_down_of_position(1, 1, input_matrix)

        # THEN
        self.assertEqual(viewing_down, expected)

    @parameterized.expand(
        [
            (matrix_0, 2),
            (matrix_1, 1),
        ]
    )
    def test_create_viewing_left_of_position(self, input_matrix, expected):
        # WHEN
        viewing_left = create_viewing_left_of_position(1, 4, input_matrix)

        # THEN
        self.assertEqual(viewing_left, expected)

    @parameterized.expand(
        [
            (matrix_0, 2),
            (matrix_1, 3),
        ]
    )
    def test_create_viewing_right_of_position(self, input_matrix, expected):
        # WHEN
        viewing_right = create_viewing_right_of_position(4, 1, input_matrix)

        # THEN
        self.assertEqual(viewing_right, expected)
