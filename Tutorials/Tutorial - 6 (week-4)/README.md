# Tax Calculator (Flowchart Implementation)

A minimal Python command-line program that computes income tax according to the provided flowchart. The script is intentionally compact, readable, and suitable for coursework or small demonstrations.

## Overview

This project implements a three-tier tax schedule:
- 2.0% for income up to and including 20,000
- 2.5% on the next portion for income from 20,001 to 50,000, with a base of 400 for the first 20,000
- 3.5% for income above 50,000, with a cumulative base to account for prior brackets

The program reads a taxable income value from the user, validates the input, computes the tax using the bracket logic, and prints the result formatted to two decimal places.

## Files

- `tax_calc.py` — main script. Prompts for income input and prints computed tax.
- `README.md` — this file.

## Requirements

- Python 3.6 or newer

## Usage

1. Open a terminal in the project folder:
   cd "c:\Parth\University of Canberra\University of Canberra\Semester 1\Core Subjects 4\IIT\Tutorials\Tutorial - 6 (week-4)"

2. Run:
   py -3 tax_calc.py
   or
   python tax_calc.py

3. Enter a numeric income when prompted. The program prints the tax amount.

Example:
```
Enter taxable income: 45000
Tax = $512.50
```

## Behavior and Validation

- Accepts decimal or integer numeric input.
- On invalid (non-numeric) input, the program prints an error and exits with a non-zero status.
- Output is shown with two decimal places and a dollar sign.

## Implementation Notes

- The tax calculation uses a concise conditional expression combining bracket bases and rates to match the flowchart logic.
- The script is written as a small, self-contained CLI (if __name__ == "__main__":) so it can be imported without side effects.

## Testing

Run the script with representative inputs to verify:
- Low income (e.g., 15000) -> 2% of income
- Mid-range income (e.g., 30000) -> base 400 + 2.5% on amount above 20000
- High income (e.g., 80000) -> cumulative base + 3.5% on amount above 50000

## License

Use and modify for coursework. No warranty provided.

## Contact

For questions about this implementation, inspect `tax_calc.py