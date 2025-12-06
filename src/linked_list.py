"""
Linked List Data Structure Implementation for History Log

This module implements a singly linked list to store executed job history.
The linked list maintains chronological order of executed tasks.
"""


class ListNode:
    """
    A node in the linked list.
    
    Each node stores a job_id and a timestamp, along with a reference
    to the next node in the list.
    """

    def __init__(self, job_id, timestamp=None):
        """
        Initialize a linked list node.
        
        Parameters:
            job_id: The identifier of the job
            timestamp: Optional timestamp for when the job was executed
        """
        self.job_id = job_id
        self.timestamp = timestamp
        self.next = None


class HistoryLog:
    """
    A linked list implementation for storing job execution history.
    
    This class maintains a chronological log of all executed jobs
    using a singly linked list structure.
    """

    def __init__(self):
        """
        Initialize an empty history log.
        
        Creates an empty linked list with a head pointer set to None.
        """
        self.head = None
        self.length = 0

    def add_to_history(self, job_id, timestamp=None):
        """
        Add a job to the history log.
        
        The job is added at the beginning of the list (most recent first).
        If no timestamp is provided, the current time is used.
        
        Parameters:
            job_id: The identifier of the executed job
            timestamp: Optional timestamp (defaults to current time if None)
        
        Returns:
            None
        """
        if timestamp is None:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        new_node = ListNode(job_id, timestamp)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def display_history(self):
        """
        Display all jobs in the history log.
        
        Prints all jobs in chronological order (most recent first).
        Shows job ID and timestamp for each entry.
        
        Returns:
            None
        """
        if self.head is None:
            print("History log is empty.")
            return
        
        current = self.head
        index = 1
        print("\n=== Job History ===")
        while current:
            print(f"{index}. Job ID: {current.job_id} | Timestamp: {current.timestamp}")
            current = current.next
            index += 1
        print("=" * 50)

    def get_last_n(self, n):
        """
        Get the last N jobs from the history log.
        
        Returns the most recent N jobs (since history is stored
        with most recent first).
        
        Parameters:
            n (int): The number of recent jobs to retrieve
        
        Returns:
            list: A list of tuples (job_id, timestamp) for the last N jobs
        """
        if n <= 0:
            return []
        
        if self.head is None:
            return []
        
        result = []
        current = self.head
        count = 0
        
        while current and count < n:
            result.append((current.job_id, current.timestamp))
            current = current.next
            count += 1
        
        return result

    def get_all(self):
        """
        Get all jobs from the history log.
        
        Returns:
            list: A list of tuples (job_id, timestamp) for all jobs
        """
        result = []
        current = self.head
        
        while current:
            result.append((current.job_id, current.timestamp))
            current = current.next
        
        return result

    def size(self):
        """
        Get the number of jobs in the history log.
        
        Returns:
            int: The number of jobs in the history
        """
        return self.length

    def is_empty(self):
        """
        Check if the history log is empty.
        
        Returns:
            bool: True if history is empty, False otherwise
        """
        return self.head is None

    def __str__(self):
        """
        Return a string representation of the history log.
        
        Returns:
            str: String representation showing history contents
        """
        if self.is_empty():
            return "HistoryLog(empty)"
        
        items = []
        current = self.head
        while current:
            items.append(f"{current.job_id}")
            current = current.next
        
        return f"HistoryLog([{', '.join(items)}])"

