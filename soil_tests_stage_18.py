# === Stage 18: Месячный отчёт ===
# Project: SoilTests
import calendar
from datetime import datetime


def build_month_report(month, year, samples, last_month_samples=None):
    """Assemble a monthly soil-analysis report with totals and month-over-month comparison."""
    months = list(calendar.month_name[1:])
    month_name = months[(month - 1) % 12]
    total_area = 0.0
    total_acidity = 0.0
    total_fertilizer = 0.0
    sample_count = 0
    for sample in samples:
        total_area += sample["area"]
        total_acidity += sample["ph"]
        total_fertilizer += sample["fertilizer"]
        sample_count += 1
    average_ph = total_acidity / sample_count if sample_count else 0.0
    average_fertilizer = total_fertilizer / sample_count if sample_count else 0.0
    comparison = {}
    if last_month_samples is not None:
        last_ph = sum(s["ph"] for s in last_month_samples) / len(last_month_samples)
        last_fert = sum(s["fertilizer"] for s in last_month_samples) / len(last_month_samples)
        ph_delta = average_ph - last_ph
        fert_delta = average_fertilizer - last_fert
        comparison = {
            "ph_change": round(ph_delta, 2),
            "fertilizer_change": round(fert_delta, 2),
        }
    report = {
        "period": f"{month_name} {year}",
        "samples": sample_count,
        "total_area": round(total_area, 2),
        "average_ph": round(average_ph, 2),
        "average_fertilizer": round(average_fertilizer, 2),
        "comparison": comparison,
    }
    return report


if __name__ == "__main__":
    current = [
        {"ph": 6.5, "fertilizer": 12.0, "area": 1.5},
        {"ph": 7.0, "fertilizer": 8.0, "area": 2.0},
        {"ph": 6.8, "fertilizer": 15.0, "area": 1.0},
    ]
    previous = [
        {"ph": 6.2, "fertilizer": 10.0, "area": 1.5},
        {"ph": 6.7, "fertilizer": 9.0, "area": 2.0},
        {"ph": 6.9, "fertilizer": 14.0, "area": 1.0},
    ]
    print(build_month_report(datetime.now().month, datetime.now().year, current, previous))
