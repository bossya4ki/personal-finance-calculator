import json
from datetime import date
from decimal import Decimal
from pathlib import Path


def read_operations(path):
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def add_operation(operations, kind, amount, category, day):
    value = Decimal(amount.strip().replace(",", "."))
    if not value.is_finite() or value <= 0 or value.as_tuple().exponent < -2:
        raise ValueError("Введите положительную сумму с точностью до копейки")
    category = category.strip()
    if not category or kind not in {"income", "expense"}:
        raise ValueError("Укажите категорию и тип операции")
    parsed_day = date.fromisoformat(day)
    if parsed_day.isoformat() != day:
        raise ValueError("Используйте формат ГГГГ-ММ-ДД")
    operations.append({"kind": kind, "amount": format(value, ".2f"),
                       "category": category, "date": day})


def save_operations(path, operations):
    temporary = path.with_name("." + path.name + ".tmp")
    temporary.write_text(json.dumps(operations, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(path)
