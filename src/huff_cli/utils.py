from . import core


def print_tree(node: core.HuffmanNode, prefix="", is_left=True):
    if node is None:
        return

    if node.right:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)

    char_repr = f"'{node.char}'" if node.char is not None else "INT"
    print(prefix + ("└── " if is_left else "┌── ") + f"({char_repr}, {node.freq})")

    if node.left:
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)
