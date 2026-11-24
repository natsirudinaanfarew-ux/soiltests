# === Stage 12: Поиск дубликатов ===
# Project: SoilTests
from datetime import date


def normalize_field(value):
    """Return a normalized string representation of a field value."""
    if value is None:
        return ""
    return str(value).strip().lower()


def normalize_date(value):
    """Normalize a date value to a comparable 'YYYY-MM-DD' string."""
    if value is None:
        return ""
    if isinstance(value, date):
        return value.isoformat()
    text = str(value).strip()
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%m/%d/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(text, fmt).isoformat()
        except ValueError:
            continue
    return text


def canonical_key(record):
    """Build a canonical key from a soil plot record."""
    title = normalize_field(record.get("name"))
    area = normalize_field(record.get("area"))
    soil = normalize_field(record.get("soil_type"))
    sample_date = normalize_date(record.get("sample_date"))
    return f"{title}|{area}|{soil}|{sample_date}"


def find_duplicate_indices(records):
    """Return indices of records that have duplicate canonical keys."""
    key_index = {}
    for index, record in enumerate(records):
        key = canonical_key(record)
        key_index.setdefault(key, []).append(index)
    duplicates = []
    for indices in key_index.values():
        if len(indices) > 1:
            duplicates.extend(indices)
    return duplicates


def group_duplicate_indices(records):
    """Group indices of records that share a canonical key."""
    key_index = {}
    for index, record in enumerate(records):
        key = canonical_key(record)
        key_index.setdefault(key, []).append(index)
    return [indices for indices in key_index.values() if len(indices) > 1]


def remove_duplicates(records):
    """Return a list with duplicate canonical keys removed, preserving order."""
    key_index = {}
    for index, record in enumerate(records):
        key = canonical_key(record)
        if key in key_index:
            continue
        key_index[key] = index
    return [records[key_index[key]] for key in key_index]
