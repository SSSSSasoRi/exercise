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
