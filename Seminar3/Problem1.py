# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

list1 = [1,2,1,3,4,5,6,6,8,8,9,9,9,0,0,0,0,0]


def find_duplicates(input_list):
    seen = set()
    duplicates = []
    for item in input_list:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.add(item)
    return duplicates


list2 = find_duplicates(list1)

print(list2)