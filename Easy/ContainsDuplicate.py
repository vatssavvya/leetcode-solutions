class Solution(object):
    def containsDuplicate(self, nums):
        for num in nums:
            target = num
            nums.remove(num)
            if target in nums:
                return True
        return False
    