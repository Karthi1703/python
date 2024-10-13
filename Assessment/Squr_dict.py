def square_dict(nums: list) -> dict:
    return{num:num**2 for num in nums}
print(square_dict([1,2,3,4]))