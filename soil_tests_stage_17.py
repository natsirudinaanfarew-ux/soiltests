# === Stage 17: Недельный отчёт ===
# Project: SoilTests
from datetime import datetime


def format_soil_report(sections, samples):
    """Build a weekly soil report as a plain-text table.

    Args:
        sections: list of dicts with keys name, area, soil_type, sample_date.
        samples: list of dicts with keys ph and fertilizer.

    Returns:
        str: formatted weekly report.
    """
    lines = []
    lines.append("Soil Tests - Weekly Report")
    lines.append("=" * 60)
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")

    lines.append("Sections")
    lines.append("-" * 60)
    header = f"{'Section':<20}{'Area (ha)':>12}{'Soil Type':<20}{'Sample Date':>15}"
    lines.append(header)
    lines.append("-" * 60)
    for s in sections:
        lines.append(
            f"{s['name']:<20}{s['area']:>12.2f}"
            f"{s['soil_type']:<20}{s['sample_date']:>15}"
        )
    lines.append("")

    lines.append("Samples")
    lines.append("-" * 60)
    header = f"{'Section':<20}{'PH':>8}{'Fertilizer':<20}"
    lines.append(header)
    lines.append("-" * 60)
    for s in samples:
        section_name = "N/A"
        for sec in sections:
            if s['section'] == sec['name']:
                section_name = sec['name']
                break
        lines.append(
            f"{section_name:<20}{s['ph']:>8.1f}{s['fertilizer']:<20}"
        )
    lines.append("")

    return "\n".join(lines)


def generate_weekly_report(sections, samples):
    """Generate a weekly soil report and return it as a string."""
    return format_soil_report(sections, samples)
