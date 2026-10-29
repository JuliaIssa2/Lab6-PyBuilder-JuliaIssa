# Lab 6 – Automatic Build Using PyBuilder

## Student Information

**Student:** Julia Issa  
**Lab:** Lab 6 – Automatic Build  
**Topic:** Using PyBuilder for Python Build Automation

---

## Project Overview

This project demonstrates how PyBuilder can be used to automate the build and testing process of a Python application.

The project consists of a calculator implemented in Python. In addition to the basic arithmetic operations, the calculator was extended with modulus, exponentiation, and square root operations as required by the lab.

PyBuilder is configured through the `build.py` file and is responsible for discovering and executing the project's unit tests.

---

## Calculator Operations

The calculator implements the following operations:

- **Addition** – Adds two numbers.
- **Subtraction** – Subtracts the second number from the first.
- **Multiplication** – Multiplies two numbers.
- **Division** – Divides the first number by the second.
- **Modulus** – Returns the remainder after division.
- **Exponentiation** – Raises a number to a specified power.
- **Square Root** – Calculates the square root of a number.

The implementation also handles invalid operations such as division by zero and attempting to calculate the square root of a negative number.

---

## Project Structure

```text
calculator_Julia_Issa/
│
├── build.py
├── .gitignore
│
├── screenshots/
│   └── Screenshot (813).png
│
├── src/
│   └── main/
│       └── python/
│           └── calculator_Julia_Issa/
│               └── __init__.py
│
└── tests/
    ├── __init__.py
    └── unittest/
        ├── __init__.py
        └── calculator_Julia_Issa/
            ├── __init__.py
            └── test_calculator_Julia_Issa.py
```

Generated PyBuilder directories such as `target/`, `.pybuilder/`, and Python `__pycache__/` directories are excluded from version control using `.gitignore`.

---

## Requirements

The project was developed and tested with:

- Python 3.11
- PyBuilder 0.13.24
- Python `unittest`

PyBuilder can be installed with:

```bash
python -m pip install pybuilder
```

The installed version can be checked with:

```bash
pyb --version
```

---

## Running the Unit Tests

Open a terminal in the root directory of the project:

```text
calculator_Julia_Issa
```

Then run:

```bash
pyb run_unit_tests
```

PyBuilder reads the project configuration from `build.py`, prepares the required environment, discovers the unit tests, and executes them automatically.

---

## Unit Testing

The project contains **10 unit tests** covering the calculator functionality.

The tests verify the behavior of the implemented arithmetic operations, including the additional operations required for the lab.

The final PyBuilder execution produced:

```text
Executed 10 unit tests
All unit tests passed.

BUILD SUCCESSFUL
```

This confirms that the calculator implementation and its unit tests complete successfully through the automated PyBuilder process.

---

## Successful Build

The final build was executed using:

```bash
pyb run_unit_tests
```

The successful execution reported:

```text
Project: calculator_Julia_Issa
Version: 0.1.0
Base directory: c:\users\acer\desktop\calculator_julia_issa

Executed 10 unit tests
All unit tests passed.

BUILD SUCCESSFUL
```

A screenshot showing the successful PyBuilder execution is included in the repository under the `screenshots` directory.

### Build Screenshot

![Successful PyBuilder Build](screenshots/Screenshot%20%28813%29.png)

---

## Build Automation

The `build.py` file contains the PyBuilder configuration for the project.

The automated build process performs the required preparation and source compilation steps before executing the unit tests. This provides a repeatable way of validating the calculator project without manually running individual test files.

The final build successfully completed the following tasks:

```text
prepare
compile_sources
run_unit_tests
```

---

## Result

The completed project demonstrates a working automated Python build process using PyBuilder.

The calculator includes the required arithmetic functionality and extensions, the unit tests execute automatically through PyBuilder, and all **10 unit tests pass successfully**.
