def removeDuplicates(nums):
    if len(nums)==0:
        return 0
    p1 =0
    for p2 in range(1, len(nums)):
        if nums[p1]!=nums[p2]:
            p1+=1
            nums[p1]=nums[p2]
    return p1+1
nums=[0,0,0,1,1,2]
res=removeDuplicates(nums)
print(res)