"""
storage.py
Handles reading and writing device records to a JSON file.
This acts as our "file-based database" for the TechCycle prototype.
"""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "devices.json")


def load_devices():
    """Load all device records from the JSON file. Returns a list of dicts."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_devices(devices):
    """Save the full list of device records back to the JSON file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(devices, f, indent=4)


def add_device(device):
    """Append a single new device record and persist it."""
    devices = load_devices()
    device["id"] = len(devices) + 1
    devices.append(device)
    save_devices(devices)
    return device
