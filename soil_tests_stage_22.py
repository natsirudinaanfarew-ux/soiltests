# === Stage 22: Календарная сетка ===
# Project: SoilTests
"""Calendar view for a soil sample month.

Renders a sample as a text grid spanning the month of the sample date,
showing sample markers on the relevant days.
"""

from calendar import month_name
from datetime import date, timedelta


def render_sample_calendar(sample_name, sample_date):
    """Return a text grid showing the sample positioned on its month.

    Args:
        sample_name: identifier of the soil sample to place on the grid.
        sample_date: date on which the sample was taken.

    Returns:
        A multi-line string with the month header, weekday labels,
        day numbers, and a marker for the sample day.
    """
    year, month, day = sample_date.year, sample_date.month, sample_date.day
    first_weekday = sample_date.weekday()
    days_in_month = sample_date.month_length(year, month)
    grid = []
    grid.append(f"{month_name[month - 1]} {year}")
    grid.append("Mon Tue Wed Thu Fri Sat Sun")
    row = []
    for offset in range(first_weekday):
        row.append("")
    for current in range(1, days_in_month + 1):
        row.append(str(current))
        if current == day:
            row[-1] = f"*{sample_name}"
        if len(row) == 7:
            grid.append(" ".join(row))
            row = []
    if row:
        grid.append(" ".join(row))
    return "\n".join(grid)


def month_length(year, month):
    """Return the number of days in the given year-month."""
    if month == 12:
        return (date(year + 1, 1, 1) - timedelta(days=1)).day
    return (date(year, month + 1, 1) - timedelta(days=1)).day
