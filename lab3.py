from logging import root
from typing import List

class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def in_order_traversal(self) -> List:
      if self is None:
          return []
      result = []
      self._traverse(result)
      return result

    def _traverse(self, result: List) -> None:
        if self.left is not None:
            self.left._traverse(result)
        result.append(self.value)
        if self.right is not None:
            self.right._traverse(result)
            
            
            
    #         10
    #       /     \
    #     33        20
    #   /   \     /    \
    # 15     23  50      30
    #   \    /     \    /  \
    #    17  28     45 25  40
    #   /      \         \
    # 19         21        15


