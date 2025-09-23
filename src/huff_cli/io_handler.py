import aiofiles
import pickle
from typing import Tuple, Optional


async def read_text_file(path: str) -> Optional[str]:
    """
    Asynchronously reads an ASCII-encoded text file.
    Returns the contents of the file, or None in case of an error.
    """
    try:
        async with aiofiles.open(path, mode="r", encoding="ascii") as f:
            return await f.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except UnicodeDecodeError:
        print(f"Error: File '{path}' contains non-ASCII characters.")
        return None


async def write_compressed_file(path: str, data: Tuple[dict, bytearray]):
    """
    Asynchronously writes compressed data to a binary file.
    Uses pickle to serialize a tuple (frequency map, byte array).
    """
    try:
        async with aiofiles.open(path, mode="wb") as f:
            await f.write(pickle.dumps(data))
    except IOError as e:
        print(f"Error writing to file '{path}': {e}")


async def read_compressed_file(path: str) -> Optional[Tuple[dict, bytearray]]:
    """
    Asynchronously reads a compressed binary file.
    Uses pickle to deserialize data into a tuple.
    """
    try:
        async with aiofiles.open(path, mode="rb") as f:
            content = await f.read()
            return pickle.loads(content)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except (pickle.UnpicklingError, EOFError, TypeError):
        print(f"Error: File '{path}' is damaged or has an incorrect format.")
        return None
    except IOError as e:
        print(f"Error reading from file '{path}': {e}")
        return None


async def write_text_file(path: str, text: str):
    """
    Asynchronously writes plain text to a file.
    """
    try:
        async with aiofiles.open(path, mode="w", encoding="ascii") as f:
            await f.write(text)
    except IOError as e:
        print(f"Error writing to file '{path}': {e}")
