# === Stage 16: Просмотр истории ===
# Project: SoilTests
from datetime import datetime


class SoilRecordView:
    """Compact historical display for a single soil record."""

    def __init__(self, name, area, soil_type, sample_date):
        self.name = name
        self.area = area
        self.soil_type = soil_type
        self.sample_date = sample_date

    def format_date(self, value):
        if isinstance(value, str):
            for layout in ("%Y-%m-%d", "%d.%m.%Y", "%m/%d/%Y"):
                try:
                    return datetime.strptime(value, layout).strftime("%Y-%m-%d")
                except ValueError:
                    continue
            return value
        return value.strftime("%Y-%m-%d")

    def compact_line(self):
        return f"{self.name} | {self.area} ha | {self.soil_type} | {self.format_date(self.sample_date)}"

    def render_history(self, previous=None):
        lines = [self.compact_line()]
        if previous:
            for record in reversed(previous):
                lines.append(f"  -> {record.compact_line()}")
        return "\n".join(lines)


def build_view(records, target_index):
    target = records[target_index]
    previous = records[:target_index]
    return SoilRecordView(
        name=target.name,
        area=target.area,
        soil_type=target.soil_type,
        sample_date=target.sample_date,
    ), previous


if __name__ == "__main__":
    history = [
        SoilRecordView("North Field", 12.5, "Loam", "2023-05-10"),
        SoilRecordView("North Field", 12.5, "Loam", "2024-05-11"),
        SoilRecordView("North Field", 13.0, "Clay", "2025-05-12"),
    ]
    view, prior = build_view(history, 2)
    print(view.render_history(prior))
