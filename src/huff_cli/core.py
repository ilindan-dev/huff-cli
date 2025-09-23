import heapq
from collections import Counter


class HuffmanNode:
    """A class for representing a node in a Huffman tree."""
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_map(text: str) -> dict:
    """Builds a frequency map of the symbols"""
    return Counter(text)


def build_huffman_tree(freq_map: dict) -> HuffmanNode:
    """Builds a Huffman tree based on a frequency map."""
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged_freq = left.freq + right.freq
        merged_node = HuffmanNode(None, merged_freq, left, right)

        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0] if priority_queue else None


def _generate_codes_recursive(node: HuffmanNode, prefix: str, codes: dict):
    """A recursive helper for generating codes."""
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = prefix or "0"

    _generate_codes_recursive(node.left, prefix + "0", codes)
    _generate_codes_recursive(node.right, prefix + "1", codes)


def generate_huffman_codes(tree: HuffmanNode) -> dict:
    """Generates Huffman codes from a tree."""
    codes = {}
    _generate_codes_recursive(tree, "", codes)
    return codes


def get_encoded_text(text: str, codes: dict) -> str:
    """Converts the source text to a string of '0' and '1'."""
    return "".join(codes[char] for char in text)


def pad_encoded_text(encoded_text: str) -> str:
    """
    Complements the encoded string to a multiple of 8 bits.
    8 bits of information about the number of added zeros are added to the beginning.
    """
    padding_amount = 8 - (len(encoded_text) % 8)
    if padding_amount == 8:
        padding_amount = 0

    padded_info = f"{padding_amount:08b}"

    padded_text = encoded_text + ('0' * padding_amount)

    return padded_info + padded_text


def text_to_byte_array(padded_text: str) -> bytearray:
    """Converts the augmented string from '0' and '1' into an array of bytes."""
    b = bytearray(int(padded_text[i:i + 8], 2) for i in range(0, len(padded_text), 8))
    return b


def decode_text(encoded_bytes: bytearray, huffman_tree: HuffmanNode) -> str:
    """Decodes a byte array using the Huffman tree to get the original text."""
    if not encoded_bytes or not huffman_tree:
        return ""

    bit_string = "".join(f"{byte:08b}" for byte in encoded_bytes)

    padding_amount = int(bit_string[:8], 2)
    bit_string = bit_string[8:]

    if padding_amount > 0:
        encoded_data = bit_string[:-padding_amount]
    else:
        encoded_data = bit_string

    decoded_chars = []
    current_node = huffman_tree

    if not current_node.left and not current_node.right:
        return current_node.char * len(encoded_data)

    for bit in encoded_data:
        current_node = current_node.left if bit == '0' else current_node.right


        if current_node.char is not None:
            decoded_chars.append(current_node.char)
            current_node = huffman_tree

    return "".join(decoded_chars)