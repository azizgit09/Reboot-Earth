"""
logic.py
Business logic for TechCycle:
- classify a device as Repair / Recycle / Donate based on simple rules
- compute impact stats across all stored devices
"""


def classify_device(condition, age_years):
    """
    Very simple rule-based routing (no AI needed for this prototype).
    condition: "working", "minor_issue", "major_issue", "dead"
    age_years: int
    Returns a recommended action.
    """
    condition = condition.lower().strip()

    if condition == "dead" or age_years >= 8:
        return "Recycle"
    if condition == "major_issue" and age_years >= 5:
        return "Recycle"
    if condition in ("minor_issue", "major_issue"):
        return "Repair Shop"
    if condition == "working":
        return "Donate / Resell"
    return "Repair Shop"  # default fallback


def compute_stats(devices):
    """Return a summary dict: counts per recommended action."""
    stats = {"Repair Shop": 0, "Recycle": 0, "Donate / Resell": 0, "Other": 0}
    for d in devices:
        action = d.get("recommendation", "Other")
        if action in stats:
            stats[action] += 1
        else:
            stats["Other"] += 1
    stats["Total Devices"] = len(devices)
    return stats
