def running_sum(nums):
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result

# Test
print(running_sum([1,2,3,4]))  # [1,3,6,10]
print(running_sum([1,1,1,1]))  # [1,2,3,4]
