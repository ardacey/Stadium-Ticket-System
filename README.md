# Stadium Ticket System

A small command-line ticket manager for stadium seating. The program reads a command file, updates category layouts and ticket sales, and writes the results to `output.txt` while also printing them to the console.

## Features

- Create seating categories with custom row and column sizes
- Sell individual seats or seat ranges
- Cancel sold tickets
- Print category balance reports
- Display the current seat layout for any category

## Requirements

- Python 3

## Usage

Run the script with an input file that contains one command per tokenized line:

```powershell
python "Stadium Ticket System.py" input_example.txt
```

The program creates `output.txt` in the project root every time it runs.

## Command Format

- `CREATECATEGORY <category-name> <rows>x<columns>`
- `SELLTICKET <customer-name> <student|full|season> <category-name> <seat-or-range...>`
- `CANCELTICKET <category-name> <seat-or-range...>`
- `BALANCE <category-name>`
- `SHOWCATEGORY <category-name>`

Seat references use a row letter followed by a column number. Ranges use the form `A0-6`.

## Example

Sample input and output files are included in the repository:

- `input_example.txt`
- `output_example.txt`

Use them to verify the program behavior or as a starting point for your own input files.

## Notes

- Generated output is written to `output.txt`, which is ignored by Git.
- The script is intentionally lightweight and has no external dependencies.
