import pytest
from huff_cli.core import (
    HuffmanNode,
    build_frequency_map,
    build_huffman_tree,
    generate_huffman_codes,
)

def test_generate_huffman_codes_standard_case():
    """
    It tests the generation of codes for the standard case with several characters.
    """
    freq_map = {"a": 3, "b": 2, "c": 1}
    huffman_tree = build_huffman_tree(freq_map)
    expected_codes = {"a": "0", "b": "11", "c": "10"}

    actual_codes = generate_huffman_codes(huffman_tree)

    assert actual_codes == expected_codes

def test_generate_huffman_codes_single_character():
    """
    It tests the generation of codes for the standard case with several characters.
    """
    freq_map = {"a": 5}
    huffman_tree = build_huffman_tree(freq_map)
    expected_codes = {"a": "0"}

    actual_codes = generate_huffman_codes(huffman_tree)

    assert actual_codes == expected_codes

def test_generate_huffman_codes_empty_text():
    """
    It tests the generation of codes for the standard case with several characters.
    """
    huffman_tree = build_huffman_tree({})
    expected_codes = {}

    actual_codes = generate_huffman_codes(huffman_tree)

    assert actual_codes == expected_codes