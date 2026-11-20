# === Stage 4: Редактирование записей ===
# Project: SoilTests
# Stage 4: Edit a plot entity by identifier, allowing only permitted fields.
# Standalone module using only the standard library.

VALID_PLOT_FIELDS = frozenset({"name", "area", "soil_type"})

ALLOWED_SOIL_TYPES = frozenset({"clay", "sandy", "loam", "chalk", "peat"})


def normalize_plot_value(value):
    """Normalize a single plot field value to a plain string, or return None."""
    if value is None:
        return None
    if isinstance(value, bool):
        return str(value)
    return str(value).strip()


def validate_plot_update(update):
    """Validate a plot-update mapping.

    Returns a new dict containing only permitted fields with normalized values.
    Raises ValueError if any field is not allowed or any value is invalid.
    """
    if not isinstance(update, dict):
        raise ValueError("Plot update must be a mapping of field names to values.")

    if not update:
        return {}

    unknown = set(update) - VALID_PLOT_FIELDS
    if unknown:
        raise ValueError(
            "Unknown plot field(s): " + ", ".join(sorted(unknown))
        )

    normalized = {}
    for key, raw in update.items():
        if key not in VALID_PLOT_FIELDS:
            raise ValueError("Unknown plot field: " + key)
        normalized_value = normalize_plot_value(raw)
        if key == "soil_type" and normalized_value not in ALLOWED_SOIL_TYPES:
            raise ValueError(
                "Invalid soil_type: " + repr(normalized_value)
            )
        if normalized_value is not None and normalized_value == "":
            raise ValueError("Plot field " + key + " must not be empty.")
        normalized[key] = normalized_value

    return normalized


def apply_plot_update(plot, update):
    """Return a copy of plot with the permitted fields from update applied."""
    normalized = validate_plot_update(update)
    new_plot = dict(plot)
    for key, value in normalized.items():
        new_plot[key] = value
    return new_plot
