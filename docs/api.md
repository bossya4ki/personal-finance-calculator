# Функции программы

- `read_operations(path)` восстанавливает записи из JSON.
- `add_operation(...)` проверяет сумму, дату и категорию и добавляет операцию.
- `save_operations(path, operations)` сохраняет список.
- `balance(operations)` вычисляет разность доходов и расходов через Decimal.
