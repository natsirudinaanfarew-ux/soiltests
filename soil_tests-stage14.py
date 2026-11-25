# === Stage 14: Избранное ===
# Project: SoilTests
class SoilSection:
    def __init__(self, name, area, soil_type, sample_date):
        self.name = name
        self.area = area
        self.soil_type = soil_type
        self.sample_date = sample_date
        self.is_favourite = False

    def toggle_favourite(self):
        self.is_favourite = not self.is_favourite

    def is_favourite(self):
        return self.is_favourite
