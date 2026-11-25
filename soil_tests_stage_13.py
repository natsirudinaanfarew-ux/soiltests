# === Stage 13: Массовое обновление ===
# Project: SoilTests
from datetime import date


class Plot:
    def __init__(self, name, area, soil_type, sample_date):
        self.name = name
        self.area = area
        self.soil_type = soil_type
        self.sample_date = sample_date


class Fieldbook:
    def __init__(self):
        self.plots = []
        self._selection = []

    def add_plot(self, plot):
        self.plots.append(plot)

    def select(self, plot):
        if plot in self.plots:
            if plot not in self._selection:
                self._selection.append(plot)

    def clear_selection(self):
        self._selection = []

    def preview(self, attribute, old_value, new_value):
        preview = []
        for plot in self._selection:
            if getattr(plot, attribute) != old_value:
                preview.append(
                    f"{plot.name}: {attribute} {old_value!r} -> {new_value!r} (skipped, already {old_value!r})"
                )
            else:
                preview.append(f"{plot.name}: {attribute} {old_value!r} -> {new_value!r}")
        return preview

    def apply(self, attribute, new_value):
        for plot in self._selection:
            setattr(plot, attribute, new_value)
        self.clear_selection()

    def report(self):
        lines = ["Mass update report", "=" * 40]
        lines.append(f"Selected plots: {len(self._selection)}")
        lines.extend(self.preview("name", "name", "name"))
        lines.append("-" * 40)
        return lines
