import csv
import tempfile
import unittest
from pathlib import Path

from src.universal_functions.spreadsheet_stuff.convert_csv_file_into_tsv_file import (
    convert_csv_file_into_tsv_file,
)


class TestConvertCsvFileIntoTsvFile(unittest.TestCase):
    def test_converts_csv_rows_to_tsv_rows(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path_to_csv_file = Path(temp_dir) / "example.csv"
            path_to_tsv_file = Path(temp_dir) / "example.tsv"

            with open(path_to_csv_file, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["name", "notes"])
                writer.writerow(["Baxter Stockman", "flying, prone weakness"])

            result = convert_csv_file_into_tsv_file(
                path_to_csv_file=path_to_csv_file,
                path_to_tsv_file=path_to_tsv_file
            )

            with open(path_to_tsv_file, newline="", encoding="utf-8") as file:
                rows = list(csv.reader(file, delimiter="\t"))

            self.assertEqual(str(path_to_tsv_file), result)
            self.assertEqual(
                [
                    ["name", "notes"],
                    ["Baxter Stockman", "flying, prone weakness"],
                ],
                rows
            )

    def test_uses_tsv_suffix_when_output_path_is_blank(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path_to_csv_file = Path(temp_dir) / "example.csv"

            with open(path_to_csv_file, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["name"])
                writer.writerow(["Hoopmaster"])

            result = convert_csv_file_into_tsv_file(
                path_to_csv_file=path_to_csv_file
            )

            self.assertEqual(str(Path(temp_dir) / "example.tsv"), result)
            self.assertTrue((Path(temp_dir) / "example.tsv").exists())


if __name__ == "__main__":
    unittest.main()
