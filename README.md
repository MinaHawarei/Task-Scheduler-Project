# Task Scheduler & Job History Manager

A Python project demonstrating core data structures (Queue, Linked List, Hash Table) integrated into a task scheduling system with **full application state persistence**.

## Project Overview

- Task scheduling with FIFO queuing, O(1) lookups, and execution history.
- **Full program state persistence**: the entire application state (queue, history, hash table/job metadata, config) is saved to a single JSON file and restored automatically on startup.
- No manual save/load steps are required; all changes auto-save.

## Project Structure

```
Task-Scheduler-Project/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── queue.py             # Queue implementation
│   ├── linked_list.py       # Linked list for history log
│   ├── hash_table.py        # Hash table with chaining
│   ├── state_manager.py     # Unified state persistence (app_state.json)
│   └── scheduler.py         # Scheduler integrating all structures and state
├── tests/
│   ├── __init__.py
│   └── test_scheduler.py    # Test file (placeholder)
├── main.py                  # CLI application entry point
├── requirements.txt         # Project dependencies
└── README.md                # This file
```

## Features

- **Automatic full-state load on startup**: The app restores from `app_state.json` if it exists and is valid.
- **Automatic full-state save on any change**: Enqueue, dequeue/execute, removals, and future state changes trigger an auto-save.
- **Centralized state management**: `src/state_manager.py` is the single source of truth for persistence.
- **JSON-based storage**: State is serialized to human-readable JSON for portability and debugging.
- **Graceful handling of missing/corrupted state files**: Missing or invalid files fall back to a fresh default state without crashing.
- **Menu simplified**: Manual “Save/Load Queue” options removed; state is handled automatically.

### Data Structures

1. **Queue (`src/queue.py`)**
   - Methods: `enqueue`, `dequeue`, `is_empty`, `peek`, `size`
   - Serializable via `to_dict` / `from_dict`

2. **Linked List - History Log (`src/linked_list.py`)**
   - Methods: `add_to_history`, `display_history`, `get_last_n`, `size`
   - Stores job ID + timestamp; serializable via `to_dict` / `from_dict`

3. **Hash Table (`src/hash_table.py`)**
   - Methods: `hash`, `insert`, `search`, `remove`, `get_all_keys`
   - Collision handling via chaining; serializable via `to_dict` / `from_dict`

4. **Scheduler (`src/scheduler.py`)**
   - Methods: `submit_task`, `run_next_task`, `run_all`, `find_job`, `remove_job`, `display_queue`, `get_last_n_tasks`
   - Integrates Queue, HashTable, HistoryLog, and `StateManager`
   - Provides `to_dict` / `_from_dict` for full-state serialization

5. **State Manager (`src/state_manager.py`)**
   - Saves/loads full application state to `app_state.json`
   - Handles missing/corrupted files gracefully
   - Centralizes auto-save logic triggered by the scheduler

## How State Persistence Works

- **What is saved**: queue contents, history entries (with timestamps), hash table entries (job metadata), and config/runtime settings.
- **When it saves**: automatically after any state-changing operation (enqueue, dequeue/execute, remove, future config updates).
- **How it loads**: on program start, `main.py` calls the scheduler’s `load_state()`; if the file is valid, everything is restored, otherwise a fresh state is used.
- **State file**: `app_state.json` (JSON). High-level structure:
  ```json
  {
    "queue": { "items": [...] },
    "history": { "entries": [ { "job_id": "...", "timestamp": "..." } ] },
    "hash_table": { "capacity": 16, "entries": [ { "key": "...", "value": {...} } ] },
    "config": {},
    "metadata": { "saved_at": "2025-12-10T12:34:56.000Z", "version": 1 }
  }
  ```

## Usage

### Run

```bash
python main.py
```

### Interactive Menu Options

1. Submit a new task  
2. Run next task  
3. Run all pending tasks  
4. View execution history  
5. Search for a job by ID  
6. View last N tasks  
7. Remove job from hash table  
8. Display queue status  
9. Display statistics  

> Manual save/load is not needed. Close and reopen the program; it resumes from the last saved state automatically.

### Example Startup Message

- `App state loaded successfully.` (when `app_state.json` is valid)  
- `Starting with a fresh state.` (when the file is missing/corrupted)

## Architecture / Code Structure

- `main.py`: CLI entry; bootstraps `Scheduler` with `StateManager`, auto-loads state, runs menu.
- `scheduler.py`: Orchestrates Queue, HashTable, HistoryLog; triggers auto-save through `StateManager`; provides serialization.
- `queue.py`: FIFO queue logic; serializable to/from dict.
- `linked_list.py`: Execution history via singly linked list; serializable.
- `hash_table.py`: O(1) average lookup with chaining; serializable.
- `state_manager.py`: Centralized full-state persistence to JSON; handles load/save and error resilience.

## Error Handling

- Missing `app_state.json`: starts with a fresh state, no crash.
- Corrupted/invalid JSON: logs a message and falls back to a clean state.
- All auto-saves use JSON; failures are logged to the console.

## Examples

- **Auto-load message**: `App state loaded successfully.`  
- **Fresh start message**: `Starting with a fresh state.`  
- **State file snippet**:
  ```json
  {
    "queue": { "items": ["job1", "job2"] },
    "history": { "entries": [] },
    "hash_table": { "capacity": 16, "entries": [] },
    "config": {},
    "metadata": { "saved_at": "2025-12-10T12:34:56.000Z", "version": 1 }
  }
  ```

## Changelog

- **Full-state persistence**: Introduced unified state management via `state_manager.py`; automatic load on startup and auto-save on every state change; removed manual queue save/load options.

## Installation

1. Ensure Python 3.6+ is installed.
2. Clone or download the project.
3. No external dependencies are required (uses only the Python standard library).

## Testing

- Run `python main.py` and exercise menu options.
- Validate persistence by closing and reopening the app; prior tasks/history/config should be restored.

## License

This project is for educational purposes.

