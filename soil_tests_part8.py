# === Stage 8: Сортировка записей ===
# Project: SoilTests
from datetime import date


def sort_records(records, key_field, ascending):
    """Sort soil-test records by a given field, ascending or descending.

    Args:
        records (list): list of record dicts.
        key_field (str): field name to sort by.
        ascending (bool): sort direction; True for ascending, False for descending.
    """
    return sorted(records, key=lambda record: record.get(key_field), reverse=not ascending)


def sort_by_name(records, ascending=True):
    """Sort records by the 'name' field (soil type name)."""
    return sort_records(records, key_field="name", ascending=ascending)


def sort_by_date(records, ascending=True):
    """Sort records by the 'date' field (soil-test date)."""
    return sort_records(records, key_field="date", ascending=ascending)


def sort_records_multi(records, key_fields, ascending=True):
    """Sort records by multiple fields in the given order.

    The first field is the primary sort key; subsequent fields break ties.
    A single boolean controls all fields' sort direction.

    Args:
        records (list): list of record dicts.
        key_fields (list): ordered list of field names to sort by.
        ascending (bool): sort direction for all fields.
    """
    return sorted(
        records,
        key=lambda record: [record.get(field) for field in key_fields],
        reverse=not ascending,
    )


if __name__ == "__main__":
    sample_records = [
        {"name": "Clay", "date": date(2024, 5, 1)},
        {"name": "Sandy", "date": date(2024, 3, 15)},
        {"name": "Loam", "date": date(2024, 3, 15)},
        {"name": "Silt", "date": date(2024, 1, 10)},
    ]

    print("By name (ascending):")
    for record in sort_by_name(sample_records, ascending=True):
        print(record)

    print("\nBy name (descending):")
    for record in sort_by_name(sample_records, ascending=False):
        print(record)

    print("\nBy date (ascending):")
    for record in sort_by_date(sample_records, ascending=True):
        print(record)

    print("\nBy date (descending):")
    for record in sort_by_date(sample_records, ascending=False):
        print(record)

    print("\nBy name then date (ascending):")
    for record in sort_records_multi(sample_records, key_fields=["name", "date"], ascending=True):
        print(record)
