def two_sum(nums, target):
    i = 0
    j = 0
    n = len(nums)
    while i < n - 1:
        if nums[i] + nums[j] == target:
            return [i, j]
        else:
            if j < n - 1:
                j += 1
            else:
                i += 1
                j = i + 1
    return None
# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  