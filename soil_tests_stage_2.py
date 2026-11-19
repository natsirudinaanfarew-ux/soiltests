# === Stage 2: Проверка полей ===
# Project: SoilTests
"""Validation and input normalization for the SoilTests 'участок' entity."""

from datetime import date


def normalize_str(value):
    """Return a trimmed, title-cased string, or raise ValueError if empty."""
    if value is None:
        raise ValueError("field is required")
    text = str(value).strip()
    if not text:
        raise ValueError("field cannot be empty")
    return text


def normalize_area(value):
    """Parse a positive float area, raising ValueError on bad input."""
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValueError("area must be a number")
    if number <= 0:
        raise ValueError("area must be greater than zero")
    return number


def normalize_soil_type(value):
    """Normalize soil type to a lower-case, whitespace-collapsed string."""
    text = normalize_str(value).lower()
    return " ".join(text.split())


def normalize_date(value):
    """Parse a date from 'YYYY-MM-DD' or an existing date object."""
    if isinstance(value, date):
        return value
    text = normalize_str(value)
    try:
        return date.fromisoformat(text)
    except ValueError:
        raise ValueError("date must be in YYYY-MM-DD format")


def validate_plot(name, area, soil_type, date_sampled):
    """Validate all fields of a 'участок' entity and return normalized values."""
    normalized_name = normalize_str(name)
    normalized_area = normalize_area(area)
    normalized_soil_type = normalize_soil_type(soil_type)
    normalized_date = normalize_date(date_sampled)
    return normalized_name, normalized_area, normalized_soil_type, normalized_date
