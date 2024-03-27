# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if  nums[i] + nums[j] == target:
#                     return [i, j]
#         return None


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        maps = {}
        for  idx, num in enumerate(nums):
            temp = target - num
            if temp in maps:
                return [maps[temp],idx]
            maps[num] = idx
        return None
    
test =  Solution()
print(test.twoSum([2,7,11,15], 9))