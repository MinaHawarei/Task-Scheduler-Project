"""
Queue Data Structure Implementation

This module implements a Queue data structure using a list-based approach.
The queue follows FIFO (First In First Out) principle and supports
persistence to/from files.
"""


class Queue:
    """
    A Queue implementation that stores tasks in FIFO order.
    """

    def __init__(self):
        """
        Initialize an empty queue.
        
        Creates an empty list to store queue elements.
        """
        self.items = []

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        
        Parameters:
            item: The item to be added to the queue (typically a job_id)
        
        Returns:
            None
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.
        
        Returns:
            The item at the front of the queue (FIFO order)
        
        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.pop(0)

    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
        """
        return len(self.items) == 0

    def peek(self):
        """
        Return the item at the front of the queue without removing it.
        
        Returns:
            The item at the front of the queue, or None if queue is empty
        """
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        """
        Get the number of items in the queue.
        
        Returns:
            int: The number of items in the queue
        """
        return len(self.items)

    def to_dict(self):
        """
        Serialize queue state to a dictionary.
        
        Returns:
            dict: Serialized queue state
        """
        return {"items": list(self.items)}

    @classmethod
    def from_dict(cls, data):
        """
        Create a Queue instance from serialized data.
        
        Parameters:
            data (dict): Serialized queue state
        
        Returns:
            Queue: Restored Queue instance
        """
        queue = cls()
        items = data.get("items", [])
        if isinstance(items, list):
            queue.items = list(items)
        return queue

    def __str__(self):
        """
        Return a string representation of the queue.
        
        Returns:
            str: String representation showing queue contents
        """
        return f"Queue({self.items})"

    def __repr__(self):
        """
        Return a detailed string representation of the queue.
        
        Returns:
            str: Detailed string representation
        """
        return self.__str__()

