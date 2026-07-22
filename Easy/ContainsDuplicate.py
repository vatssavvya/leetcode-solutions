class Solution(object):
    def containsDuplicate(self, nums):
       newNums = set(nums)
       return (len(nums) != len(newNums))       

    