"""
main.py
TechCycle - E-Waste Repair & Reuse Platform (Prototype)
Mid-Semester Project - Milestone 2

A simple menu-driven CLI prototype that:
1. Registers a device submitted by a user
2. Classifies it (Repair / Recycle / Donate) using rule-based logic
3. Lists all submitted devices
4. Shows impact stats (how many devices were saved from landfill, etc.)
"""

from storage import load_devices, add_device
from logic import classify_device, compute_stats


def add_device_flow():
    print("\n--- Add a New Device ---")
    name = input("Device name (e.g., Samsung Phone): ").strip()
    device_type = input("Device type (phone/charger/earphones/laptop/other): ").strip()
    condition = input("Condition (working/minor_issue/major_issue/dead): ").strip()

    try:
        age_years = int(input("Approximate age in years: ").strip())
    except ValueError:
        age_years = 0

    recommendation = classify_device(condition, age_years)

    device = {
        "name": name,
        "type": device_type,
        "condition": condition,
        "age_years": age_years,
        "recommendation": recommendation,
    }
    add_device(device)

    print(f"\nDevice registered successfully!")
    print(f"Recommended action: {recommendation}")


def view_devices_flow():
    devices = load_devices()
    print("\n--- All Submitted Devices ---")
    if not devices:
        print("No devices submitted yet.")
        return

    for d in devices:
        print(
            f"[{d['id']}] {d['name']} ({d['type']}) | "
            f"Condition: {d['condition']} | Age: {d['age_years']}y | "
            f"=> {d['recommendation']}"
        )


def stats_flow():
    devices = load_devices()
    stats = compute_stats(devices)
    print("\n--- Impact Stats ---")
    for key, value in stats.items():
        print(f"{key}: {value}")


def main_menu():
    while True:
        print("\n========== TechCycle ==========")
        print("1. Add Device")
        print("2. View All Devices")
        print("3. View Impact Stats")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_device_flow()
        elif choice == "2":
            view_devices_flow()
        elif choice == "3":
            stats_flow()
        elif choice == "4":
            print("Exiting TechCycle. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main_menu()
