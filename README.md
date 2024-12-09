# Python MD4 Implementation

A lightweight and efficient implementation of the MD4 cryptographic hash function in Python. This repository provides an educational, Python-based implementation of MD4 for learning purposes, cryptographic research, or retrocompatibility with legacy systems.

## Features

- **Pure Python** implementation for portability.
- Follows the original MD4 algorithm specification.
- Includes test cases to validate functionality.

## Usage

### Installation
Clone the repository:
```bash
git clone https://github.com/timothyjxhn/MD4_Python.git
cd MD4_Python
```

### Running the MD4 Script
To run the MD4 script, use the following command:
```bash
python md4.py -h
```

This will display the help message with usage instructions. You can hash a string or a file using the following commands:

- Hash a string:
  ```bash
  python md4.py "your_string_here"
  ```

- Hash a file:
  ```bash
  python md4.py -f path/to/your/file
  ```

### Running the Test Cases
To run the test cases, use the following command:
```bash
python md4_test.py
```

All test case results were verified against the following online tool:
[CyberChef](https://gchq.github.io/CyberChef/)

### References
- [RFC 1320](https://www.rfc-editor.org/rfc/rfc1320.html)

---

**Disclaimer**: MD4 is considered cryptographically broken and unsuitable for secure applications. For educational and legacy support use cases only.
