import argparse

from . import core
from . import io_handler
from . import utils


def encode_workflow(args):
    """Workflow for the encoding process."""
    print(f"Reading file: {args.input}")
    text = io_handler.read_text_file(args.input)
    if text is None:
        return

    if not text:
        print("File is empty. Creating an empty compressed file.")
        io_handler.write_compressed_file(args.output, ({}, bytearray()))
        return

    print("Building Huffman tree and generating codes...")
    freq_map = core.build_frequency_map(text)
    huffman_tree = core.build_huffman_tree(freq_map)
    codes = core.generate_huffman_codes(huffman_tree)

    if args.print_tree:
        print("\n--- Huffman Tree (Encode) ---")
        utils.print_tree(huffman_tree)
        print("---------------------------\n")

    encoded_text = core.get_encoded_text(text, codes)

    padded_text = core.pad_encoded_text(encoded_text)

    byte_array = core.text_to_byte_array(padded_text)

    io_handler.write_compressed_file(args.output, (freq_map, byte_array))

    print("\nEncoding complete!")
    original_size = len(text.encode("ascii"))
    compressed_size = len(byte_array)
    print(f"Original size: {original_size} bytes")
    print(f"Compressed size: {compressed_size} bytes")
    if compressed_size > 0:
        print(f"Compression ratio: {original_size / compressed_size:.2f}x")


def decode_workflow(args):
    """Workflow for the decoding process."""
    print(f"Reading compressed file: {args.input}")

    data_to_decode = io_handler.read_compressed_file(args.input)
    if data_to_decode is None:
        return

    freq_map, byte_array = data_to_decode

    if not freq_map:
        print("Compressed file is empty. Creating an empty output file.")
        io_handler.write_text_file(args.output, "")
        return

    print("Rebuilding Huffman tree and decoding data...")

    huffman_tree = core.build_huffman_tree(freq_map)

    if args.print_tree:
        print("\n--- Huffman Tree (Encode) ---")
        utils.print_tree(huffman_tree)
        print("---------------------------\n")

    decoded_text = core.decode_text(byte_array, huffman_tree)

    io_handler.write_text_file(args.output, decoded_text)

    print(f"\nDecoding complete! Output saved to: {args.output}")


def main():
    """Main function to parse arguments and call workflows."""
    parser = argparse.ArgumentParser(description="CLI for Huffman data compression.")
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available commands"
    )

    p_encode = subparsers.add_parser("encode", help="Encode a text file.")
    p_encode.add_argument("input", type=str, help="Input text file path.")
    p_encode.add_argument("output", type=str, help="Output compressed file path.")
    p_encode.add_argument(
        "--print-tree",
        action="store_true",
        help="Print the Huffman tree to the screen.",
    )
    p_encode.set_defaults(func=encode_workflow)

    p_decode = subparsers.add_parser("decode", help="Decode a compressed file.")
    p_decode.add_argument("input", type=str, help="Input compressed file path.")
    p_decode.add_argument("output", type=str, help="Output decoded text file path.")
    p_decode.add_argument(
        "--print-tree",
        action="store_true",
        help="Print the reconstructed Huffman tree.",
    )
    p_decode.set_defaults(func=decode_workflow)

    args = parser.parse_args()
    args.func(args)


def run():
    """Entry point for the console script."""
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
