def min(nums):
    result = 999999999999999999
    for x in nums:
        if result > x:
            result = x
    return result


def max(nums):
    result = -999999999999999999
    for x in nums:
        if result < x:
            result = x
    return result


def mean(nums):
    sum = 0
    for n in nums:
        sum = sum + n
    result = sum / len(nums)
    return result


def second_max(nums):
    result = -999999999999999999
    for x in nums:
        if x == max(nums):
            continue
        if x > result:
            result = x
    return result


def count_number(nums, a, b):
    result = 0
    for x in nums:
        if x >= a and x <= b:
            result = result + 1
    return result


def sum_number_range(nums, a, b):
    result = 0
    for x in nums:
        if x >= a and x <= b:
            result = result + x
    return result
