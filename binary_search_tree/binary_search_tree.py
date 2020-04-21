import sys
sys.path.append('../queue_and_stack')

from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:

    ########################################
    # PROPERTIES
    ########################################

    @property
    def left(self):

        return self._left

    @left.setter
    def left(self, left):

        self._left = left
        return

    @left.deleter
    def left(self):

        self._left = None
        return

    @property
    def right(self):

        return self._right

    @right.setter
    def right(self, right):

        self._right = right
        return

    @right.deleter
    def right(self):

        self._right = None
        return

    ########################################
    # EXTERNAL
    ########################################

    def __init__(self, value, left=None, right=None):

        self.value = value
        self.left = left
        self.right = right

        return

    def __len__(self):

        return 1 + self._len_or(self.left) + self._len_or(self.right)

    #---------------------------------------
    # DAY 1
    #---------------------------------------

    # Insert the given value into the tree
    def insert(self, new_value):

        if new_value < self.value:

            if isinstance(self.left, BinarySearchTree):
                self.left.insert(new_value)

            else:
                self.left = BinarySearchTree(new_value)

        else:

            if isinstance(self.right, BinarySearchTree):
                self.right.insert(new_value)

            else:
                self.right = BinarySearchTree(new_value)

        return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target_value):

        if target_value == self.value:
            return True

        elif target_value < self.value and isinstance(self.left, BinarySearchTree):
            return self.left.contains(target_value)

        elif target_value > self.value and isinstance(self.right, BinarySearchTree):
            return self.right.contains(target_value)

        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    #---------------------------------------
    # DAY 2
    #---------------------------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    #---------------------------------------
    # STRETCH
    #---------------------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

    ########################################
    # INTERNAL
    ########################################

    @staticmethod
    def _len_or(thing, default=0):

        try:
            return len(thing)

        except TypeError:
            return default

    ########################################
