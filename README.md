# huff-cli

<p align="center">
  <a href="https://github.com/ilindan-dev/huff-cli/actions/workflows/ci.yml"><img src="https://github.com/ilindan-dev/huff-cli/actions/workflows/ci.yml/badge.svg" alt="CI Status"></a>
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
  <a href="https://github.com/ilindan-dev/huff-cli/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License: MIT"></a>
</p>


A command-line tool for data compression based on the Huffman algorithm.

This project provides a CLI utility to encode (compress) and decode (decompress) text files using Huffman coding.

## Features

-   **Encode:** Compresses ASCII text files into a binary format.
-   **Decode:** Decompresses files back to the original text.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/ilindan-dev/huff-cli/huff-cli.git
    cd huff-cli
    ```
2.  Install the project in editable mode (recommended for development):
    ```bash
    pip install -e .
    ```
    This command reads the `pyproject.toml` file, installs dependencies, and makes the `huff-cli` command available in your terminal.

## Usage

The CLI has two main commands: `encode` and `decode`.

### Encode a file

```bash
huff-cli encode [INPUT_FILE] [OUTPUT_FILE] --print-tree
```

### Decode a file
```bash
huff-cli decode [INPUT_FILE] [OUTPUT_FILE] --print-tree
```

