import csv
import tempfile
import unittest
from pathlib import Path

from src.universal_functions.spreadsheet_stuff.spreadsheet_updaters.update_encounter_feedback_spreadsheet import (
    update_encounter_feedback_spreadsheet,
)


class TestUpdateEncounterFeedbackSpreadsheet(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path_to_csv_file = Path(self.temp_dir.name) / "encounter_feedback.csv"
        self.fieldnames = [
            "encounter_name",
            "party_level",
            "party_size",
            "predicted_difficulty",
            "actual_difficulty",
            "monster_count",
            "total_monster_xp",
            "adjusted_xp",
            "rounds",
            "notes",
        ]

        with open(self.path_to_csv_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerow(
                {
                    "encounter_name": "old_encounter",
                    "party_level": "4",
                    "party_size": "4",
                    "predicted_difficulty": "medium",
                    "actual_difficulty": "easy",
                    "monster_count": "3",
                    "total_monster_xp": "300",
                    "adjusted_xp": "600",
                    "rounds": "2",
                    "notes": "Original notes.",
                }
            )

    def tearDown(self):
        self.temp_dir.cleanup()

    def get_rows(self):
        with open(self.path_to_csv_file, newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    def test_adds_new_encounter_row(self):
        update_encounter_feedback_spreadsheet(
            encounter_dict={
                "encounter_name": "new_encounter",
                "party_level": 5,
                "party_size": 4,
                "predicted_difficulty": "hard",
                "actual_difficulty": "medium",
                "adjusted_xp": 1800,
            },
            path_to_encounter_feedback_csv_file=self.path_to_csv_file,
        )

        rows = self.get_rows()

        self.assertEqual(2, len(rows))
        self.assertEqual("new_encounter", rows[1]["encounter_name"])
        self.assertEqual("5", rows[1]["party_level"])
        self.assertEqual("1800", rows[1]["adjusted_xp"])

    def test_overwrites_duplicate_by_encounter_name(self):
        update_encounter_feedback_spreadsheet(
            encounter_dict={
                "encounter_name": "OLD_ENCOUNTER",
                "party_level": 6,
                "actual_difficulty": "deadly",
                "notes": "Updated notes.",
            },
            path_to_encounter_feedback_csv_file=self.path_to_csv_file,
            duplicate_action="overwrite",
        )

        rows = self.get_rows()

        self.assertEqual(1, len(rows))
        self.assertEqual("OLD_ENCOUNTER", rows[0]["encounter_name"])
        self.assertEqual("6", rows[0]["party_level"])
        self.assertEqual("deadly", rows[0]["actual_difficulty"])
        self.assertEqual("Updated notes.", rows[0]["notes"])

    def test_stop_duplicate_does_not_write(self):
        with self.assertRaises(SystemExit):
            update_encounter_feedback_spreadsheet(
                encounter_dict={
                    "encounter_name": "old_encounter",
                    "party_level": 10,
                    "actual_difficulty": "deadly",
                },
                path_to_encounter_feedback_csv_file=self.path_to_csv_file,
                duplicate_action="stop",
            )

        rows = self.get_rows()

        self.assertEqual(1, len(rows))
        self.assertEqual("4", rows[0]["party_level"])
        self.assertEqual("easy", rows[0]["actual_difficulty"])


if __name__ == "__main__":
    unittest.main()
