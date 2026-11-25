# === Stage 15: Смена статуса ===
# Project: SoilTests
ALLOWED_TRANSITIONS = {
    "pending": {"analyzed"},
    "analyzed": {"approved", "rejected"},
    "approved": {"in_use", "maintenance"},
    "in_use": {"maintenance"},
    "maintenance": {"available"},
    "available": {"pending"},
    "rejected": {"pending"},
}

def is_valid_transition(current, target):
    return target in ALLOWED_TRANSITIONS.get(current, set())

class SoilPlot:
    def __init__(self, name, area, soil_type, sample_date):
        self.name = name
        self.area = area
        self.soil_type = soil_type
        self.sample_date = sample_date
        self.status = "pending"
        self.history = []

    def change_status(self, target, reason):
        if target not in ALLOWED_TRANSITIONS.get(self.status, set()):
            allowed = sorted(ALLOWED_TRANSITIONS.get(self.status, set()))
            raise ValueError(
                f"Cannot move '{self.status}' to '{target}'. "
                f"Allowed: {allowed}"
            )
        if not reason or not reason.strip():
            raise ValueError("Reason must not be empty")
        self.status = target
        self.history.append({"from": self.status, "to": target, "reason": reason})
        return self.status

    def log_change(self, target, reason):
        if not is_valid_transition(self.status, target):
            raise ValueError("Invalid status transition")
        self.status = target
        self.history.append({"from": self.status, "to": target, "reason": reason})
        return self.status

    def get_history(self):
        return list(self.history)

if __name__ == "__main__":
    plot = SoilPlot("Field-A", 1200, "loam", "2024-05-01")
    print(plot.change_status("analyzed", "pH measured"))
    print(plot.change_status("approved", "within range"))
    print(plot.change_status("in_use", "sowing started"))
    try:
        plot.change_status("pending", "not allowed now")
    except ValueError as exc:
        print("Blocked:", exc)
