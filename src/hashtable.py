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
        self.num_entries = 0

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

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
            self.num_entries += 1
        else:
            # go through linked list
            # if key not there, add node
            # if key there, update value
            current_node = self.storage[index]
            if current_node.key == key:
                current_node.value = value
                return
            while current_node.next is not None:
                current_node = current_node.next
                if current_node.key == key:
                    current_node.value = value
                    return
            current_node.next = LinkedPair(key, value)
            self.num_entries += 1
            # Check the load factor num_entries/capacity
            # if > 0.7 resize
            load_factor = self.num_entries / self.capacity
            if load_factor > 0.7:
                self.resize()
            return

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_node = self.storage[index]
        if current_node is None:
            return
        if current_node.key == key:
            self.storage[index] = current_node.next
            self.num_entries -= 1
            return
        next_node = current_node.next
        while next_node is not None:
            if next_node.key == key:
                current_node.next = next_node.next
                next_node.next = None
                self.num_entries -= 1
                return
            current_node = next_node
            next_node = next_node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_node = self.storage[index]
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_ht = HashTable(self.capacity)
        for bucket in self.storage:
            current_node = bucket
            while current_node is not None:
                index = self._hash_mod(current_node.key)
                new_ht.insert(current_node.key, current_node.value)
                current_node = current_node.next
        self.storage = new_ht.storage

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    #test removing
    # print(ht.remove("line_3"))
    # print(ht.remove("line_3"))

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
