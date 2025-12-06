"""
Queue Data Structure Implementation

This module implements a Queue data structure using a list-based approach.
The queue follows FIFO (First In First Out) principle and supports
persistence to/from files.
"""


class Queue:
    """
    A Queue implementation that stores tasks in FIFO order.
    Supports file persistence for saving and restoring state.
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

    def save_queue_to_file(self, filename="queue_state.txt"):
        """
        Save the current queue state to a file.
        
        The queue is saved as a JSON-formatted list of job IDs.
        This allows for easy restoration of the queue state.
        
        Parameters:
            filename (str): The name of the file to save to (default: "queue_state.txt")
        
        Returns:
            bool: True if save was successful, False otherwise
        """
        try:
            import json
            with open(filename, 'w') as f:
                json.dump(self.items, f)
            return True
        except Exception as e:
            print(f"Error saving queue to file: {e}")
            return False

    def load_queue_from_file(self, filename="queue_state.txt"):
        """
        Load queue state from a file.
        
        Reads a JSON-formatted list of job IDs and restores the queue.
        If the file doesn't exist, the queue remains empty.
        
        Parameters:
            filename (str): The name of the file to load from (default: "queue_state.txt")
        
        Returns:
            bool: True if load was successful, False otherwise
        """
        try:
            import json
            import os
            
            if not os.path.exists(filename):
                print(f"File {filename} does not exist. Starting with empty queue.")
                return False
            
            with open(filename, 'r') as f:
                self.items = json.load(f)
            
            # Validate that loaded data is a list
            if not isinstance(self.items, list):
                self.items = []
                return False
            
            return True
        except json.JSONDecodeError:
            print(f"Error: {filename} is not valid JSON. Starting with empty queue.")
            self.items = []
            return False
        except Exception as e:
            print(f"Error loading queue from file: {e}")
            self.items = []
            return False

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

