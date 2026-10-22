
import csv
import argparse
from pathlib import Path


def generate_report(input_file):
    path = Path(input_file)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {input_file}")

    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file has no column headers.")

        headers = reader.fieldnames
        rows = list(reader)

    report = []
    report.append("CSV FILE REPORT")
    report.append("=" * 30)
    report.append(f"File: {path.name}")
    report.append(f"Rows: {len(rows)}")
    report.append(f"Columns: {len(headers)}")
    report.append("")
    report.append("EMPTY CELLS")

    for header in headers:
        empty_count = sum(
            1 for row in rows
            if not (row.get(header) or "").strip()
        )
        report.append(f"{header}: {empty_count}")

    report.append("")
    report.append("NUMERIC COLUMN STATISTICS")

    for header in headers:
        values = []

        for row in rows:
            value = (row.get(header) or "").strip()

            if not value:
                continue

            try:
                values.append(float(value))
            except ValueError:
                values = []
                break

        if values:
            total = sum(values)
            average = total / len(values)

            report.append(f"{header}:")
            report.append(f"  Count: {len(values)}")
            report.append(f"  Sum: {total:g}")
            report.append(f"  Average: {average:.2f}")

    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a report from a CSV file."
    )
    parser.add_argument("input_file", help="Path to the CSV file")
    parser.add_argument(
        "-o", "--output",
        default="report.txt",
        help="Output report file (default: report.txt)"
    )
    args = parser.parse_args()

    try:
        report = generate_report(args.input_file)
        Path(args.output).write_text(report + "\n", encoding="utf-8")
        print(report)
        print(f"\nReport saved to: {args.output}")

    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
