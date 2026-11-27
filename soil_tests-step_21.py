# === Stage 21: Сравнение периодов ===
# Project: SoilTests
from datetime import date


class SoilPeriod:
    """A sampling period defined by a name and a soil test record."""

    def __init__(self, name, soil_area_name, ph, nitrogen, phosphorus, potassium, soil_date):
        self.name = name
        self.soil_area_name = soil_area_name
        self.ph = ph
        self.nitrogen = nitrogen
        self.phosphorus = phosphorus
        self.potassium = potassium
        self.soil_date = soil_date

    def key_indicators(self):
        return [self.ph, self.nitrogen, self.phosphorus, self.potassium]


def compare_periods(period_a, period_b, tolerance=0.5):
    """Compare two soil periods by their key indicators.

    Returns a list of (indicator, delta) tuples for values that differ
    by more than the given tolerance, sorted by absolute delta descending.
    """
    differences = []
    for index, value_a in enumerate(period_a.key_indicators()):
        value_b = period_b.key_indicators()[index]
        delta = value_a - value_b
        if abs(delta) > tolerance:
            differences.append((period_a.name, period_b.name, index, delta))
    differences.sort(key=lambda item: abs(item[3]), reverse=True)
    return differences


def summarize_comparison(differences):
    """Produce a short human-readable summary of the comparison result."""
    if not differences:
        return "No significant differences between the periods."
    lines = []
    for period_a_name, period_b_name, indicator, delta in differences:
        indicator_names = ["acidity (pH)", "nitrogen", "phosphorus", "potassium"]
        label = indicator_names[indicator]
        direction = "higher" if delta > 0 else "lower"
        lines.append(
            f"{period_a_name} {direction} than {period_b_name} by {abs(delta):.2f} in {label}"
        )
    return "\n".join(lines)


def compare_periods_by_date(period_a, period_b):
    """Return the earlier and later periods by sampling date."""
    if period_a.soil_date < period_b.soil_date:
        return period_a, period_b
    if period_a.soil_date > period_b.soil_date:
        return period_b, period_a
    return period_a, period_b


if __name__ == "__main__":
    earlier = SoilPeriod(
        name="Spring2024",
        soil_area_name="NorthField",
        ph=6.2,
        nitrogen=30.0,
        phosphorus=15.0,
        potassium=120.0,
        soil_date=date(2024, 4, 12),
    )
    later = SoilPeriod(
        name="Autumn2024",
        soil_area_name="NorthField",
        ph=5.9,
        nitrogen=55.0,
        phosphorus=20.0,
        potassium=118.0,
        soil_date=date(2024, 10, 5),
    )
    ordered = compare_periods_by_date(earlier, later)
    summary = summarize_comparison(compare_periods(*ordered))
    print(summary)
