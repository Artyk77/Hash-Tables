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
        self.count = 0 #reset


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
        

        hash_key = self._hash_mod(key)

        if self.storage[hash_key]:
            entry = self.storage[hash_key]
            while entry:
                if entry.key == key: # Update the value
                    entry.value = value
                    break
                elif entry.next: # Allows to loop back through the next entry, which is why this is in a while loop
                    entry = entry.next
                else: # Link the two items
                    entry.next = LinkedPair(key, value)
                    self.count += 1
                    break
        else:
            self.storage[hash_key] = LinkedPair(key, value) # Instert LinkedPair
            self.count += 1



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hash_key = self._hash_mod(key)

        if self.storage[hash_key] is None:
            print("No Key Found", key)
            return

        entry = self.storage[hash_key]
        prev_entry = None
        while entry: # Same concept of insert, allows to loop through pairs (if there is a pair)
            # print(entry.key, key)
            if entry.key == key: # Matches correct key
                if prev_entry:
                    if entry.next: # Link the two together since the connector of these two is about to be removed
                        prev_entry.next = entry.next
                    else:
                        prev_entry.next = None
                else:
                    if entry.next: # Shifts over one to the left so the first index is now the second (only if there is a next)
                        self.storage[hash_key] = entry.next
                    else:
                        self.storage[hash_key] = None # Where it gets reset
                self.count -= 1
                return entry.value
            else:
                prev_entry = entry
                entry = entry.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash_key = self._hash_mod(key)

        if self.storage[hash_key]:
            entry = self.storage[hash_key]
            while entry:
                if entry.key == key:
                    return entry.value
                entry = entry.next
        return None        


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        new_storage = []
        for entry in self.storage:
            while entry:
                new_storage.append([entry.key, entry.value])
                entry = entry.next

        self.capacity = 2*self.capacity
        self.storage = [None]*self.capacity

        for entry in new_storage :
            self.insert(entry[0], entry[1])
            self.count -= 1
        return



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
