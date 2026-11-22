# === Stage 9: Теги ===
# Project: SoilTests
from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class SoilTag:
    name: str
    color: str = "#8d8d8d"


class SoilTagCollection:
    def __init__(self) -> None:
        self._tags: Dict[str, SoilTag] = {}

    def add(self, name: str, color: Optional[str] = None) -> SoilTag:
        if not name:
            raise ValueError("Tag name cannot be empty")
        if name not in self._tags:
            self._tags[name] = SoilTag(name=name, color=color or self._default_color(name))
        return self._tags[name]

    def remove(self, name: str) -> bool:
        return self._tags.pop(name, None) is not None

    def find(self, name: str) -> Optional[SoilTag]:
        return self._tags.get(name)

    def __contains__(self, name: str) -> bool:
        return name in self._tags

    def __len__(self) -> int:
        return len(self._tags)

    def _default_color(self, name: str) -> str:
        hue = sum(ord(c) for c in name) % 360
        return f"hsl({hue}, 45%, 55%)"


def tag_soil(soil: "Soil", tag_name: str, collection: SoilTagCollection) -> SoilTag:
    tag = collection.add(tag_name)
    soil.tags.append(tag.name)
    return tag


def untag_soil(soil: "Soil", tag_name: str, collection: SoilTagCollection) -> bool:
    if tag_name in soil.tags:
        soil.tags.remove(tag_name)
    return collection.remove(tag_name)


def find_soils_by_tag(soils: List["Soil"], tag_name: str) -> List["Soil"]:
    return [soil for soil in soils if tag_name in soil.tags]
