"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order
Example 1: Input: nums = [2,7,11,15], target = 9 Output: [0,1] Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. 
Example 2: Input: nums = [3,2,4], target = 6 Output: [1,2] 
Example 3: Input: nums = [3,3], target = 6 Output: [0,1]
Your solution need not be the most efficient one. Of course you are encouraged to come out with the most efficient solution
"""

#loop and check first and next index 

def find(nums, target):
# write your implementation here
    
    for i in range(len(nums)):
        for j in range (i+1, len(nums)): 
            if nums[i] + nums[j] == target:
                return [i, j]

print(find([2, 7, 11, 15], 9))
print(find([3,2,4], 6))
print(find([3,3], 6))
