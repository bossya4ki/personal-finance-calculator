from decimal import Decimal, InvalidOperation
from pathlib import Path

from operations import add_operation, read_operations, save_operations


def balance(operations):
    return sum((Decimal(row["amount"]) * (1 if row["kind"] == "income" else -1)
                for row in operations), Decimal("0.00"))


def main():
    path = Path("finance.json")
    try:
        operations = read_operations(path)
    except (OSError, ValueError) as error:
        print("Ошибка загрузки:", error)
        return
    while True:
        print("1 Доход | 2 Расход | 3 Список | 4 Баланс | 0 Выход")
        try:
            command = input("> ").strip()
            if command == "0":
                return
            if command in {"1", "2"}:
                updated = operations.copy()
                kind = "income" if command == "1" else "expense"
                add_operation(updated, kind, input("Сумма: "), input("Категория: "), input("Дата: "))
                save_operations(path, updated)
                operations = updated
                print("Операция сохранена.")
            elif command == "3":
                for row in operations:
                    label = "Доход" if row["kind"] == "income" else "Расход"
                    print(row["date"], label, row["category"], row["amount"], "руб.")
            elif command == "4":
                print(f"Баланс: {balance(operations):.2f} руб.")
            else:
                print("Выберите пункт меню.")
        except (EOFError, KeyboardInterrupt):
            return
        except (ValueError, InvalidOperation, OSError) as error:
            print("Ошибка:", error)


if __name__ == "__main__":
    main()
