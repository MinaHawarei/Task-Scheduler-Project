"""
State Manager Module

Handles unified application state persistence and restoration.
"""

import json
import os
from datetime import datetime


class StateManager:
    """
    Manages saving and loading of full application state to a JSON file.
    """

    def __init__(self, filename="app_state.json"):
        """
        Initialize the state manager.

        Parameters:
            filename (str): Path to the state file (default: "app_state.json")
        """
        self.filename = filename

    def save_state(self, scheduler):
        """
        Save the full application state to disk.

        Parameters:
            scheduler: Scheduler instance to serialize

        Returns:
            bool: True if save succeeded, False otherwise
        """
        state = scheduler.to_dict()
        state["metadata"] = {
            "saved_at": datetime.now().isoformat(),
            "version": 1,
        }

        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(state, f, indent=2)
            return True
        except Exception as exc:
            print(f"Error saving application state: {exc}")
            return False

    def load_state(self):
        """
        Load the full application state from disk.

        Returns:
            dict | None: The loaded state, or None if not available/corrupted.
        """
        if not os.path.exists(self.filename):
            return None

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, dict):
                return None
            return data
        except json.JSONDecodeError:
            print(f"State file {self.filename} is corrupted. Starting fresh.")
            return None
        except Exception as exc:
            print(f"Error loading application state: {exc}")
            return None

