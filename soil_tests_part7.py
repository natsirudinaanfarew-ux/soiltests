# === Stage 7: Фильтрация записей ===
# Project: SoilTests
from datetime import date


def find_sections_by_area(sections, target_area):
    """Return the sections whose area equals target_area."""
    return [section for section in sections if section.area == target_area]


def find_sections_in_date_range(sections, start, end):
    """Return the sections sampled between start and end (inclusive)."""
    return [
        section
        for section in sections
        if start <= section.sample_date <= end
    ]


def find_sections_by_area_and_date_range(sections, target_area, start, end):
    """Return sections matching both an area value and a date range."""
    return [
        section
        for section in sections
        if section.area == target_area and start <= section.sample_date <= end
    ]


def find_sections_in_area_range(sections, min_area, max_area):
    """Return sections whose area falls within the inclusive [min_area, max_area]."""
    return [
        section
        for section in sections
        if min_area <= section.area <= max_area
    ]


def find_sections_by_soil_type_in_area_range(sections, soil_type, min_area, max_area):
    """Return sections of a given soil type with area within the inclusive range."""
    return [
        section
        for section in sections
        if section.soil_type == soil_type
        and min_area <= section.area <= max_area
    ]


def count_sections_by_area(sections, target_area):
    """Return how many sections have an area equal to target_area."""
    return len(find_sections_by_area(sections, target_area))


def filter_sections_by_area_and_date_range(sections, target_area, start, end):
    """Return sections with a matching area sampled within the inclusive date range."""
    return find_sections_by_area_and_date_range(sections, target_area, start, end)


def format_area_filter_result(matched, total):
    """Return a short human-readable summary of an area-based filter run."""
    return (
        f"Matched {len(matched)} of {total} sections "
        f"by area: {[section.name for section in matched]}"
    )


def format_date_range_filter_result(matched, total):
    """Return a short human-readable summary of a date-range filter run."""
    return (
        f"Matched {len(matched)} of {total} sections "
        f"within date range: "
        f"{[section.sample_date.isoformat() for section in matched]}"
    )


def apply_area_and_date_filters(sections, area, start, end):
    """Apply area equality and inclusive date-range filters to a section list."""
    return find_sections_by_area_and_date_range(sections, area, start, end)


def apply_area_range_filter(sections, min_area, max_area):
    """Apply an inclusive area-range filter to a section list."""
    return find_sections_in_area_range(sections, min_area, max_area)
