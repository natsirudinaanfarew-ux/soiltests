# === Stage 5: Удаление и восстановление ===
# Project: SoilTests
from datetime import date


class SoilPlot:
    """A soil analysis plot with soft-delete support."""

    def __init__(self, name, area, soil_type, sample_date):
        self.name = name
        self.area = area
        self.soil_type = soil_type
        self.sample_date = sample_date
        self.deleted = False

    def delete(self):
        """Soft-delete the plot: mark it without removing data."""
        self.deleted = True

    def restore(self):
        """Restore a soft-deleted plot."""
        self.deleted = False

    @property
    def is_active(self):
        """Whether the plot is currently available."""
        return not self.deleted

    def __repr__(self):
        status = "active" if self.is_active else "deleted"
        return f"SoilPlot(name={self.name!r}, area={self.area}, soil_type={self.soil_type!r}, sample_date={self.sample_date}, status={status})"


def soft_delete_plot(plot):
    """Convenience helper to soft-delete a plot by reference."""
    plot.delete()


def restore_plot(plot):
    """Convenience helper to restore a soft-deleted plot by reference."""
    plot.restore()


def find_active_plot(plots, name):
    """Return the first active plot with the given name, or None."""
    for plot in plots:
        if plot.is_active and plot.name == name:
            return plot
    return None


def find_deleted_plot(plots, name):
    """Return the first soft-deleted plot with the given name, or None."""
    for plot in plots:
        if not plot.is_active and plot.name == name:
            return plot
    return None


if __name__ == "__main__":
    demo_plots = [
        SoilPlot("North Field", 1200, "loam", date(2024, 5, 12)),
        SoilPlot("South Field", 800, "clay", date(2024, 6, 3)),
    ]

    demo_plots[0].delete()

    print("Active plots:")
    for plot in demo_plots:
        if plot.is_active:
            print(" ", plot)

    print("Deleted plots:")
    for plot in demo_plots:
        if not plot.is_active:
            print(" ", plot)

    print("Lookup 'North Field':", find_active_plot(demo_plots, "North Field"))
    print("Lookup 'South Field':", find_active_plot(demo_plots, "South Field"))

    demo_plots[0].restore()
    print("After restore, lookup 'North Field':", find_active_plot(demo_plots, "North Field"))
