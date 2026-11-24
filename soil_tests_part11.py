# === Stage 11: Быстрые фильтры ===
# Project: SoilTests
from datetime import datetime, timedelta

# SoilTests - Stage 11: fast filters for soil sample records ("участок")
# Filter records by sampling date: today, this week, and overdue.

WEEKDAY_LIMIT = 6  # Monday..Saturday; Sunday (0) is excluded from "this week"

def parse_date(value):
    return datetime.strptime(value, "%Y-%m-%d").date()

def filter_records(records, sample_field, date_field):
    today = datetime.now().date()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=WEEKDAY_LIMIT)

    result = {
        "today": [],
        "this_week": [],
        "overdue": [],
    }

    for record in records:
        raw = record.get(date_field)
        if raw is None:
            continue
        try:
            record_date = parse_date(raw)
        except ValueError:
            continue

        if record_date == today:
            result["today"].append(record)
        elif week_start <= record_date <= week_end:
            result["this_week"].append(record)
        elif record_date < today:
            result["overdue"].append(record)

    return result


def run_stage_11(records, sample_field="sample_id", date_field="sample_date"):
    """Apply Stage 11 fast filters to a list of soil sample records.

    Args:
        records: iterable of record dictionaries.
        sample_field: key holding the unique sample identifier.
        date_field: key holding the sampling date as a YYYY-MM-DD string.

    Returns:
        dict with keys "today", "this_week", and "overdue", each mapping to
        the list of matching records.
    """
    return filter_records(records, sample_field, date_field)


if __name__ == "__main__":
    sample_records = [
        {"sample_id": "S001", "soil_area": "Plot A", "sample_date": "2025-06-15"},
        {"sample_id": "S002", "soil_area": "Plot B", "sample_date": "2025-06-20"},
        {"sample_id": "S003", "soil_area": "Plot C", "sample_date": "2025-06-10"},
        {"sample_id": "S004", "soil_area": "Plot D", "sample_date": "2025-06-23"},
        {"sample_id": "S005", "soil_area": "Plot E", "sample_date": "2025-06-18"},
    ]

    filtered = run_stage_11(sample_records)
    for label in ("today", "this_week", "overdue"):
        print(label, filtered[label])
