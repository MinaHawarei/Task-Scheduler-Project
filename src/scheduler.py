"""
Task Scheduler Implementation

This module implements a task scheduler that integrates Queue, Linked List,
and Hash Table data structures to manage task execution and history.
"""

from .queue import Queue
from .linked_list import HistoryLog
from .hash_table import HashTable
from .state_manager import StateManager


class Scheduler:
    """
    A task scheduler that manages task execution using multiple data structures.
    
    The scheduler uses:
    - Queue: To store pending tasks (FIFO order)
    - HashTable: For O(1) lookup of jobs by ID
    - HistoryLog: To maintain execution history
    """

    def __init__(self, state_manager=None):
        """
        Initialize the scheduler with empty data structures.
        
        Creates a new Queue, HashTable, and HistoryLog instance.
        """
        self.queue = Queue()
        self.hash_table = HashTable()
        self.history = HistoryLog()
        self.config = {}  # Placeholder for future runtime settings/configuration
        self.state_manager = state_manager or StateManager()

    def submit_task(self, job_id):
        """
        Submit a new task to the scheduler.
        
        The task is added to the queue and registered in the hash table.
        The hash table stores job metadata (status, submission time, etc.).
        
        Parameters:
            job_id: The unique identifier for the job
        
        Returns:
            bool: True if task was successfully submitted
        """
        # Add to queue
        self.queue.enqueue(job_id)
        
        # Register in hash table with metadata
        from datetime import datetime
        job_data = {
            "job_id": job_id,
            "status": "pending",
            "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.hash_table.insert(job_id, job_data)
        
        self._auto_save()
        return True

    def run_next_task(self):
        """
        Execute the next task in the queue.
        
        Removes the task from the queue, executes it, updates its status
        in the hash table, and adds it to the history log.
        
        Returns:
            str: The job_id of the executed task, or None if queue is empty
        """
        if self.queue.is_empty():
            return None
        
        # Get next task from queue
        job_id = self.queue.dequeue()
        
        # Execute the task (simulated)
        print(f"Executing task: {job_id}")
        
        # Update status in hash table
        job_data = self.hash_table.search(job_id)
        if job_data:
            from datetime import datetime
            job_data["status"] = "completed"
            job_data["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.hash_table.insert(job_id, job_data)
        
        # Add to history log
        self.history.add_to_history(job_id)
        
        self._auto_save()
        return job_id

    def run_all(self):
        """
        Execute all pending tasks in the queue.
        
        Processes all tasks in FIFO order until the queue is empty.
        Each task is executed, updated in the hash table, and added to history.
        
        Returns:
            int: The number of tasks executed
        """
        count = 0
        while not self.queue.is_empty():
            self.run_next_task()
            count += 1
        
        return count

    def find_job(self, job_id):
        """
        Find a job by its ID using the hash table.
        
        Provides O(1) average-case lookup time.
        
        Parameters:
            job_id: The job ID to search for
        
        Returns:
            dict: The job data if found, None otherwise
        """
        return self.hash_table.search(job_id)

    def get_queue_size(self):
        """
        Get the number of pending tasks in the queue.
        
        Returns:
            int: The number of tasks waiting in the queue
        """
        return self.queue.size()

    def get_history_size(self):
        """
        Get the number of completed tasks in history.
        
        Returns:
            int: The number of tasks in the history log
        """
        return self.history.size()

    def display_history(self):
        """
        Display all jobs in the execution history.
        
        Returns:
            None
        """
        self.history.display_history()

    def get_last_n_tasks(self, n):
        """
        Get the last N executed tasks from history.
        
        Parameters:
            n (int): The number of recent tasks to retrieve
        
        Returns:
            list: A list of tuples (job_id, timestamp) for the last N tasks
        """
        return self.history.get_last_n(n)

    def remove_job(self, job_id):
        """
        Remove a job from the hash table.
        
        Note: This only removes from the hash table. If the job is in the queue,
        it will still be executed. This method is useful for cleaning up completed jobs.
        
        Parameters:
            job_id: The job ID to remove
        
        Returns:
            bool: True if job was found and removed, False otherwise
        """
        removed = self.hash_table.remove(job_id)
        if removed:
            self._auto_save()
        return removed

    def display_queue(self):
        """
        Display all pending tasks in the queue.
        
        Returns:
            None
        """
        if self.queue.is_empty():
            print("Queue is empty.")
        else:
            print(f"\n=== Pending Tasks Queue ===")
            print(f"Queue size: {self.queue.size()}")
            print(f"Next task: {self.queue.peek()}")
            print("=" * 50)

    def _auto_save(self):
        """
        Trigger an automatic save of the full application state.
        """
        self.state_manager.save_state(self)

    def to_dict(self):
        """
        Serialize scheduler state to a dictionary suitable for JSON.
        
        Returns:
            dict: Serialized scheduler state
        """
        return {
            "queue": self.queue.to_dict(),
            "hash_table": self.hash_table.to_dict(),
            "history": self.history.to_dict(),
            "config": self.config,
        }

    def load_state(self):
        """
        Load scheduler state from persistent storage.
        
        Returns:
            bool: True if state was loaded, False otherwise.
        """
        loaded_state = self.state_manager.load_state()
        if not loaded_state:
            return False
        self._from_dict(loaded_state)
        return True

    def _from_dict(self, data):
        """
        Restore scheduler state from a dictionary.
        
        Parameters:
            data (dict): Serialized scheduler state
        """
        self.queue = Queue.from_dict(data.get("queue", {}))
        self.hash_table = HashTable.from_dict(data.get("hash_table", {}))
        self.history = HistoryLog.from_dict(data.get("history", {}))
        self.config = data.get("config", {})

