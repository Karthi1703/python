def find_largest(nums: list) -> int:
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

print(find_largest(nums = [2,3,0,11,86]))