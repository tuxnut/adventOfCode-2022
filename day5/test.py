import unittest

from day5.main import parse_initial_state, place_crates_into_column, remove_crates_from_column


class TestDay5(unittest.TestCase):
    def test_parse_initial_state(self):
        # GIVEN
        file_content = [
            "    [D]",
            "[N] [C]",
            "[Z] [M] [P]",
        ]

        # WHEN
        state = parse_initial_state(file_content, 3)

        # THEN
        self.assertDictEqual(
            state,
            {
                "1": "ZN",
                "2": "MCD",
                "3": "P",
            },
        )

    def test_remove_crates_from_column(self):
        # GIVEN
        state = {
            "1": "ZN",
            "2": "MCD",
            "3": "P",
        }
        number_of_crates_to_move = 2
        source = "2"

        # WHEN
        new_state, removed_crates = remove_crates_from_column(state, number_of_crates_to_move, source)

        # THEN
        self.assertDictEqual(
            new_state,
            {
                "1": "ZN",
                "2": "M",
                "3": "P",
            },
        )
        self.assertEqual(removed_crates, "CD")

    def test_place_crates_into_column(self):
        # GIVEN
        state = {
            "1": "ZN",
            "2": "M",
            "3": "P",
        }
        crates = "HTR"
        destination = "3"

        # WHEN
        new_state = place_crates_into_column(state, crates, destination)

        # THEN
        self.assertDictEqual(
            new_state,
            {
                "1": "ZN",
                "2": "M",
                "3": "PHTR",
            },
        )
