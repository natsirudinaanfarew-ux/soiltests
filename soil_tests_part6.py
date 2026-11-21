# === Stage 6: Связанная сущность ===
# Project: SoilTests
"""SoilTests stage 6: sample entity and its registration."""

from datetime import date

SAMPLES = {}


def add_sample(site_id, name, ph, date_of_test):
    """Register a soil sample against an existing site.

    site_id: identifier of the site the sample belongs to.
    name: descriptive label for the sample.
    ph: measured acidity value of the sample.
    date_of_test: date the sample was taken.

    Returns the stored sample identifier or None if the site is unknown.
    """
    if site_id not in SAMPLES:
        return None
    sample_id = len(SAMPLES) + 1
    SAMPLES[sample_id] = {
        "sample_id": sample_id,
        "site_id": site_id,
        "name": name,
        "ph": ph,
        "date_of_test": date_of_test,
    }
    return sample_id
