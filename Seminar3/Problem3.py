# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

def find_combinations(items, max_weight):
    if not items or max_weight <= 0:
        return [[]]
    items_list = list(items.items())
    first_item, first_weight = items_list[0]
    combos_without_first = find_combinations(dict(items_list[1:]), max_weight)
    combos_with_first = []
    if first_weight <= max_weight:
        combos_with_first = find_combinations(dict(items_list[1:]), max_weight - first_weight)
        combos_with_first = [[first_item] + combo for combo in combos_with_first]
    return combos_without_first + combos_with_first

items = {
    "Палатка": 4,
    "Спальник": 3,
    "Котелок": 1,
    "Фонарик": 0.5,
    "Еда": 2
}
print(items)

max_weight = 5
print(max_weight)

all_combinations = find_combinations(items, max_weight)

print("Один из вариантов:", all_combinations[1])

print("Все возможные варианты:")
for combo in all_combinations:
    print(combo)