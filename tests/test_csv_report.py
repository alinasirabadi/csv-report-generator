
import unittest
import tempfile
from pathlib import Path

from csv_report import generate_report


class TestCSVReport(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.csv_path = Path(self.temp_dir.name) / "sample.csv"

        self.csv_path.write_text(
            "name,age,salary\n"
            "Ali,25,1200\n"
            "Sara,30,1800\n"
            "Reza,,1500\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_counts_rows_and_columns(self):
        report = generate_report(self.csv_path)

        self.assertIn("Rows: 3", report)
        self.assertIn("Columns: 3", report)

    def test_reports_empty_cells(self):
        report = generate_report(self.csv_path)

        self.assertIn("age: 1", report)
        self.assertIn("name: 0", report)

    def test_calculates_numeric_statistics(self):
        report = generate_report(self.csv_path)

        self.assertIn("Sum: 55", report)
        self.assertIn("Average: 27.50", report)
        self.assertIn("Sum: 4500", report)

    def test_missing_file(self):
        missing = Path(self.temp_dir.name) / "missing.csv"

        with self.assertRaises(FileNotFoundError):
            generate_report(missing)


if __name__ == "__main__":
    unittest.main()
