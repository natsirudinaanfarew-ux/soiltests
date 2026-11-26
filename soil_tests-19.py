# === Stage 19: Скользящее среднее ===
# Project: SoilTests
"""
moving_average.py

Independent module for SoilTests.
Computes a moving average over a numeric indicator (pH) collected across
soil samples belonging to a given plot.
"""

from statistics import mean


def moving_average(values, window):
    """Return the moving average of ``values`` using a sliding window.

    ``values`` is an iterable of numbers in chronological order.
    ``window`` is the number of consecutive samples to average.
    Returns a list of floats, one entry per position where a full
    window is available.
    """
    if window <= 0:
        raise ValueError("window must be a positive integer")

    result = []
    for i in range(len(values) - window + 1):
        chunk = values[i:i + window]
        result.append(mean(chunk))
    return result


def trailing_average(values, window):
    """Return the trailing moving average (window anchored at the end).

    Each entry reflects the average of the last ``window`` samples
    available up to and including the current position. The first
    ``window - 1`` entries are not defined and are returned as None.
    """
    if window <= 0:
        raise ValueError("window must be a positive integer")

    result = [None] * max(0, len(values) - window + 1)
    if not values:
        return result

    buffer = []
    for idx, value in enumerate(values):
        buffer.append(value)
        if len(buffer) > window:
            buffer.pop(0)
        if len(buffer) == window:
            result[idx] = mean(buffer)
    return result


def report_moving_average(plot_name, window, values):
    """Build a short human-readable report of the moving average.

    ``plot_name`` identifies the soil plot.
    ``values`` is the list of numeric pH readings for that plot.
    ``window`` is the averaging window size.
    """
    averages = moving_average(values, window)
    if not averages:
        return f"Plot '{plot_name}': insufficient data for moving average"

    line = f"Plot '{plot_name}' - pH moving average (window={window}):"
    for i, avg in enumerate(averages):
        line += f" {i + 1}:{avg:.2f}"
    return line
