def is_anagram(first_string, second_string):
    first_string_list = list(first_string.lower())
    second_string_list = list(second_string.lower())

    quick_sort(first_string_list, 0, len(first_string_list) - 1)
    quick_sort(second_string_list, 0, len(second_string_list) - 1)

    first_string_ordered = "".join(first_string_list)
    second_string_ordered = "".join(second_string_list)

    if first_string == "" or second_string == "":
        return (first_string_ordered, second_string_ordered, False)

    if first_string_list == second_string_list:
        return (first_string_ordered, second_string_ordered, True)

    return (first_string_ordered, second_string_ordered, False)


# Algoritmo de Quick Sort retirado do Course
def quick_sort(letters, start, end):
    if start < end:
        p = partition(letters, start, end)
        quick_sort(letters, start, p - 1)
        quick_sort(letters, p + 1, end)


def partition(letters, start, end):
    pivot = letters[end]
    delimiter = start - 1

    for index in range(start, end):
        if letters[index] <= pivot:
            delimiter = delimiter + 1
            letters[index], letters[delimiter] = (
                letters[delimiter],
                letters[index],
            )

    letters[delimiter + 1], letters[end] = letters[end], letters[delimiter + 1]

    return delimiter + 1
