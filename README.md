# CSV Report Generator

A lightweight Python command-line tool for generating reports from CSV files.

## Features

- Counts rows and columns
- Detects empty cells in each column
- Calculates sum and average for numeric columns
- Saves reports to a text file
- Handles missing input files
- Includes automated unit tests

## Requirements

- Python 3.8 or newer
- No third-party packages required

## Usage

Generate a report:

    python csv_report.py sample.csv

Choose an output filename:

    python csv_report.py sample.csv --output my_report.txt

## Run Tests

    python -m unittest discover -s tests -v

## License

MIT
