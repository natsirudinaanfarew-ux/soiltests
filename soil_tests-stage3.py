# === Stage 3: Хранилище в памяти ===
# Project: SoilTests
"""SoilTests: in-memory store for soil plots (участок)."""

import string
import random


class PlotError(Exception):
    """Raised on invalid plot operations."""


class Plot:
    """A soil plot: name, area, soil type, and sampling date."""

    def __init__(self, name, area, soil_type, sample_date):
        self.name = name
        self.area = area
        self.soil_type = soil_type
        self.sample_date = sample_date
        self.id = self._generate_id()

    @staticmethod
    def _generate_id():
        alphabet = string.ascii_uppercase + string.digits
        return ''.join(random.choice(alphabet) for _ in range(6))

    def __repr__(self):
        return f"Plot(id={self.id!r}, name={self.name!r}, area={self.area}, soil_type={self.soil_type!r}, sample_date={self.sample_date!r})"


class PlotStore:
    """A simple in-memory store for Plot entities, keyed by id."""

    def __init__(self):
        self._plots = {}

    def add(self, plot):
        if plot.id in self._plots:
            raise PlotError(f"Plot with id {plot.id!r} already exists")
        self._plots[plot.id] = plot
        return plot

    def get(self, plot_id):
        if plot_id not in self._plots:
            raise PlotError(f"Plot with id {plot_id!r} not found")
        return self._plots[plot_id]

    def list(self):
        return list(self._plots.values())
