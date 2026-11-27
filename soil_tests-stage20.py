# === Stage 20: Текстовая гистограмма ===
# Project: SoilTests
from collections import Counter


def build_soil_type_histogram(probes):
    """Build a textual histogram of soil type distribution."""
    counter = Counter(probe["soil_type"] for probe in probes)
    width = max(counter.values(), default=0)
    if width == 0:
        return ""
    max_width = 20
    width = min(width, max_width)
    lines = []
    for soil_type, count in counter.most_common():
        bar = "#" * count
        if count > width:
            bar = bar[:width] + "->"
        lines.append(f"{soil_type:<15} {bar}")
    return "\n".join(lines)


def render_soil_type_histogram(probes, separator="=" * 40):
    """Render a textual histogram of soil type distribution."""
    distribution = build_soil_type_histogram(probes)
    header = f"Soil Type Distribution (max={max(Counter(p['soil_type'] for p in probes), default=0)})"
    return f"{separator}\n{header}\n{separator}\n{distribution}\n{separator}"


def display_soil_type_histogram(probes):
    """Display a textual histogram of soil type distribution."""
    print(render_soil_type_histogram(probes))


if __name__ == "__main__":
    sample_probes = [
        {"soil_type": "clay"},
        {"soil_type": "clay"},
        {"soil_type": "clay"},
        {"soil_type": "sandy"},
        {"soil_type": "sandy"},
        {"soil_type": "loam"},
        {"soil_type": "loam"},
        {"soil_type": "peaty"},
    ]
    display_soil_type_histogram(sample_probes)
