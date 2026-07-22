class Solution(object):
    def containsDuplicate(self, nums):
        i = 0
        while i < len(nums):
            target = nums[i]
            nums.remove(target)
            if target in nums:
                return True
        return False
    