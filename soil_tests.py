# === Stage 1: Каркас модуля ===
# Project: SoilTests
from datetime import date


class Plot:
    def __init__(self, name, area, soil_type, sample_date):
        self.name = name
        self.area = area
        self.soil_type = soil_type
        self.sample_date = sample_date

    def __repr__(self):
        return (
            f"Plot(name={self.name!r}, area={self.area}, "
            f"soil_type={self.soil_type!r}, sample_date={self.sample_date})"
        )


def create_demo_plots():
    return [
        Plot("North Field", 1200.0, "loam", date(2024, 3, 14)),
        Plot("South Meadow", 850.0, "clay", date(2024, 3, 16)),
        Plot("East Ridge", 2400.0, "sandy", date(2024, 3, 18)),
    ]


def main():
    plots = create_demo_plots()
    print("SoilTests Demo")
    print("=" * 20)
    for plot in plots:
        print(plot)


if __name__ == "__main__":
    main()
