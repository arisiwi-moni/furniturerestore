# === Stage 2: Проверка полей ===
# Project: FurnitureRestore
import re


def normalize_name(value):
    cleaned = value.strip().lower()
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned


def normalize_era(value):
    value = value.strip()
    eras = {"средние века": "Средние века",
            "эпоха Возрождения": "Эпоха Возрождения",
            "викторианская": "Викторианская",
            "современная": "Современная"}
    return eras.get(value, value) if value else value


def normalize_material(value):
    value = value.strip().lower()
    materials = {"дерево": "Дерево",
                 "дуб": "Дуб",
                 "сосна": "Сосна",
                 "липа": "Липа",
                 "кожа": "Кожа",
                 "кованый металл": "Кованый металл"}
    return materials.get(value, value) if value else value


def normalize_condition(value):
    value = value.strip().lower()
    conditions = {"отличное": "Отличное",
                  "хорошее": "Хорошее",
                  "среднее": "Среднее",
                  "плохое": "Плохое",
                  "критическое": "Критическое"}
    return conditions.get(value, value) if value else value


def validate_item(item):
    errors = []
    if not item.get("название"):
        errors.append("Название предмета обязательно")
    if not item.get("эпоха"):
        errors.append("Укажите эпоху предмета")
    if not item.get("материал"):
        errors.append("Укажите материал предмета")
    if not item.get("состояние"):
        errors.append("Укажите состояние предмета")
    if "название" in item and not item["название"].strip():
        errors.append("Название предмета не может быть пустым")
    if errors:
        return errors
    return None


def build_item_record(raw):
    name = normalize_name(raw.get("название", ""))
    era = normalize_era(raw.get("эпоха", ""))
    material = normalize_material(raw.get("материал", ""))
    condition = normalize_condition(raw.get("состояние", ""))
    cleaned = {"название": name,
               "эпоха": era,
               "материал": material,
               "состояние": condition}
    errors = validate_item(cleaned)
    return (cleaned, errors) if errors else None
