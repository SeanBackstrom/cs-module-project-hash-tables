class HashTableEntry():
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

    def __str__(self):
        return "'{}': '{}'".format(self.key, self.value)




# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable():
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """


    def __init__(self, capacity):
        # Your code here
        self.total_items = 0
        self.capacity = capacity
        self.bucket_array = [None for i in range(capacity)]
        
        



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.total_items / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        byte_array = key.encode('utf-8')

        for byte in byte_array:
            hash = ((hash * 33) ^ byte) % 0x100000000

        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        self.total_items +=1  
        load_factor = self.get_load_factor()
 

        key_hash = self.djb2(key)
        bucket_index = key_hash % self.capacity

        new_entry = HashTableEntry(key, value)
        existing_entry = self.bucket_array[bucket_index]

        if existing_entry:
            last_entry = None
            while existing_entry:
                if existing_entry.key == key:
                    #found an existing key, replace the value
                    existing_entry.value = value
                    return
                last_entry = existing_entry
                existing_entry = existing_entry.next
            #past this point, we did not find an existing key
            #append to end of bucket
            last_entry.next = new_entry
        else:
            self.bucket_array[bucket_index] = new_entry
        load_factor = self.get_load_factor()

        if load_factor >= 0.7:
            self.resize(self.capacity * 2)   
        load_factor = self.get_load_factor() 
        print(self.capacity, load_factor)
        


    def debug_print(self):
        for i in range(self.capacity):
            node = self.bucket_array[i]
            print('Bucket {}'.format(i))
            if node:
                while node:
                    print('    {}'.format(node))
                    node = node.next
            else:
                print('    Empty')

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.total_items -= 1
        key_hash = self.djb2(key)
        bucket_index = key_hash % self.capacity

        existing_entry = self.bucket_array[bucket_index]
        if existing_entry:
            last_entry = None
            while existing_entry:
                if existing_entry.key == key:
                    if last_entry:
                        last_entry.next = existing_entry.next
                    else:
                        self.bucket_array[bucket_index] = existing_entry.next
                last_entry = existing_entry
                existing_entry = existing_entry.next


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        key_hash = self.djb2(key)
        bucket_index = key_hash % self.capacity

        existing_entry = self.bucket_array[bucket_index]
        if existing_entry:
            while existing_entry:
                if existing_entry.key == key:
                    return existing_entry.value
                existing_entry = existing_entry.next

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_arr = [None for i in range(0, new_capacity)]
        

        for i in range(self.capacity):
            node = self.bucket_array[i]
            if node:
                while node:
                    key_hash = self.djb2(node.key)
                    bucket_index = key_hash % new_capacity

                    new_entry = HashTableEntry(node.key, node.value)
                    existing_entry = new_arr[bucket_index]

                    if existing_entry:
                        last_entry = None
                        while existing_entry:
                            if existing_entry.key == node.key:
                                #found an existing key, replace the value
                                existing_entry.value = node.value
                                return
                            last_entry = existing_entry
                            existing_entry = existing_entry.next
                        #past this point, we did not find an existing key
                        #append to end of bucket
                        last_entry.next = new_entry
                    else:
                        new_arr[bucket_index] = new_entry
                    node = node.next  
        self.capacity = new_capacity 
        self.bucket_array = new_arr
        '''
        if self.load_factor >= 0.70:
            self.capacity *= 2
            for i in range(0, int(self.capacity / 2)):
                self.bucket_array.append(None)
            self.load_factor = self.total_items / self.capacity

            for i in self.bucket_array:
                
                if i is not None:
                    
                    key_hash = self.djb2(i.key)
                    bucket_index = key_hash % self.capacity

                    new_entry = HashTableEntry(i.key, i.value)
                    existing_entry = self.bucket_array[bucket_index]

                    if existing_entry:
                        last_entry = None
                        while existing_entry:
                            if existing_entry.key == i.key:
                                #found an existing key, replace the value
                                existing_entry.value = i.value
                                return
                            last_entry = existing_entry
                            existing_entry = existing_entry.next
                        #past this point, we did not find an existing key
                        #append to end of bucket
                        last_entry.next = new_entry
                    else:
                        self.bucket_array[bucket_index] = new_entry
                        
                    self.delete(i.key)
        '''




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    ht.resize(16)
    ht.debug_print()
    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
