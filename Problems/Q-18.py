class solution:
    def __init__(self,nums:list[int]):
        j=0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
print("enter the list of numbers:")
nums=list(map(int,input().split()))
s=solution(nums)
print("the modified list is:",nums)