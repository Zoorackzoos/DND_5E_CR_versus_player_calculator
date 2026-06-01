import csv


def convert_csv_file_into_tsv_file(path_to_csv_file,
                                    path_to_tsv_file,
                                    tab_amount="\t"):
    with open("encounter_feedback.tsv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)