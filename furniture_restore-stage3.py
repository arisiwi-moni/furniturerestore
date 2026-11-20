# === Stage 3: Хранилище в памяти ===
# Project: FurnitureRestore
items_store.py

from typing import Dict, List, Optional, Type, Any


class FurnitureItem:
    """Сущность «предмет»: название, эпоха, материал, состояние.

    Идентификатор формируется автоматически при создании экземпляра
    и сохраняется в атрибуте id.
    """

    def __init__(self, name: str, era: str, material: str, condition: str,
                 item_id: Optional[str] = None) -> None:
        self.name = name
        self.era = era
        self.material = material
        self.condition = condition
        self.id = item_id or str(len(_items_store)) + 1


class ItemsStore:
    """Память для предметов: добавление, получение и перебор."""

    def __init__(self) -> None:
        self._data: Dict[str, FurnitureItem] = {}

    def add(self, item: FurnitureItem) -> FurnitureItem:
        """Добавить предмет под своим id, перезаписав прежние данные."""
        self._data[item.id] = item
        return item

    def get(self, item_id: str) -> Optional[FurnitureItem]:
        """Вернуть предмет по id или None, если его нет."""
        return self._data.get(item_id)

    def all_items(self) -> List[FurnitureItem]:
        """Вернуть все предметы в порядке возрастания id."""
        return [self._data[item_id] for item_id in sorted(self._data)]

    def __len__(self) -> int:
        return len(self._data)


_items_store = ItemsStore()


def create_item(name: str, era: str, material: str, condition: str) -> FurnitureItem:
    """Создать предмет и сохранить его в глобальном хранилище."""
    item = FurnitureItem(name, era, material, condition)
    _items_store.add(item)
    return item


def get_item(item_id: str) -> Optional[FurnitureItem]:
    """Получить предмет по id из глобального хранилища."""
    return _items_store.get(item_id)


def list_items() -> List[FurnitureItem]:
    """Получить список всех предметов из глобального хранилища."""
    return _items_store.all_items()


if __name__ == "__main__":
    create_item("Стул", "XVIII век", "Дуб", "Хорошее")
    create_item("Стол", "XIX век", "Сосна", "Плохое")
    print(f"Всего предметов: {len(_items_store)}")
    for item in list_items():
        print(item.id, item.name, item.era, item.material, item.condition)
    found = get_item("1")
    if found:
        print("Найдено:", found.name)
    else:
        print("Не найдено")
