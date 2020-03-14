# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        l_pair = LinkedPair(key, value)

        if self.storage[idx] is None:
            self.storage[idx] = l_pair
        else:
            curr_pair = self.storage[idx]
            while curr_pair:
                if curr_pair.key == key:
                    curr_pair.value = value
                    break
                elif curr_pair.next:
                    curr_pair = curr_pair.next
                else:
                    curr_pair.next = l_pair
                    break

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)

        if self.storage[idx] is not None:
            self.storage[idx] = None
        else:
            print(f'Value at Key {key} not found...')

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)

        if self.storage[idx] is not None:
            if self.storage[idx].key == key:
                return self.storage[idx].value
            curr_pair = self.storage[idx].next
            while curr_pair is not None:
                if curr_pair.key == key:
                    return curr_pair.value
                curr_pair = curr_pair.next
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        old_stor = self.storage
        self.storage = [None] * self.capacity

        for pair in old_stor:
            while pair is not None:
                self.insert(pair.key, pair.value)
                pair = pair.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
