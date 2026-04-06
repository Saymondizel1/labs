# lab3
# Repository for labs Laboratory Work: Binary Tree In-Order Traversal

## Task Description
This laboratory work implements a Binary Tree data structure, constructs it from an array representation read from a file, and performs an in-order traversal to retrieve the elements in a specific order.

## Problem Statement
* A binary tree must be constructed from an array where the left child of a node at index `i` is at `2*i + 1` and the right child is at `2*i + 2`.
* The array representation can contain `null`, `n`, or `none` strings to denote empty child nodes.
* The data is read from an external text file (e.g., `pyramid.txt`), which can have values separated by commas or spaces.
* The goal is to perform an **in-order traversal** (Left, Root, Right) of the constructed tree and return the sequence of visited nodes.

## Objective
Implement the following core functions:
1.  `build_tree_from_array(arr, i=0)`: Recursively builds the binary tree from a list.
2.  `build_tree_from_file(filename)`: Parses a file into an array and triggers tree construction.
3.  `in_order_traversal(root)`: Returns a list of node values visited in in-order.

## Algorithm Overview
This implementation consists of three main components:

1.  **File Parsing**:
    * Reads the file content, replaces commas with spaces, and splits the string into a list of tokens.
    * Converts numeric tokens to integers and recognizes specific string literals (`null`, `none`, `n`) as `None`.
2.  **Tree Construction**:
    * Uses a recursive approach to build the tree.
    * Given an index `i`, the function creates a `BinaryTree` node.
    * It recursively assigns the left child using index `2 * i + 1` and the right child using `2 * i + 2`.
3.  **In-Order Traversal**:
    * Recursively traverses the left subtree.
    * Visits the current root node (adds its value to the result list).
    * Recursively traverses the right subtree.

## Full Solution

```python
from typing import List

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(root) -> List:
    if root is None:
        return []
    return in_order_traversal(root.left) + [root.value] + in_order_traversal(root.right)

def build_tree_from_array(arr, i=0):
    if i < len(arr) and arr[i] is not None:
        root = BinaryTree(arr[i])
        root.left = build_tree_from_array(arr, 2 * i + 1)
        root.right = build_tree_from_array(arr, 2 * i + 2)
        return root
    return None

def build_tree_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().replace(',', ' ').split()
            
            arr = []
            for item in content:
                if item.lower() in ['null', 'n', 'none']:
                    arr.append(None)
                else:
                    arr.append(int(item))
                    
            return build_tree_from_array(arr)
            
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
        return None

if __name__ == "__main__":
    filename = "pyramid.txt" 
    
    print(f"Будуємо дерево з файлу {filename}...")
    root = build_tree_from_file(filename)
    
    if root:
        result = in_order_traversal(root)
        print("In-order обхід дерева:", result)
