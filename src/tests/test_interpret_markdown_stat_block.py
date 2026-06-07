import tempfile
import unittest
from pathlib import Path

from src.universal_functions.stat_block_interpreter.interpret_markdown_stat_block import (
    interpret_markdown_stat_block_into_python_file,
    parse_markdown_stat_block,
)


class TestInterpretMarkdownStatBlock(unittest.TestCase):
    def test_parse_template_stat_block(self):
        parsed_stat_block = parse_markdown_stat_block(
            path_to_markdown_file="docs/stat_block_interpreter_template.md"
        )

        self.assertEqual(
            "Template Monster, Parser Trial",
            parsed_stat_block["metadata"]["name"]
        )
        self.assertEqual(-1, parsed_stat_block["ability_scores"]["str_modifier"])
        self.assertEqual(["radiant"], parsed_stat_block["wri"]["weak"])
        self.assertEqual(["fire", "necrotic"], parsed_stat_block["wri"]["resistant"])
        self.assertEqual("test spark", parsed_stat_block["actions"][0]["name"])
        self.assertIn(
            "jokes i refuse to delete",
            [section.lower() for section in parsed_stat_block["ignored_sections"]]
        )

    def test_interpreter_writes_enum_backed_python_dictionary_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path_to_python_file = Path(temp_dir) / "template_monster.py"

            monster_properties = interpret_markdown_stat_block_into_python_file(
                path_to_markdown_file="docs/stat_block_interpreter_template.md",
                path_to_python_file=path_to_python_file,
                dict_variable_name="template_monster_dict"
            )

            python_file_text = path_to_python_file.read_text(encoding="utf-8")

            self.assertEqual("Template Monster, Parser Trial", monster_properties["name"])
            self.assertTrue(path_to_python_file.exists())
            self.assertIn("spreadsheet_enums.SpreadsheetKeysEnums.NAME.value", python_file_text)
            self.assertIn("spreadsheet_enums.SizeEnums.SMALL.value", python_file_text)
            self.assertIn("spreadsheet_enums.CreatureTypesEnums.CONSTRUCT.value", python_file_text)
            self.assertIn("spreadsheet_enums.WRIEnums.RADIANT_WEAKNESS.value", python_file_text)
            self.assertIn('"actions"', python_file_text)

    def test_missing_languages_defaults_to_common(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path_to_markdown_file = Path(temp_dir) / "no_languages.md"
            path_to_python_file = Path(temp_dir) / "no_languages.py"

            path_to_markdown_file.write_text(
                "\n".join(
                    [
                        "# No Languages Monster",
                        "# metadata",
                        "name: No Languages Monster",
                        "# core stats",
                        "size: medium",
                        "type: beast",
                        "hp: 10",
                        "ac: 10",
                        "# ability scores",
                        "str_numeric_stat: 10",
                        "dex_numeric_stat: 10",
                        "con_numeric_stat: 10",
                        "int_numeric_stat: 10",
                        "wis_numeric_stat: 10",
                        "cha_numeric_stat: 10",
                    ]
                ),
                encoding="utf-8"
            )

            monster_properties = interpret_markdown_stat_block_into_python_file(
                path_to_markdown_file=path_to_markdown_file,
                path_to_python_file=path_to_python_file
            )

            self.assertEqual(["common"], monster_properties["languages"])


if __name__ == "__main__":
    unittest.main()
