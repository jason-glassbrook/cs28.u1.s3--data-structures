import sys
sys.path.append('../doubly_linked_list')

from doubly_linked_list import ListNode, DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.storage = DoublyLinkedList()
        self.lookup = dict()
        self.limit = limit

    def __len__(self):
        return len(self.storage)

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        value = None

        # if key exists
        if key in self.lookup:
            # find the node
            node = self.lookup[key]
            # move it to the front
            self.storage.move_to_front(node)
            # give the value
            (__, value) = node.value

        # if key doesn't exist
        else:
            pass

        return value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # if key exists
        if key in self.lookup:
            # get the node
            node = self.lookup[key]
            # move it to the front
            self.storage.move_to_front(node)
            # overwrite the value
            node.value = (key, value)

        # if key doesn't exist
        else:
            # add key-value to .storage, .lookup
            self.storage.add_to_head((key, value))
            self.lookup[key] = self.storage.head

        # ensure length is under limit
        if len(self) > self.limit:
            # remove last node from .storage
            (old_key, __) = self.storage.remove_from_tail()
            # remove from .lookup
            del self.lookup[old_key]

        pass
