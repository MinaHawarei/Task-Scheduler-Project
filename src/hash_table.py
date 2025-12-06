"""
Hash Table Data Structure Implementation

This module implements a hash table with chaining for collision resolution.
The hash table provides O(1) average-case lookup time for job IDs.
"""


class HashNode:
    """
    A node in the hash table chain.
    
    Each node stores a key-value pair and a reference to the next node
    in the collision chain.
    """

    def __init__(self, key, value):
        """
        Initialize a hash table node.
        
        Parameters:
            key: The job ID (used as the hash key)
            value: The associated data for this job
        """
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table implementation with chaining for collision resolution.
    
    This hash table provides O(1) average-case time complexity for
    insert, search, and remove operations. Collisions are handled using
    a linked list chain at each bucket.
    """

    def __init__(self, capacity=16):
        """
        Initialize the hash table.
        
        Parameters:
            capacity (int): The initial capacity of the hash table (default: 16)
        """
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * capacity

    def hash(self, key):
        """
        Compute the hash value for a given key.
        
        Uses a simple polynomial rolling hash function:
        - Converts key to string if needed
        - Uses polynomial hash: sum of (char_code * base^position) mod capacity
        - This provides good distribution for string keys
        
        Parameters:
            key: The key to hash (can be string or number)
        
        Returns:
            int: The hash value (bucket index) between 0 and capacity-1
        """
        # Convert key to string for consistent hashing
        key_str = str(key)
        
        # Polynomial rolling hash function
        # Base 31 is commonly used for string hashing
        base = 31
        hash_value = 0
        
        for char in key_str:
            hash_value = (hash_value * base + ord(char)) % self.capacity
        
        return hash_value

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        
        If the key already exists, the value is updated.
        Collisions are handled using chaining (linked list at each bucket).
        
        Time Complexity: O(1) average case, O(n) worst case (if all keys hash to same bucket)
        
        Parameters:
            key: The job ID to insert
            value: The associated data for this job
        
        Returns:
            bool: True if insertion was successful
        """
        # Get the bucket index using hash function
        bucket_index = self.hash(key)
        
        # Check if key already exists in the chain
        current = self.buckets[bucket_index]
        while current:
            if current.key == key:
                # Key exists, update the value
                current.value = value
                return True
            current = current.next
        
        # Key doesn't exist, insert new node at the beginning of the chain
        new_node = HashNode(key, value)
        new_node.next = self.buckets[bucket_index]
        self.buckets[bucket_index] = new_node
        self.size += 1
        
        # Optional: Resize if load factor is too high (for better performance)
        if self.size > self.capacity * 0.75:
            self._resize()
        
        return True

    def search(self, key):
        """
        Search for a key in the hash table.
        
        Returns the value associated with the key, or None if not found.
        
        Time Complexity: O(1) average case, O(n) worst case
        
        Parameters:
            key: The job ID to search for
        
        Returns:
            The value associated with the key, or None if key not found
        """
        bucket_index = self.hash(key)
        current = self.buckets[bucket_index]
        
        # Traverse the chain to find the key
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        return None

    def remove(self, key):
        """
        Remove a key-value pair from the hash table.
        
        If the key is found, it is removed from the chain.
        
        Time Complexity: O(1) average case, O(n) worst case
        
        Parameters:
            key: The job ID to remove
        
        Returns:
            bool: True if key was found and removed, False otherwise
        """
        bucket_index = self.hash(key)
        current = self.buckets[bucket_index]
        previous = None
        
        # Traverse the chain to find the key
        while current:
            if current.key == key:
                # Found the key, remove it from the chain
                if previous:
                    previous.next = current.next
                else:
                    # Key is at the head of the chain
                    self.buckets[bucket_index] = current.next
                
                self.size -= 1
                return True
            
            previous = current
            current = current.next
        
        return False

    def _resize(self):
        """
        Resize the hash table when load factor exceeds threshold.
        
        This method doubles the capacity and rehashes all existing entries.
        This helps maintain O(1) average-case performance.
        
        Returns:
            None
        """
        old_buckets = self.buckets
        old_capacity = self.capacity
        
        # Double the capacity
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self.size = 0
        
        # Rehash all existing entries
        for bucket in old_buckets:
            current = bucket
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def get_all_keys(self):
        """
        Get all keys currently in the hash table.
        
        Returns:
            list: A list of all keys in the hash table
        """
        keys = []
        for bucket in self.buckets:
            current = bucket
            while current:
                keys.append(current.key)
                current = current.next
        return keys

    def is_empty(self):
        """
        Check if the hash table is empty.
        
        Returns:
            bool: True if hash table is empty, False otherwise
        """
        return self.size == 0

    def __str__(self):
        """
        Return a string representation of the hash table.
        
        Returns:
            str: String representation showing hash table contents
        """
        if self.is_empty():
            return "HashTable(empty)"
        
        items = []
        for bucket in self.buckets:
            current = bucket
            while current:
                items.append(f"{current.key}:{current.value}")
                current = current.next
        
        return f"HashTable([{', '.join(items)}])"

