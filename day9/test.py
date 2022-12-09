import unittest

from parameterized import parameterized

from day9.main import compute_tail_position


class TestDay9(unittest.TestCase):
    @parameterized.expand(
        [
            ((0, 0), (0, 0), (0, 0)),  # overlapping
            ((0, 1), (0, 0), (0, 0)),  # 1 y-axis
            ((1, 0), (0, 0), (0, 0)),  # 1 x-axis
            ((1, 1), (0, 0), (0, 0)),  # 1 x-axis + y-axis
            ((0, 2), (0, 0), (0, 1)),  # 2 pos y-axis
            ((0, -2), (0, 0), (0, -1)),  # 2 neg y-axis
            ((2, 0), (0, 0), (1, 0)),  # 2 pos x-axis
            ((-2, 0), (0, 0), (-1, 0)),  # 2 neg y-axis
            ((2, 1), (0, 0), (1, 1)),  # 2 x-axis + 1 y-axis
            ((2, -1), (0, 0), (1, -1)),  # 2 x-axis + 1 y-axis
            ((1, 2), (0, 0), (1, 1)),  # 1 x-axis + 2 y-axis
            ((-1, 2), (0, 0), (-1, 1)),  # 1 x-axis + 2 y-axis
            ((-2, -1), (0, 0), (-1, -1)),  # 2 x-axis + 1 y-axis
            ((-2, 1), (0, 0), (-1, 1)),  # 2 x-axis + 1 y-axis
            ((-1, -2), (0, 0), (-1, -1)),  # 1 x-axis + 2 y-axis
            ((1, -2), (0, 0), (1, -1)),  # 1 x-axis + 2 y-axis
        ]
    )
    def test_compute_tail_position(self, head_position, tail_position, expected):
        # WHEN
        result = compute_tail_position(tail_position, head_position)

        # THEN
        self.assertTupleEqual(result, expected)
