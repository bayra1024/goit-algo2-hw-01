dictionary = [8, 2, 7, 1, 3, 6, 4]


def min_max(input_list):
    if len(input_list) == 1:
        print(f"return {input_list[0]}")
        return input_list[0], input_list[0]
    else:
        print(f"split {input_list}")
        mid = len(input_list) // 2
        left = input_list[:mid]
        right = input_list[mid:]
        # Рекурсивне розділення
        left = min_max(left)
        right = min_max(right)
        # Об'єднання результатів
        print(f"merge {left} and {right}")
        return min(left[0], right[0]), max(left[1], right[1])


print(min_max(dictionary))
