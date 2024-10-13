def calculate(nums: list , operation: str = "sum") -> int :
    if operation == "sum":
        return sum(nums)
    elif operation == "product":
        result = 1
        for num in nums:
            result *= num
        return result
print (calculate([1,2,3,4],"sum"))
print (calculate([5,3,2],"product"))