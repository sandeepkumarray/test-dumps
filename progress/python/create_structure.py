import os
import argparse

def parse_structure(structure_file):
    """Parse the structure file into a nested list structure."""
    with open(structure_file, 'r', encoding='utf-8') as f:
        lines = [line.rstrip() for line in f if line.strip()]

    tree = []
    stack = [( -1, tree )]  # (indent level, list reference)

    for line in lines:
        indent = len(line) - len(line.lstrip('\t'))
        name = line.strip()
        node = {"name": name, "children": []}

        # Pop stack until we find the correct parent level
        while stack and indent <= stack[-1][0]:
            stack.pop()

        # Safeguard: if stack is empty, reinitialize with root
        if not stack:
            stack = [(-1, tree)]

        # Append to the current parent's children
        stack[-1][1].append(node)

        # Push this node to stack
        stack.append((indent, node["children"]))

    return tree


def create_structure(root_dir, structure_tree):
    """Recursively create directories and files from the parsed structure."""
    for node in structure_tree:
        name = node["name"]
        path = os.path.join(root_dir, name)

        # Directory
        if name.endswith('/'):
            os.makedirs(path, exist_ok=True)
            create_structure(path, node["children"])
        else:
            # File
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write("")  # empty file placeholder


def main():
    parser = argparse.ArgumentParser(description="Recreate directory and file structure from text file.")
    parser.add_argument("root_directory", help="Root directory where structure will be created")
    parser.add_argument("structure_file", help="Path to structure text file")
    args = parser.parse_args()

    structure_tree = parse_structure(args.structure_file)
    create_structure(args.root_directory, structure_tree)

    print(f"✅ Structure created successfully under: {args.root_directory}")


if __name__ == "__main__":
    main()
