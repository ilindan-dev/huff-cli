import pickle
from typing import Tuple, Optional


def read_text_file(path: str) -> Optional[str]:
    # Reads a text file in ASCII encoding.
    try:
        with open(path, mode="r", encoding="ascii", errors="ignore") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except IOError as e:
        print(f"Error reading from file '{path}': {e}")
        return None


def write_compressed_file(path: str, data: Tuple[dict, bytearray]):
    # Writes compressed data to a binary file.
    try:
        with open(path, mode="wb") as f:
            pickle.dump(data, f)
    except IOError as e:
        print(f"Error writing to file '{path}': {e}")


def read_compressed_file(path: str) -> Optional[Tuple[dict, bytearray]]:
    # Reads a compressed binary file.
    try:
        with open(path, mode="rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except (pickle.UnpicklingError, EOFError, TypeError):
        print(f"Error: File '{path}' is damaged or has an incorrect format.")
        return None
    except IOError as e:
        print(f"Error reading from file '{path}': {e}")
        return None


def write_text_file(path: str, text: str):
    # Writes plain text to a file.
    try:
        with open(path, mode="w", encoding="ascii") as f:
            f.write(text)
    except IOError as e:
        print(f"Error writing to file '{path}': {e}")
