class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
               seen.add(nums[i])
            else:
                return True
        return False      
        
        
        
        
        
        """
        :type nums: List[int]
        :rtype: bool
        """
        