import unittest

from parameterized import parameterized

from day6.main import find_start_of_message_marker, find_start_of_packet_marker


class TestDay6(unittest.TestCase):
    @parameterized.expand(
        [
            ("first", "mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
            ("second", "bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
            ("third", "nppdvjthqldpwncqszvftbrmjlhg", 6),
            ("forth", "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
            ("fifth", "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
        ]
    )
    def test_find_start_of_packet_marker(self, name: str, signal: str, actual_result: int):
        # WHEN
        start_of_packet_marker = find_start_of_packet_marker(signal)

        # THEN
        self.assertEqual(start_of_packet_marker, actual_result)

    @parameterized.expand(
        [
            ("first", "mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
            ("second", "bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
            ("third", "nppdvjthqldpwncqszvftbrmjlhg", 23),
            ("forth", "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
            ("fifth", "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
        ]
    )
    def test_find_start_of_message_marker(self, name: str, signal: str, actual_result: int):
        # WHEN
        start_of_message_marker = find_start_of_message_marker(signal)

        # THEN
        self.assertEqual(start_of_message_marker, actual_result)
