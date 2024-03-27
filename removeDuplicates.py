class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        pre_num = nums[0]
        for i in range(1, len(nums)):
            if pre_num == nums[i]:
                nums[i] = '_'
            else :
                pre_num = nums[i]
                k += 1
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == '_' and nums[j] != '_':
                nums[i], nums[j] = nums[j], nums[i]
                
            elif nums[i] == '_' and nums[j] == '_':
                j = j + 1
            else:
                i = i + 1
                j  = j + 1
        return k
    
test = Solution()
print(test.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))