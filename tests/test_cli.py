import filecmp

import pytest
import argparse
import pickle
import os

from huff_cli import cli, core


def test_encode_integration(tmp_path):
    """
    Tests that the encode workflow produces a file with the correct frequency map
    and that the data within can be successfully decoded back to the original text.
    """
    # 1. Arrange
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.bin"
    original_text = "abracadabra"

    input_file.write_text(original_text, encoding="ascii")

    args = argparse.Namespace(
        input=str(input_file), output=str(output_file), print_tree=False
    )

    golden_freq_map = {"a": 5, "b": 2, "r": 2, "c": 1, "d": 1}
    golden_byte_array = bytearray(b"\x01J\xce\x94")

    # 2. Act
    cli.encode_workflow(args)

    # 3. Assert
    assert os.path.exists(output_file)

    with open(output_file, "rb") as f:
        freq_map, byte_array = pickle.load(f)
    assert freq_map == golden_freq_map

    rebuilt_tree = core.build_huffman_tree(freq_map)
    decoded_text = core.decode_text(byte_array, rebuilt_tree)
    assert decoded_text == original_text


def test_decode_reverses_encode(tmp_path):
    """
    Full end-to-end test. Verifies that the `decode` command correctly
    reconstructs a file created by the `encode` command.
    """

    input_file = tmp_path / "input.txt"
    compressed_file = tmp_path / "output.bin"
    decoded_file = tmp_path / "decoded.txt"
    original_text = "full cycle test: encode then decode"
    input_file.write_text(original_text, encoding="ascii")

    encode_args = argparse.Namespace(
        input=str(input_file), output=str(compressed_file), print_tree=False
    )
    cli.encode_workflow(encode_args)

    decode_args = argparse.Namespace(
        input=str(compressed_file), output=str(decoded_file), print_tree=False
    )
    cli.decode_workflow(decode_args)

    assert os.path.exists(decoded_file)
    assert filecmp.cmp(input_file, decoded_file, shallow=False)
