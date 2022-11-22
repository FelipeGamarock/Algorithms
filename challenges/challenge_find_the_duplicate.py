def find_duplicate(nums):
    nums_set = set(nums)
    for num in nums_set:
        if type(num) is not int or num <= 0:
            return False
        nums.remove(num)

    if len(nums) == 0:
        return False

    return nums[0]
    # quick_sort(nums, 0, len(nums) - 1)
    # print(nums)
    # old_num = 0
    # for num in nums:
    #     if type(num) is not int or num <= 0:
    #         return False
    #     if num == old_num:
    #         return num
    #     old_num = num
    # return False



# Algoritmo de Quick Sort retirado do Course
# def quick_sort(numbers, start, end):
#     if start < end:
#         p = partition(numbers, start, end)
#         quick_sort(numbers, start, p - 1)
#         quick_sort(numbers, p + 1, end)


# def partition(numbers, start, end):
#     pivot = numbers[end]
#     delimiter = start - 1

#     for index in range(start, end):

#         if numbers[index] <= pivot:
#             delimiter = delimiter + 1
#             numbers[index], numbers[delimiter] = (
#                 numbers[delimiter],
#                 numbers[index],
#             )

#     numbers[delimiter + 1], numbers[end] = numbers[end], numbers[delimiter + 1]

#     return delimiter + 1
