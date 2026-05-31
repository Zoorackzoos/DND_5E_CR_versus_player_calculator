import csv
import tempfile
import unittest
from pathlib import Path

from src.universal_functions.spreadsheet_stuff.update_homebrew_monster_spreadsheet import (
    update_homebrew_monster_spreadsheet,
)


class TestUpdateHomebrewMonsterSpreadsheet(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path_to_csv_file = Path(self.temp_dir.name) / "monsters.csv"
        self.fieldnames = [
            "Name",
            "CR",
            "HP",
            "AC",
            "average_damage",
            "attack_modifier",
        ]

        with open(self.path_to_csv_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerow(
                {
                    "Name": "Old Monster",
                    "CR": "1",
                    "HP": "30",
                    "AC": "12",
                    "average_damage": "9",
                    "attack_modifier": "3",
                }
            )

    def tearDown(self):
        self.temp_dir.cleanup()

    def get_rows(self):
        with open(self.path_to_csv_file, newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    def test_adds_new_monster_row(self):
        update_homebrew_monster_spreadsheet(
            monster_dict={
                "Name": "New Monster",
                "CR": 2,
                "hp": 45,
                "ac": 14,
                "average_damage": 15,
                "attack_modifier": 4,
            },
            path_to_csv_file=self.path_to_csv_file,
        )

        rows = self.get_rows()

        self.assertEqual(2, len(rows))
        self.assertEqual("New Monster", rows[1]["Name"])
        self.assertEqual("45", rows[1]["HP"])
        self.assertEqual("14", rows[1]["AC"])

    def test_overwrites_duplicate_by_name(self):
        update_homebrew_monster_spreadsheet(
            monster_dict={
                "Name": "old monster",
                "CR": 3,
                "HP": 80,
                "AC": 16,
            },
            path_to_csv_file=self.path_to_csv_file,
            duplicate_action="overwrite",
        )

        rows = self.get_rows()

        self.assertEqual(1, len(rows))
        self.assertEqual("old monster", rows[0]["Name"])
        self.assertEqual("80", rows[0]["HP"])
        self.assertEqual("16", rows[0]["AC"])

    def test_stop_duplicate_does_not_write(self):
        with self.assertRaises(SystemExit):
            update_homebrew_monster_spreadsheet(
                monster_dict={
                    "Name": "Old Monster",
                    "CR": 10,
                    "HP": 500,
                },
                path_to_csv_file=self.path_to_csv_file,
                duplicate_action="stop",
            )

        rows = self.get_rows()

        self.assertEqual(1, len(rows))
        self.assertEqual("1", rows[0]["CR"])
        self.assertEqual("30", rows[0]["HP"])


if __name__ == "__main__":
    unittest.main()
