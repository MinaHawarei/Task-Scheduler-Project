"""
Task Scheduler & Job History Manager - Main CLI Application

This is the main entry point for the Task Scheduler application.
It provides an interactive CLI menu to test all functionality.
"""

from src.scheduler import Scheduler
from src.state_manager import StateManager


def print_menu():
    """
    Display the main menu options.
    
    Returns:
        None
    """
    print("\n" + "=" * 60)
    print("     TASK SCHEDULER & JOB HISTORY MANAGER")
    print("=" * 60)
    print("1.  Submit a new task")
    print("2.  Run next task")
    print("3.  Run all pending tasks")
    print("4.  View execution history")
    print("5.  Search for a job by ID")
    print("6.  View last N tasks")
    print("7.  Remove job from hash table")
    print("8.  Display queue status")
    print("9.  Display statistics")
    print("0.  Exit")
    print("=" * 60)


def submit_task_menu(scheduler):
    """
    Handle task submission from user input.
    
    Parameters:
        scheduler: The Scheduler instance
    
    Returns:
        None
    """
    try:
        job_id = input("Enter job ID to submit: ").strip()
        if not job_id:
            print("Error: Job ID cannot be empty.")
            return
        
        if scheduler.submit_task(job_id):
            print(f"✓ Task '{job_id}' successfully submitted to queue.")
        else:
            print(f"✗ Failed to submit task '{job_id}'.")
    except Exception as e:
        print(f"Error submitting task: {e}")


def run_next_task_menu(scheduler):
    """
    Handle running the next task.
    
    Parameters:
        scheduler: The Scheduler instance
    
    Returns:
        None
    """
    if scheduler.get_queue_size() == 0:
        print("No tasks in queue to execute.")
        return
    
    job_id = scheduler.run_next_task()
    if job_id:
        print(f"✓ Task '{job_id}' executed successfully and added to history.")
    else:
        print("No task was executed.")


def run_all_tasks_menu(scheduler):
    """
    Handle running all pending tasks.
    
    Parameters:
        scheduler: The Scheduler instance
    
    Returns:
        None
    """
    queue_size = scheduler.get_queue_size()
    if queue_size == 0:
        print("No tasks in queue to execute.")
        return
    
    print(f"Executing {queue_size} task(s)...")
    count = scheduler.run_all()
    print(f"✓ Successfully executed {count} task(s).")


def view_history_menu(scheduler):
    """
    Display the execution history.
    
    Parameters:
        scheduler: The Scheduler instance
    
    Returns:
        None
    """
    scheduler.display_history()


def search_job_menu(scheduler):
    """
    Handle job search by ID.
    
    Parameters:
        scheduler: The Scheduler instance
    
    Returns:
        None
    """
    try:
        job_id = input("Enter job ID to search: ").strip()
        if not job_id:
            print("Error: Job ID cannot be empty.")
            return
        
        job_data = scheduler.find_job(job_id)
        if job_data:
            print("\n=== Job Details ===")
            for key, value in job_data.items():
                print(f"{key}: {value}")
            print("=" * 50)
        else:
            print(f"Job '{job_id}' not found.")
    except Exception as e:
        print(f"Error searching for job: {e}")


def view_last_n_menu(scheduler):
    """
    Display the last N tasks from history.
    
    Parameters:
        scheduler: The Scheduler instance
    
    Returns:
        None
    """
    try:
        n = int(input("Enter number of recent tasks to view: "))
        if n <= 0:
            print("Error: Number must be positive.")
            return
        
        tasks = scheduler.get_last_n_tasks(n)
        if not tasks:
            print("No tasks in history.")
            return
        
        print(f"\n=== Last {n} Tasks ===")
        for i, (job_id, timestamp) in enumerate(tasks, 1):
            print(f"{i}. Job ID: {job_id} | Timestamp: {timestamp}")
        print("=" * 50)
    except ValueError:
        print("Error: Please enter a valid number.")
    except Exception as e:
        print(f"Error viewing last N tasks: {e}")


def remove_job_menu(scheduler):
    """
    Handle job removal from hash table.
    
    Parameters:
        scheduler: The Scheduler instance
    
    Returns:
        None
    """
    try:
        job_id = input("Enter job ID to remove: ").strip()
        if not job_id:
            print("Error: Job ID cannot be empty.")
            return
        
        if scheduler.remove_job(job_id):
            print(f"✓ Job '{job_id}' successfully removed from hash table.")
        else:
            print(f"✗ Job '{job_id}' not found in hash table.")
    except Exception as e:
        print(f"Error removing job: {e}")


def display_statistics(scheduler):
    """
    Display scheduler statistics.
    
    Parameters:
        scheduler: The Scheduler instance
    
    Returns:
        None
    """
    print("\n=== Scheduler Statistics ===")
    print(f"Pending tasks in queue: {scheduler.get_queue_size()}")
    print(f"Completed tasks in history: {scheduler.get_history_size()}")
    print("=" * 50)


def main():
    """
    Main application entry point.
    
    Creates a scheduler instance and runs the interactive CLI menu loop.
    
    Returns:
        None
    """
    state_manager = StateManager()
    scheduler = Scheduler(state_manager=state_manager)
    
    # Auto-load full application state on startup
    if scheduler.load_state():
        print("App state loaded successfully.")
    else:
        print("Starting with a fresh state.")
    
    print("\nWelcome to Task Scheduler & Job History Manager!")
    print("This application demonstrates Queue, Linked List, and Hash Table data structures.")
    print("Note: Application state is automatically saved after any change and loaded on startup.")
    
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "0":
                print("\nThank you for using Task Scheduler! Goodbye.")
                break
            elif choice == "1":
                submit_task_menu(scheduler)
            elif choice == "2":
                run_next_task_menu(scheduler)
            elif choice == "3":
                run_all_tasks_menu(scheduler)
            elif choice == "4":
                view_history_menu(scheduler)
            elif choice == "5":
                search_job_menu(scheduler)
            elif choice == "6":
                view_last_n_menu(scheduler)
            elif choice == "7":
                remove_job_menu(scheduler)
            elif choice == "8":
                scheduler.display_queue()
            elif choice == "9":
                display_statistics(scheduler)
            else:
                print("Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("\n\nInterrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

