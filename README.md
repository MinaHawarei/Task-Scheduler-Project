# Task Scheduler & Job History Manager

A comprehensive Python project demonstrating the implementation of fundamental data structures (Queue, Linked List, and Hash Table) from scratch, integrated into a task scheduling system with job history management.

## Project Overview

This project implements a complete task scheduler that uses three core data structures:
- **Queue**: Manages pending tasks in FIFO order with file persistence
- **Linked List**: Maintains chronological history of executed jobs
- **Hash Table**: Provides O(1) average-case lookup for job IDs using chaining for collision resolution

## Project Structure

```
Task-Scheduler-Project/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── queue.py             # Queue implementation with persistence
│   ├── linked_list.py       # Linked list for history log
│   ├── hash_table.py        # Hash table with chaining
│   └── scheduler.py         # Main scheduler integrating all structures
├── tests/
│   ├── __init__.py
│   └── test_scheduler.py    # Test file (for future unit tests)
├── main.py                  # CLI application entry point
├── requirements.txt         # Project dependencies
└── README.md               # This file
```

## Features

### 1. Queue Data Structure (`src/queue.py`)
- **Methods:**
  - `enqueue(item)`: Add item to the rear of the queue
  - `dequeue()`: Remove and return item from the front (FIFO)
  - `is_empty()`: Check if queue is empty
  - `peek()`: View front item without removing it
  - `save_queue_to_file(filename)`: Persist queue state to JSON file
  - `load_queue_from_file(filename)`: Restore queue state from file

### 2. Linked List - History Log (`src/linked_list.py`)
- **Methods:**
  - `add_to_history(job_id, timestamp)`: Add executed job to history
  - `display_history()`: Print all jobs in chronological order
  - `get_last_n(n)`: Retrieve the last N executed jobs
  - Stores jobs with timestamps for tracking execution time

### 3. Hash Table (`src/hash_table.py`)
- **Methods:**
  - `hash(key)`: Compute hash value using polynomial rolling hash
  - `insert(key, value)`: Insert/update key-value pair
  - `search(key)`: O(1) average-case lookup
  - `remove(key)`: Remove key-value pair
- **Collision Handling:** Uses chaining (linked list) at each bucket
- **Features:**
  - Automatic resizing when load factor exceeds 0.75
  - Polynomial hash function for good distribution
  - Detailed comments explaining collision resolution

### 4. Scheduler (`src/scheduler.py`)
- **Methods:**
  - `submit_task(job_id)`: Add new task to queue and hash table
  - `run_next_task()`: Execute next task from queue
  - `run_all()`: Execute all pending tasks
  - `find_job(job_id)`: O(1) lookup using hash table
  - `get_last_n_tasks(n)`: Get recent execution history
  - `remove_job(job_id)`: Remove job from hash table
  - `save_queue_to_file()` / `load_queue_from_file()`: Persistence

## Installation

1. Clone or download this project
2. Ensure Python 3.6+ is installed
3. No external dependencies required (uses only Python standard library)

## Usage

### Running the Application

```bash
python main.py
```

### Interactive Menu Options

1. **Submit a new task** - Add a job to the queue
2. **Run next task** - Execute the first task in queue
3. **Run all pending tasks** - Execute all tasks in queue
4. **View execution history** - Display all executed jobs
5. **Search for a job by ID** - O(1) lookup using hash table
6. **View last N tasks** - Get recent execution history
7. **Remove job from hash table** - Clean up completed jobs
8. **Save queue to file** - Persist queue state
9. **Load queue from file** - Restore queue state
10. **Display queue status** - Show pending tasks
11. **Display statistics** - View scheduler metrics

## Example Workflow

```
1. Submit tasks: job1, job2, job3
2. Run next task → job1 executes and moves to history
3. Run all → job2 and job3 execute
4. View history → See all executed jobs with timestamps
5. Search job1 → Get job details from hash table
6. Save queue → Persist state to queue_state.txt
7. Load queue → Restore state from file
```

## Data Structure Details

### Queue Implementation
- Uses Python list with `append()` and `pop(0)` operations
- File persistence using JSON format
- FIFO (First In First Out) ordering

### Linked List Implementation
- Singly linked list with head pointer
- Most recent jobs stored at the head (O(1) insertion)
- Each node contains job_id and timestamp

### Hash Table Implementation
- **Hash Function:** Polynomial rolling hash (base 31)
  - Formula: `hash = (hash * 31 + char_code) % capacity`
  - Provides good distribution for string keys
- **Collision Resolution:** Chaining
  - Each bucket contains a linked list of key-value pairs
  - When collision occurs, new node is added to the chain
  - Average case: O(1), Worst case: O(n) if all keys hash to same bucket
- **Load Factor:** Automatically resizes when > 0.75

## Code Quality

- ✅ Clean OOP structure with separate classes
- ✅ Comprehensive docstrings for all methods
- ✅ Type hints and clear parameter descriptions
- ✅ Error handling and validation
- ✅ Readable, maintainable code
- ✅ No external dependencies (pure Python)

## File Persistence Format

Queue state is saved as JSON:
```json
["job1", "job2", "job3"]
```

## Testing

The application includes an interactive CLI menu for manual testing. To test all features:

1. Run `python main.py`
2. Use the menu to test each functionality
3. Try edge cases (empty queue, non-existent jobs, etc.)

## Future Enhancements

- Unit tests in `tests/test_scheduler.py`
- Priority queue support
- Job scheduling with delays
- Database persistence
- Web interface

## Author

Data Structures Project - Task Scheduler Implementation

## License

This project is for educational purposes.

