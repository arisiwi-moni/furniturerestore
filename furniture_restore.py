# === Stage 1: Каркас модуля ===
# Project: FurnitureRestore
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Item:
    """Предмет мебели, подлежащий реставрации."""

    name: str
    era: str
    material: str
    condition: str
    notes: str = ""
    tags: List[str] = field(default_factory=list)


def demo_items() -> List[Item]:
    """Создаёт демонстрационные записи предметов."""

    return [
        Item(
            name="Секретарь",
            era="XVIII век",
            material="Дуб",
            condition="Среднее",
            notes="Трещина на фасаде, потёртости.",
            tags=["дерево", "письменный"],
        ),
        Item(
            name="Кресло",
            era="XX век",
            material="Бук",
            condition="Хорошее",
            notes="Минимальный ремонт.",
            tags=["дерево", "сидение"],
        ),
        Item(
            name="Шкаф",
            era="XIX век",
            material="Сосна",
            condition="Плохое",
            notes="Перекос, облупилась краска.",
            tags=["дерево", "хранение"],
        ),
    ]


def print_items(items: List[Item]) -> None:
    """Выводит список предметов в читаемом виде."""

    for index, item in enumerate(items, start=1):
        print(f"#{index} {item.name} ({item.era})")
        print(f"    Материал: {item.material}")
        print(f"    Состояние: {item.condition}")
        if item.notes:
            print(f"    Заметки: {item.notes}")
        if item.tags:
            print(f"    Теги: {', '.join(item.tags)}")
        print()


def main() -> None:
    """Точка входа модуля проекта FurnitureRestore."""

    print("FurnitureRestore — Реставрация мебели")
    print("=" * 35)
    items = demo_items()
    print_items(items)
    print(f"Загружено предметов: {len(items)}")


if __name__ == "__main__":
    main()
