class Solution:
    def twoSum(nums,target):
        mem={}       
        for i,each in enumerate(nums):
            if(target-each in mem):
                return mem[target-each],i
            mem[each]=i
    
    nums=[1,2,7,11,15,3]
    target=16
    c=twoSum(nums,target)
    print(c)