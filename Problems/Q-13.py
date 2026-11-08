#maximum number
def maxnum(nums):
    maximum=nums[0]
    for i in nums:
        if i>maximum:
            maximum=i
    return maximum
print(maxnum([1,3,45,9,7,2]))