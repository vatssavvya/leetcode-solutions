class Solution(object):
    def containsDuplicate(self, nums):
        for num in nums:
            target = num
            nums.remove(num)
            if target in num:
                return True
        return False
    