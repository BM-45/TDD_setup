# TDD Setup - Scientific Calculator

A Test-Driven Development (TDD) implementation of a scientific calculator in Python with continuous integration and deployment using GitHub Actions.

## Overview

This project demonstrates best practices in software development through:
- Test-Driven Development methodology
- Comprehensive unit testing
- Continuous Integration/Continuous Deployment (CI/CD)
- Clean code architecture
- Automated testing workflows

## Features

### Calculator Operations
- Basic arithmetic (addition, subtraction, multiplication, division)
- Scientific functions (trigonometry, logarithms, exponents)
- Memory operations
- Error handling for invalid inputs
- Precision control for floating-point calculations

### Development Features
- Complete test coverage
- Automated testing with GitHub Actions
- Code quality checks
- Continuous integration pipeline
- Documentation generation

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

## Usage

### Using the Calculator

```python
from calculator import Calculator

# Create calculator instance
calc = Calculator()

# Basic operations
result = calc.add(5, 3)          # 8
result = calc.subtract(10, 4)    # 6
result = calc.multiply(3, 7)     # 21
result = calc.divide(15, 3)      # 5.0

# Scientific operations
result = calc.sin(0)             # 0.0
result = calc.cos(0)             # 1.0
result = calc.log(100, 10)       # 2.0
result = calc.power(2, 8)        # 256
```

### Running Tests

Run all tests:
```bash
pytest
```

Run tests with coverage report:
```bash
pytest --cov=calculator --cov-report=html
```

Run specific test file:
```bash
pytest test_calculator.py
```

Run tests in verbose mode:
```bash
pytest -v
```

## Test-Driven Development Workflow

This project follows the TDD cycle:

1. **Red** - Write a failing test
2. **Green** - Write minimal code to pass the test
3. **Refactor** - Improve the code while keeping tests passing

### Example TDD Process

```python
# Step 1: Write failing test
def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

# Step 2: Implement minimal code
class Calculator:
    def add(self, a, b):
        return a + b

# Step 3: Refactor if needed
class Calculator:
    def add(self, a: float, b: float) -> float:
        """Add two numbers and return the result."""
        return a + b
```

## Continuous Integration

GitHub Actions automatically runs tests on:
- Every push to the repository
- Every pull request
- Multiple Python versions (3.8, 3.9, 3.10, 3.11)

### CI Pipeline Steps

1. Code checkout
2. Python environment setup
3. Dependency installation
4. Linting and style checks
5. Test execution
6. Coverage report generation
7. Build verification

### Viewing CI Results

Check the [Actions tab](https://github.com/BM-45/TDD_setup/actions) to see:
- Build status
- Test results
- Coverage reports
- Workflow history

## Code Quality

### Running Linters

```bash
# Check code style with flake8
flake8 calculator.py test_calculator.py

# Analyze code with pylint
pylint calculator.py
```

## Test Coverage

Target: 100% code coverage

Current coverage includes:
- All calculator operations
- Edge cases and error conditions
- Input validation
- Exception handling

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Write tests first (TDD approach)
4. Implement the feature
5. Ensure all tests pass
6. Submit a pull request

### Contribution Checklist

- [ ] Tests written and passing
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] CI pipeline passes
- [ ] Coverage maintained or improved

## Best Practices Demonstrated

- **TDD Methodology** - Tests written before implementation
- **Clean Code** - Readable, maintainable code structure
- **SOLID Principles** - Single responsibility, proper abstraction
- **CI/CD Integration** - Automated testing and deployment
- **Version Control** - Proper Git workflow and commits
- **Documentation** - Clear comments and README

## Learning Resources

- [Test-Driven Development by Example](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530) by Kent Beck
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub Actions Documentation](https://docs.github.com/actions)
- [Python Testing Best Practices](https://docs.python-guide.org/writing/tests/)

## Troubleshooting

### Common Issues

**Tests not running:**
- Ensure pytest is installed: `pip install pytest`
- Check Python version compatibility

**Import errors:**
- Verify virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

**CI failures:**
- Check Actions tab for detailed logs
- Ensure all tests pass locally first
- Verify requirements.txt is up to date

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by TDD and clean code principles
- Thanks to the Python testing community
- GitHub Actions for CI/CD support

---

**Built with ❤️ using Test-Driven Development**
