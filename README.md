# TDD Setup - Scientific Calculator

A Test-Driven Development (TDD) implementation of a scientific calculator in Python with continuous integration and deployment using GitHub Actions.

## Overview

This project demonstrates best practices in software development through:
- Test-Driven Development methodology
- Comprehensive unit testing
- Continuous Integration/Continuous Deployment (CI/CD)
- Clean code architecture
- Automated testing workflows



## Tech Stack

- **Python 3.x** - Programming language
- **pytest** - Testing framework
- **GitHub Actions** - CI/CD platform
- **coverage.py** - Code coverage analysis
- **pylint/flake8** - Code quality tools

## Project Structure

```
.
├── calculator.py           # Main calculator implementation
├── test_calculator.py      # Comprehensive test suite
├── .github/
│   └── workflows/
│       ├── ci.yml          # Continuous integration workflow
│       └── tests.yml       # Automated testing workflow
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Git for version control

## Installation

1. Clone the repository:
```bash
git clone https://github.com/BM-45/TDD_setup.git
cd TDD_setup
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```


## Test-Driven Development Workflow

This project follows the TDD cycle:

1. **Red** - Write a failing test
2. **Green** - Write minimal code to pass the test
3. **Refactor** - Improve the code while keeping tests passing
---
